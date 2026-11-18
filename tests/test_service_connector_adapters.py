"""Service-specific input contracts, source custody and bounded HTTP execution."""
from __future__ import annotations

import copy
import hashlib
import importlib.util
import io
import json
from pathlib import Path
import tempfile
import subprocess
import sys
import unittest
import urllib.error
from unittest.mock import patch

ROOT=Path(__file__).resolve().parents[1]
DIRECTORY=ROOT/'docs/connectors'


def load(name,path):
    spec=importlib.util.spec_from_file_location(name,path)
    module=importlib.util.module_from_spec(spec);spec.loader.exec_module(module)
    return module


connector=load('service_connector',DIRECTORY/'connector.py')
catalog=load('service_connector_catalog',ROOT/'scripts/connector_catalog.py')
convert=load('service_connector_converter',ROOT/'scripts/import_service_connectors.py')


class SourceContractTests(unittest.TestCase):
    def test_distinct_services_fill_practical_gaps(self):
        data=catalog.load_catalog();by_id={row['id']:row for row in data['connectors']}
        self.assertGreater(len(by_id),250)
        self.assertEqual(len([r for r in by_id.values() if r.get('source_id','muse-connectors')=='muse-connectors']),151)
        for ident in ['google-drive','gmail','salesforce','zendesk','trello','dropbox','postgres','qdrant','snowflake','woocommerce','xero','zoom','contentful','datadog']:
            with self.subTest(service=ident):
                self.assertIn(ident,by_id)
                actual=connector.inspect(ident)
                self.assertTrue(actual['operations'])
                self.assertTrue(by_id[ident]['specialists'])

    def test_every_converted_action_has_its_own_pinned_definition(self):
        source=json.loads((DIRECTORY/'ADAPTER_SOURCES.json').read_bytes())
        for record in source['connectors']:
            adapter=connector.contract(record['id'])
            files={f['path']:f for f in record['source_files']}
            for op in adapter['operations']:
                with self.subTest(service=record['id'],operation=op['id']):
                    self.assertEqual(op['source_sha256'],files[op['source_path']]['sha256'])
                    self.assertIn(source['commit'],op['source_url'])
                    self.assertTrue(op['name'])
                    self.assertEqual(len({v['name'] for v in op['inputs']}),len(op['inputs']))

    def test_catalog_sources_and_all_distributed_hashes_reconcile(self):
        receipt=catalog.check()
        self.assertEqual(receipt['connectors'],273)
        self.assertEqual(receipt['service_adapters'],122)
        self.assertGreater(receipt['service_operations'],900)

    def test_http_templates_are_distinct_and_primary_source_linked(self):
        count=0
        for path in (DIRECTORY/'services').glob('*/http.json'):
            service=path.parent.name;data=connector.contract(service,'http.json')
            normalized=set()
            for request in data['requests']:
                import re
                signature=re.sub(r'\{[^}]+\}','{}',request['url_template'])
                self.assertNotIn(signature,normalized);normalized.add(signature)
                result=connector.prepare_read(service,request['id'],{p:'example-record' for p in request['parameters']})
                self.assertEqual(result['method'],'GET')
                self.assertIn('github.com/activepieces/activepieces/blob/511019',result['source_url'])
                count+=1
        self.assertGreaterEqual(count,20)

    def test_converter_retains_dynamic_provider_input_names(self):
        source="""export const action=createAction({name:'find',displayName:'Find Item',description:'Find a matching item.',props:{workspaceId:common.workspace(),limit:Property.Number({displayName:'Limit',required:false}),name:Property.ShortText({displayName:'Name',required:true})},async run(context){return /[{}'\"]/g.test('ok');}});"""
        parsed=convert.parse_operation(source.encode(),'example/src/lib/actions/find.ts')
        fields={v['name']:v for v in parsed['inputs']}
        self.assertEqual(set(fields),{'workspaceId','limit','name'})
        self.assertIsNone(fields['workspaceId']['required'])
        self.assertTrue(fields['name']['required']);self.assertFalse(fields['limit']['required'])
        self.assertEqual(fields['workspaceId']['source_expression'],'common.workspace()')

    def test_tampered_contract_is_rejected_before_planning(self):
        with tempfile.TemporaryDirectory() as temporary:
            root=Path(temporary);(root/'services/gmail').mkdir(parents=True)
            (root/'ADAPTER_SOURCES.json').write_bytes((DIRECTORY/'ADAPTER_SOURCES.json').read_bytes())
            (root/'services/gmail/adapter.json').write_bytes(b'{"id":"gmail"}')
            with self.assertRaisesRegex(connector.ConnectorError,'SERVICE_CONTRACT_CHANGED'):
                connector.contract('gmail',root=root)

    def test_path_escape_and_unknown_action_are_rejected(self):
        for service in ['../gmail','/tmp/private','gmail/../../x','Gmail']:
            with self.subTest(service=service),self.assertRaises(connector.ConnectorError):
                connector.inspect(service)
        with self.assertRaisesRegex(connector.ConnectorError,'UNKNOWN_ACTION'):
            connector.plan('gmail','invented-action')

    def test_preparing_action_reports_missing_and_rejects_unknown_inputs(self):
        adapter=connector.contract('trello')
        action=next(op for op in adapter['operations'] if op['kind']=='action' and any(f['required'] is True for f in op['inputs']))
        result=connector.plan('trello',action['id'])
        self.assertFalse(result['ready']);self.assertTrue(result['missing_required_inputs'])
        with self.assertRaisesRegex(connector.ConnectorError,'UNKNOWN_INPUTS'):
            connector.plan('trello',action['id'],{'undocumentedField':1})

    def test_all_specialist_packages_include_relevant_connector_closure(self):
        import re
        for role in catalog._roles():
            files=catalog.specialist_package_files(role)
            doc=json.loads(files['connectors/catalog.json'])
            with self.subTest(role=role):
                self.assertGreater(doc['service_adapters'],0)
                self.assertTrue(all(role in row['specialists'] for row in doc['connectors']))
                self.assertIn('CONNECTORS.md',files)
                self.assertIn('connectors/connector.py',files)
                manifest=json.loads(files['connectors/ADAPTER_SOURCES.json'])
                for record in manifest['connectors']:
                    for path,digest in record['files'].items():
                        self.assertEqual(hashlib.sha256(files['connectors/'+path]).hexdigest(),digest)
                for path,raw in files.items():
                    if not path.endswith('.md'):continue
                    for url in re.findall(r'(?<!!)\[[^\]]+\]\(([^)]+)\)',raw.decode()):
                        if url.startswith(('https:','http:','mailto:','#')):continue
                        from posixpath import normpath,join,dirname
                        resolved=normpath(join(dirname(path),url.split('#')[0]))
                        self.assertTrue(resolved in files or resolved=='PROFILE.md',(role,path,url))

    def test_extracted_specialist_connector_planner_works_independently(self):
        files=catalog.specialist_package_files('software-engineer')
        with tempfile.TemporaryDirectory() as temporary:
            directory=Path(temporary)
            for name,raw in files.items():
                path=directory/name;path.parent.mkdir(parents=True,exist_ok=True);path.write_bytes(raw)
            adapter=json.loads(files['connectors/services/trello/adapter.json'])
            action=next(op for op in adapter['operations'] if op['kind']=='action' and op['name']=='Get Card')
            fields={field['name']:'sample-card' for field in action['inputs']}
            input_path=directory/'inputs.json';input_path.write_text(json.dumps(fields),encoding='utf-8')
            result=subprocess.run([sys.executable,'-B',str(directory/'connectors/connector.py'),'plan','trello',action['id'],'--inputs',str(input_path)],capture_output=True,text=True,timeout=15,cwd=directory)
            self.assertEqual(result.returncode,0,result.stderr+result.stdout)
            planned=json.loads(result.stdout)
            self.assertEqual(planned['service'],'trello');self.assertEqual(planned['inputs'],fields)
            self.assertTrue(planned['ready'])


class HttpReadTests(unittest.TestCase):
    def setUp(self):
        self.directory=tempfile.TemporaryDirectory();self.addCleanup(self.directory.cleanup)
        self.output=Path(self.directory.name)/'result.json'
        self.prepared=connector.prepare_read('gmail','read-gmail-v1-users-me-profile')

    def fake_opener(self,raw=b'{"emailAddress":"sample@example.invalid","messagesTotal":3}',status=200):
        response=io.BytesIO(raw);response.status=status
        class Opener:
            seen=[]
            def open(self,request,timeout):
                self.seen.append((request,timeout));return response
        return Opener()

    def test_valid_read_writes_actual_response_and_keeps_token_out_of_receipt(self):
        opener=self.fake_opener()
        result=connector.execute_read(self.prepared,'MUSE_GMAIL_TOKEN',self.output,environment={'MUSE_GMAIL_TOKEN':'synthetic-test-token'},opener=opener)
        self.assertEqual(result['status'],'SAVED')
        self.assertEqual(json.loads(self.output.read_bytes())['response']['messagesTotal'],3)
        request,timeout=opener.seen[0]
        self.assertEqual(request.get_header('Authorization'),'Bearer synthetic-test-token')
        self.assertEqual(timeout,30)
        self.assertNotIn('synthetic-test-token',json.dumps(result))
        self.assertEqual(request.full_url,'https://gmail.googleapis.com/gmail/v1/users/me/profile')

    def test_dry_run_uses_no_credentials_and_sends_no_network_request(self):
        with patch.object(connector.urllib.request,'build_opener',side_effect=AssertionError('network call')):
            result=connector.prepare_read('gmail','read-gmail-v1-users-me-profile')
        self.assertNotIn('token',json.dumps(result).lower())

    def test_route_parameters_are_encoded_without_changing_host_or_query(self):
        result=connector.prepare_read('gmail','read-gmail-v1-users-me-messages-message-id',{'message_id':'https://other.invalid/../../x?token=bad#tail'})
        self.assertTrue(result['url'].startswith('https://gmail.googleapis.com/'))
        self.assertIn('%3Ftoken%3Dbad%23tail',result['url'])
        self.assertNotIn('?token=',result['url'])

    def test_unknown_or_missing_http_parameters_fail(self):
        for values in ({},{'message_id':'x','host':'evil.invalid'}):
            with self.assertRaisesRegex(connector.ConnectorError,'HTTP_INPUTS_MISMATCH'):
                connector.prepare_read('gmail','read-gmail-v1-users-me-messages-message-id',values)

    def test_missing_token_and_header_injection_fail_before_network(self):
        for value in ('','bad\r\nInjected: true'):
            with self.assertRaises(connector.ConnectorError):
                connector.execute_read(self.prepared,'MUSE_GMAIL_TOKEN',self.output,environment={'MUSE_GMAIL_TOKEN':value},opener=self.fake_opener())
        self.assertFalse(self.output.exists())

    def test_existing_result_is_preserved(self):
        self.output.write_text('keep',encoding='utf-8')
        opener=self.fake_opener()
        with self.assertRaisesRegex(connector.ConnectorError,'OUTPUT_MUST_BE_A_NEW_ABSOLUTE_PATH'):
            connector.execute_read(self.prepared,'MUSE_GMAIL_TOKEN',self.output,environment={'MUSE_GMAIL_TOKEN':'test'},opener=opener)
        self.assertEqual(self.output.read_text(),'keep');self.assertEqual(opener.seen,[])

    def test_oversized_and_non_json_responses_create_no_output(self):
        for raw in (b'x'*(connector.MAX_RESPONSE_BYTES+1),b'<html>error</html>',b'{"number":NaN}'):
            with self.assertRaises(connector.ConnectorError):
                connector.execute_read(self.prepared,'MUSE_GMAIL_TOKEN',self.output,environment={'MUSE_GMAIL_TOKEN':'test'},opener=self.fake_opener(raw))
            self.assertFalse(self.output.exists())

    def test_provider_error_has_status_without_response_or_token(self):
        class Broken:
            def open(self,request,timeout):
                raise urllib.error.HTTPError(request.full_url,401,'sensitive provider message',{},None)
        with self.assertRaisesRegex(connector.ConnectorError,'^PROVIDER_HTTP_ERROR:401$'):
            connector.execute_read(self.prepared,'MUSE_GMAIL_TOKEN',self.output,environment={'MUSE_GMAIL_TOKEN':'test'},opener=Broken())

    def test_redirect_refuses_cross_host_and_same_host_forwarding(self):
        handler=connector._NoRedirect()
        for url in ('https://other.invalid/','https://gmail.googleapis.com/redirect'):
            with self.assertRaisesRegex(connector.ConnectorError,'REDIRECT_REFUSED'):
                handler.redirect_request(None,None,302,'redirect',{},url)


if __name__=='__main__':
    unittest.main()
