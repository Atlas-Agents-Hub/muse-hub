#!/usr/bin/env python3
"""Convert a pinned workflow source tree into portable Muse recipes and task starters.

The importer reads JSON as data. It retains transformations and branch conditions,
replaces account-specific settings with named inputs, and packages complete graph
resources alongside the skill methods used by each recipe.
"""
from __future__ import annotations

import argparse
from collections import Counter, defaultdict
import hashlib
import json
from pathlib import Path
import re
import sys
import unicodedata
from urllib.parse import quote, parse_qsl, urlsplit

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / 'tools'))
import workflow_library

REPOSITORY = 'enescingoz/awesome-n8n-templates'
REVISION = '827110332c21cbe000ab13f6d292d5adb1f1f8db'
SCHEMA = 'muse-workflow-graph/v1'
IGNORE_KEYS = {'__rl', 'cachedResultName', 'cachedResultUrl', 'nodeCredentialType',
               'genericAuthType', 'authentication', 'credentialType'}
IDENTIFIER_KEYS = {'id', 'chatid', 'channelid', 'calendarid', 'documentid', 'sheetid',
    'folderid', 'fileid', 'databaseid', 'tableid', 'baseid', 'teamid', 'projectid',
    'workspaceid', 'listid', 'boardid', 'userid', 'assistantid', 'threadid',
    'webhookid', 'workflowid', 'sessionkey', 'recipient', 'recipients', 'sendto',
    'fromemail', 'toemail', 'email', 'phonenumber', 'destination', 'bucketname'}
SECRET = re.compile(r'password|secret|credential|authorization|bearer|access.?token|api.?key|private.?key', re.I)
EMAIL = re.compile(r'\b[A-Za-z0-9.!#$%&\x27*+/=?^_`{|}~-]+@[A-Za-z0-9-]+(?:\.[A-Za-z0-9-]+)+\b')
OPAQUE = re.compile(r'(?<![A-Za-z0-9_])[A-Za-z0-9_-]{28,}(?![A-Za-z0-9_])')
PROVIDER = re.compile(r'\b(?:OpenAI|Open AI|ChatGPT|GPT[- ]?[345](?:\.[015])?(?:[- ]?o)?(?:[- ]?mini)?|Google Gemini|Gemini|Anthropic|Claude|Mistral\.ai|DeepSeek|Groq)\b',re.I)
SAFE_LABEL = re.compile(r'[^A-Za-z0-9 ,.:;!?&()\[\]/+\-_%]')

DOMAIN = {
    'AI_Research_RAG_and_Data_Analysis': ('research-and-data', 'research-evaluator', ['rag-architect','data-quality-auditor']),
    'Database_and_Storage': ('data-engineering','data-engineer',['database-designer','data-quality-auditor']),
    'Google_Drive_and_Google_Sheets': ('documents-and-data','data-engineer',['file-organizer','data-quality-auditor']),
    'PDF_and_Document_Processing': ('documents-and-data','data-engineer',['md-document','data-quality-auditor']),
    'OpenAI_and_LLMs': ('ai-and-automation','model-builder',['agent-designer','agent-evaluation']),
    'Gmail_and_Email_Automation': ('email-and-communication','automation-engineer',['email-template-builder','automation-contract']),
    'Instagram_Twitter_Social_Media': ('creative-and-content','creative-studio',['social-content','content-production']),
    'HR_and_Recruitment': ('business-and-projects','coordinator',['interview-system-designer','process-mapper']),
    'Forms_and_Surveys': ('research-and-feedback','research-evaluator',['survey-designer','data-quality-auditor']),
    'devops': ('reliability-engineering','reliability-engineer',['observability-designer','runbook-generator']),
    'WordPress': ('creative-and-content','creative-studio',['wordpress-pro','content-production']),
    'Notion': ('knowledge-and-planning','personal-companion',['knowledge-ops','para-method']),
    'Airtable': ('data-engineering','data-engineer',['database-designer','data-quality-auditor']),
    'Slack': ('team-communication','automation-engineer',['support-ops','team-communications']),
    'Telegram': ('personal-and-team-automation','automation-engineer',['automation-contract','agent-designer']),
    'WhatsApp': ('personal-and-team-automation','automation-engineer',['automation-contract','support-ops']),
    'Discord': ('community-and-content','automation-engineer',['automation-contract','community-content']),
}
EXTENSION_BASE = {'data-engineer':'model-builder','reliability-engineer':'software-engineer',
                  'automation-engineer':'software-engineer','product-interface-designer':'creative-studio'}
OPERATOR = {
    'input': ('automation-contract', 'Receive the task input', 'Record the supplied event, file, or record batch and its selection criteria.', 'A named input record or bounded batch.', 'The input type, required fields, and selection scope match this request.'),
    'schedule': ('automation-contract', 'Set the requested timing', 'Use the requested time zone and cadence to define when this flow starts; retain a manual run option.', 'A trigger specification with a time zone and manual entry.', 'The next occurrence matches the requested local time and frequency.'),
    'map-fields': ('data-quality-auditor', 'Map the record fields', 'Apply the field assignments, type conversions, and expressions to the incoming records.', 'Mapped records with the expected field names and types.', 'Required fields survive mapping and record counts reconcile.'),
    'transform': ('javascript-pro', 'Transform the incoming records', 'Implement the included transformation using the current records and named step outputs; preserve its calculations and edge cases.', 'Transformed records plus a representative before-and-after example.', 'The example agrees with the transformation and invalid or empty input has a defined result.'),
    'filter': ('data-quality-auditor', 'Select the matching records', 'Evaluate the supplied conditions for each record and keep a separate count of matches and nonmatches.', 'Selected records and the corresponding match counts.', 'A matching record and a near-miss take the intended paths.'),
    'branch': ('automation-contract', 'Choose the next branch', 'Evaluate the branch rules in order and route the result to the corresponding numbered output.', 'The selected branch with the values used to make the decision.', 'Both a matching case and the fallback follow the correct edges.'),
    'join': ('data-quality-auditor', 'Combine the matching inputs', 'Join the incoming branches using the declared mode, matching keys, and unmatched-record policy.', 'A joined result with the match and unmatched counts.', 'Duplicate keys and missing partners produce the intended output cardinality.'),
    'batch': ('incremental-pipeline', 'Process a bounded batch', 'Apply the declared batch size, preserve order where needed, and carry the continuation cursor into the next batch.', 'Batch output and a continuation position.', 'Each input record is processed once and a restart continues from the saved position.'),
    'aggregate': ('pandas-pro', 'Aggregate the records', 'Group or collect the incoming values using the named fields and aggregation settings.', 'A grouped result with denominators and group sizes.', 'Totals reconcile with the eligible input rows and missing values follow the stated policy.'),
    'deduplicate': ('data-quality-auditor', 'Remove repeated records', 'Compare the configured identity fields and keep the selected representative of each distinct record.', 'Distinct records and a duplicate count.', 'Two records with the same identity collapse while different identities remain separate.'),
    'sort': ('pandas-pro', 'Order the result', 'Sort by the declared keys and directions with an explicit handling rule for missing values.', 'Records in the requested stable order.', 'Ties and missing sort keys preserve the intended ordering.'),
    'limit': ('data-quality-auditor', 'Bound the result size', 'Apply the requested record limit after the relevant filtering and ordering.', 'A bounded result and the total eligible count.', 'The retained count does not exceed the limit and selection order is consistent.'),
    'extract-document': ('md-document', 'Extract the document content', 'Read the configured file type and preserve text, structure, tables, and source locations needed by later stages.', 'Extracted document content linked to the original file.', 'Representative pages or records match the source and unreadable content is identified.'),
    'parse': ('data-quality-auditor', 'Parse the structured result', 'Parse the incoming payload against the declared format or schema, retaining the original text for any parse failure.', 'Typed records or an explicit parse-error record.', 'Valid samples parse and malformed or missing fields remain visible.'),
    'chunk': ('chunking-strategies', 'Divide the source material', 'Split the selected material using the configured size, overlap, separators, and source metadata.', 'Source-linked chunks with stable identifiers.', 'A boundary sample preserves meaning and overlapping chunks are traceable to the same source.'),
    'retrieve': ('rag-architect', 'Retrieve the relevant evidence', 'Use the configured corpus, query, and retrieval settings to collect evidence for the current request.', 'Ranked evidence with source identifiers and scores where available.', 'Relevant items are retrievable and unrelated or out-of-scope material is excluded.'),
    'embed': ('embeddings-guide', 'Create the retrieval representation', 'Use the configured embedding capability to represent the selected text, keeping model identity and vector dimensions with the result.', 'Vectors paired with stable source identifiers.', 'All vectors use one compatible dimension and each maps back to its original text.'),
    'model': ('agent-designer', 'Select the model capability', 'Choose an available model route suited to the requested text, vision, audio, or structured-output task.', 'A model configuration with the required input and output shape.', 'The configured route supports the task format and fits the requested runtime and cost limits.'),
    'generate': ('agent-designer', 'Produce the requested content', 'Use the supplied prompt, context, and output schema to produce the task result with the available model capability.', 'The requested answer, draft, analysis, or structured result.', 'The result follows the supplied context and schema and addresses the user request.'),
    'summarize': ('md-document', 'Summarize the source material', 'Summarize the selected source with its required sections, audience, and length while retaining consequential details.', 'A summary linked to its source material.', 'Names, quantities, dates, and key conclusions match the source.'),
    'classify': ('data-labeling', 'Classify the incoming content', 'Apply the supplied category definitions and retain the evidence supporting the selected label.', 'A label and the relevant source evidence for each item.', 'Ambiguous examples and items outside the category set are handled explicitly.'),
    'extract-fields': ('data-quality-auditor', 'Extract the requested fields', 'Extract the fields specified by the schema and keep their source context and missing-value state.', 'A structured record with source-linked values.', 'Each required field is present or marked missing; invented values are not substituted.'),
    'session': ('context-window-management', 'Keep the conversation context', 'Associate only the needed prior context with the current session and use the requested retention boundary.', 'A session-scoped context record.', 'A second session cannot read or overwrite this session’s context.'),
    'wait': ('effect-reconciliation', 'Wait for the required result', 'Use the declared delay or completion condition and record the job or event identifier before resuming.', 'A completion observation or a saved continuation point.', 'The flow resumes for the expected result and does not repeat a completed write.'),
    'respond': ('team-communications', 'Return the result', 'Format the result for its intended recipient or response channel, including the requested fields and attachments.', 'A finished response with its associated output files.', 'The response destination and contents match the request.'),
    'file': ('file-organizer', 'Prepare the output file', 'Read, convert, or write the requested file format using the selected input and output location.', 'A file in the requested format and its location.', 'The file opens correctly and its contents match the preceding step.'),
    'image': ('image-retoucher', 'Prepare the visual asset', 'Apply the requested image operation, dimensions, and export settings to the selected asset.', 'An image with the specified format and dimensions.', 'Inspect the visual result and confirm its dimensions and readability.'),
    'service-read': ('automation-contract', 'Read the selected service records', 'Use the configured service operation and its filters to retrieve the selected records or resource.', 'A service result with source identifiers and pagination state.', 'The selected account, resource, fields, and complete page range match the request.'),
    'service-write': ('effect-reconciliation', 'Apply the requested service update', 'Prepare the configured operation using the prior output, perform the requested update, and retain the returned identifier.', 'The service result and a readback of the affected resource.', 'The exact target and payload match the request; the returned record confirms the effect.'),
    'http': ('automation-contract', 'Call the configured endpoint', 'Use the configured HTTP method, URL, headers, and body with the expected response format.', 'A response with status, typed body, and relevant pagination or job identifiers.', 'The response status and body satisfy the operation contract and the request targets the selected service.'),
    'inspect': ('data-quality-auditor', 'Inspect the intermediate result', 'Inspect the incoming data at this point and retain the fields required by the next operation.', 'An inspected intermediate result.', 'The expected records and fields are present before the flow continues.'),
}


def json_bytes(value):
    return (json.dumps(value, ensure_ascii=False, indent=2, allow_nan=False) + '\n').encode()


def slug(value, limit=86):
    plain = unicodedata.normalize('NFKD', value).encode('ascii', 'ignore').decode().lower()
    return re.sub(r'[^a-z0-9]+', '-', plain).strip('-')[:limit].rstrip('-') or 'workflow'


def display(value):
    value = re.sub(r'[\x00-\x1f\u202a-\u202e\u2066-\u2069]', ' ', str(value))
    value = EMAIL.sub('selected contact', value)
    value = re.sub(r'\s+', ' ', value).strip()
    return value[:240]


def clean_title(path):
    title = path.stem.replace('_', ' ')
    title = PROVIDER.sub('Muse', title)
    title = re.sub(r'\bn8n\b', 'Muse', title, flags=re.I)
    title = re.sub(r'\bAI[- ]Powered\s*', '', title, flags=re.I)
    title = re.sub(r'\bAI Agent\b', 'Assistant', title, flags=re.I)
    title = re.sub(r'\bMuse\s*(?:and|&|,)\s*Muse\b', 'Muse', title, flags=re.I)
    title = re.sub(r'\busing Muse\s*$', '', title, flags=re.I)
    title = re.sub(r'\bwith Muse\s*$', '', title, flags=re.I)
    title = re.sub(r'\s*[-–—,:]\s*$', '', title).strip()
    return display(title)


def kind(node):
    name = node['type'].split('.')[-1]
    params = node.get('parameters', {})
    if name.startswith(('lmChat', 'lmOpen', 'lmOllama')):
        return 'model', 'model'
    if name.startswith('embeddings'):
        return 'embed', 'embedding'
    if name.startswith('vectorStore') or name.startswith('retriever') or name == 'toolVectorStore':
        return 'retrieve', 'vector-store'
    if name.startswith('memory'):
        return 'session', 'session-store'
    if name.startswith('textSplitter'):
        return 'chunk', 'local'
    if name.startswith('document') or name in ('extractFromFile','readPDF'):
        return 'extract-document', 'local'
    if name.startswith('outputParser'):
        return 'parse', 'local'
    if name in ('scheduleTrigger','cron','interval'):
        return 'schedule', 'scheduler'
    if name.endswith('Trigger') or name in ('manualTrigger','start','webhook','chatTrigger','manualChatTrigger'):
        return 'input', 'muse'
    local = {'set':'map-fields','code':'transform','function':'transform','functionItem':'transform',
      'toolCode':'transform','toolCalculator':'transform','crypto':'transform','dateTime':'transform',
      'if':'branch','switch':'branch','filter':'filter','merge':'join','splitInBatches':'batch',
      'splitOut':'batch','itemLists':'aggregate','aggregate':'aggregate','summarize':'aggregate',
      'removeDuplicates':'deduplicate','sort':'sort','limit':'limit','html':'parse',
      'markdown':'file','convertToFile':'file','compression':'file','moveBinaryData':'file',
      'spreadsheetFile':'file','readBinaryFile':'file','readBinaryFiles':'file','writeBinaryFile':'file',
      'readWriteFile':'file','editImage':'image','wait':'wait','noOp':'inspect','stopAndError':'inspect',
      'executionData':'inspect'}
    if name in local:
        return local[name], 'local'
    if name in ('respondToWebhook','form'):
        return 'respond', 'muse'
    if name in ('httpRequest','httpRequestTool','toolHttpRequest','graphql'):
        return 'http', 'http'
    if name in ('agent','chainLlm','chainRetrievalQa','openAi','openAiAssistant'):
        return 'generate', 'model'
    if name == 'chainSummarization':
        return 'summarize', 'model'
    if name in ('textClassifier','sentimentAnalysis'):
        return 'classify', 'model'
    if name == 'informationExtractor':
        return 'extract-fields', 'model'
    if name in ('toolWorkflow','executeWorkflow','retrieverWorkflow'):
        return 'service-read', 'workflow'
    adapter = slug(re.sub(r'Tool$', '', name))
    operation = str(params.get('operation','')).lower()
    if operation in {'get','getall','search','list','read','lookup','getmany','query','find',
                     'download','select','fetch','getevent','getevents','getmessages'}:
        return 'service-read', adapter
    if operation in {'create','append','appendorupdate','update','upsert','delete','send',
                     'sendmessage','upload','post','add','reply','message','sendphoto'}:
        return 'service-write', adapter
    if name in ('gmail','telegram','slack','emailSend','discord','whatsApp','twilio','twitter','linkedIn','wordpress'):
        return 'service-write', adapter
    return 'service-read', adapter


class Sanitizer:
    def __init__(self, names):
        self.configuration = []
        self.names = names
        self.counter = Counter()

    def slot(self, node, path, reason):
        stem = slug(node + '-' + '-'.join(path[-3:]), 72)
        self.counter[stem] += 1
        key = stem if self.counter[stem] == 1 else stem + '-' + str(self.counter[stem])
        self.configuration.append({'id':key,'purpose':reason,'required':True})
        return {'configuration_input':key}

    def expression(self, text):
        text = text.removeprefix('=').strip()
        references=re.findall(r"\$\(\s*['\"]([^'\"]+)['\"]\s*\)|\$node\[['\"]([^'\"]+)['\"]\]",text)
        unknown={a or b for a,b in references}-{*self.names}
        if unknown:
            raise ValueError('unresolved parameter node reference')
        text = re.sub(r"\$\(\s*(['\"])(.*?)\1\s*\)",
                      lambda m: 'steps[' + json.dumps(self.names.get(m.group(2), display(m.group(2)))) + ']', text)
        text = re.sub(r"\$node\[(['\"])(.*?)\1\]",
                      lambda m: 'steps[' + json.dumps(self.names.get(m.group(2),display(m.group(2)))) + ']', text)
        text = text.replace('$json', 'record').replace('$input.all()', 'records').replace('$input.first()', 'records[0]')
        text = text.replace('$input.item', 'record').replace('$now', 'current_time').replace('$today', 'current_date')
        text = text.replace('$execution.id','run_id').replace('$workflow.id','workflow_id')
        text = text.replace('$runIndex','batch_index').replace('$itemIndex','record_index')
        text = re.sub(r'(steps\[[^\]]+\])\.item\.json',r'\1.record',text)
        text = re.sub(r'(steps\[[^\]]+\])\.first\(\)\.json',r'\1.records[0]',text)
        text = EMAIL.sub('[configured contact]', text)
        text = re.sub(r'\b(?:sk-[A-Za-z0-9_-]{15,}|Bearer\s+[A-Za-z0-9._-]{15,})', '[configured credential]', text)
        return text

    def clean(self, value, node, path=()):
        key = path[-1] if path else ''
        lower = key.lower().replace('_','').replace('-','')
        if isinstance(value,dict):
            if value.get('__rl') is True:
                candidate = value.get('value')
                if isinstance(candidate,str) and ('{{' in candidate or candidate.startswith('=')):
                    return {'expression':self.expression(candidate)}
                return self.slot(node,path,'Select the ' + ' / '.join(path) + ' for this task.')
            if 'name' in value and SECRET.search(str(value['name'])):
                return {k: self.slot(node,path+(k,), 'Configure the named authentication setting in the selected service connection.') if k=='value'
                        else self.clean(v,node,path+(k,)) for k,v in value.items() if k not in IGNORE_KEYS}
            return {k:self.clean(v,node,path+(k,)) for k,v in value.items()
                    if k not in IGNORE_KEYS and not (k=='id' and isinstance(v,str))}
        if isinstance(value,list):
            return [self.clean(v,node,path+(str(i),)) for i,v in enumerate(value)]
        if isinstance(value,str):
            if lower in ('model','modelid','modelname','deploymentname') and value:
                return self.slot(node,path,'Select an available model with the required input and output capability.')
            if SECRET.search(key) and value and not ('{{' in value or value.startswith('=')):
                return self.slot(node,path,'Configure ' + display(key) + ' in the selected service connection.')
            if lower in IDENTIFIER_KEYS and value and not ('{{' in value or value.startswith('=')):
                return self.slot(node,path,'Select the ' + display(key) + ' for ' + node + '.')
            if key in ('jsCode','functionCode','pythonCode'):
                value=re.sub(r"(['\"])([A-Za-z0-9_=-]{28,})\1",
                    lambda m:json.dumps('{{input:'+self.slot(node,path+('literal',),
                        'Provide the configured resource or key used by this transformation.')['configuration_input']+'}}'),value)
                return {'language':'python' if key=='pythonCode' else 'javascript',
                        'reference': self.expression(value), 'inputs':'records, record, and named steps'}
            if '{{' in value or value.startswith('='):
                return {'expression': self.expression(value)}
            if re.search(r'ignore (?:all |any |previous )*(?:instructions|rules)|reveal.*system.prompt',value,re.I):
                return self.slot(node,path,'Provide task instructions and the expected output format.')
            if EMAIL.search(value) or re.fullmatch(r'\+?\d[\d ()-]{9,}',value):
                return self.slot(node,path,'Provide the contact, recipient, or message content for ' + display(key) + '.')
            if value.startswith(('http://','https://')):
                # Every network target is supplied by the person running this recipe.
                # The adapter and source operation retain the service and API context.
                result=self.slot(node,path,'Set the ' + display(key) + ' endpoint or source URL for this operation.')
                parsed=urlsplit(value)
                host=parsed.hostname or ''
                if host and not re.fullmatch(r'[\d.:]+',host) and host not in ('localhost',):
                    for suffix in ('.atlassian.net','.myshopify.com','.sharepoint.com','.supabase.co','.n8n.cloud'):
                        if host.endswith(suffix):host='{account}'+suffix
                    route=re.sub(r'/[A-Za-z0-9_-]{18,}', '/{resource}', parsed.path)
                    route=re.sub(r'/\d{5,}', '/{resource}', route)
                    route=re.sub(r'/bot[^/]+','/bot{credential}',route)
                    query='&'.join(quote(k)+'={value}' for k,_ in parse_qsl(parsed.query,keep_blank_values=True))
                    self.configuration[-1]['endpoint_template']=parsed.scheme+'://'+host+route+('?' +query if query else '')
                return result
            if OPAQUE.search(value) and len(value)<300:
                return self.slot(node,path,'Choose the ' + display(key) + ' resource value for this task.')
            if len(value)>25_000:
                return self.slot(node,path,'Provide the ' + display(key) + ' content for this operation.')
            if value.strip().startswith(('{','[')):
                try:nested=json.loads(value)
                except (ValueError,TypeError):pass
                else:return {'json':self.clean(nested,node,path+('body',))}
            return EMAIL.sub('[configured contact]', value)
        if isinstance(value,int) and lower in IDENTIFIER_KEYS:
            return self.slot(node,path,'Select the ' + display(key) + ' for this task.')
        return value


def convert(path, source_root, tree, skill_ids):
    raw = path.read_bytes()
    rel = path.relative_to(source_root).as_posix()
    expected = tree.get(rel)
    if expected is None or hashlib.sha1(b'blob ' + str(len(raw)).encode() + b'\0' + raw).hexdigest() != expected:
        raise ValueError('source blob mismatch: ' + rel)
    doc = json.loads(raw)
    if not isinstance(doc,dict) or not isinstance(doc.get('nodes'),list):
        return None,'not-workflow'
    nodes = [n for n in doc['nodes'] if n.get('type')!='n8n-nodes-base.stickyNote']
    if not 3 <= len(nodes) <= 40:
        return None,'complexity'
    if any(n.get('type','').endswith(('.executeCommand','.ssh')) for n in nodes):
        return None,'host-command'
    if len({n.get('name') for n in nodes}) != len(nodes):
        return None,'duplicate-node-name'
    title = clean_title(path)
    identity = 'flow-' + slug(title,78) + '-' + hashlib.sha256(rel.encode()).hexdigest()[:6]
    names = {n['name']:'step-'+str(i+1) for i,n in enumerate(nodes)}
    sanitizer = Sanitizer(names)
    converted = []
    for n in nodes:
        operation, adapter = kind(n)
        parameters = sanitizer.clean(n.get('parameters',{}), names[n['name']])
        if n.get('disabled'):
            operation,adapter='inspect','local'
            parameters={'bypass':True,'instruction':'Pass the incoming records to the next connected operation.'}
        if operation=='model':
            parameters={'capability':'text generation','settings':{k:v for k,v in parameters.get('options',{}).items()
                        if k in ('temperature','maxTokens','topP','frequencyPenalty','presencePenalty')}}
        if operation=='embed':
            parameters={'capability':'text embeddings','settings':{k:v for k,v in parameters.items() if k in ('dimensions','batchSize')}}
        label = display(PROVIDER.sub('Model',n['name']))
        if len(label)<3:label=OPERATOR[operation][1]
        converted.append({'id':names[n['name']],'label':label,'operation':operation,
                          'adapter':adapter,'parameters':parameters})
    edges=[];seen_edges=set();terminal=[]
    for source,channels in doc.get('connections',{}).items():
        if source not in names:raise ValueError('unresolved graph node reference')
        if not isinstance(channels,dict):raise ValueError('invalid source graph channels')
        for channel,branches in channels.items():
            if not isinstance(branches,list):raise ValueError('invalid source graph branches')
            for branch,targets in enumerate(branches):
                if targets is None or targets==[]:
                    terminal.append({'from':names[source],'channel':channel.removeprefix('ai_'),'branch':branch})
                    continue
                if not isinstance(targets,list):raise ValueError('invalid source graph targets')
                for target in targets:
                    if target.get('node') not in names:raise ValueError('unresolved graph node reference')
                    edge={'from':names[source],'to':names[target['node']],
                          'channel':channel.removeprefix('ai_'),'branch':branch,'input':target.get('index',0)}
                    signature=tuple(edge.values())
                    if signature in seen_edges:raise ValueError('duplicate source graph edge')
                    edges.append(edge);seen_edges.add(signature)
    # Expressions can read a named result without a direct control edge. Keep
    # those dependencies so disconnected or conditional sources remain visible.
    for node in converted:
        expression_text=json.dumps(node['parameters'],ensure_ascii=False)
        refs=set(re.findall(r'steps\[\\"(step-\d+)\\"\]',expression_text))
        for source in sorted(refs):
            if source==node['id']:continue
            if not any(e['from']==source and e['to']==node['id'] for e in edges):
                edges.append({'from':source,'to':node['id'],'channel':'data','branch':0,'input':0})
    if not edges:return None,'disconnected'
    connected={e[k] for e in edges for k in ('from','to')}
    converted=[n for n in converted if n['id'] in connected]
    if len(converted)<3:return None,'too-few-operations'
    # Include only inputs still referenced after generic model conversion.
    declared=json.dumps(converted,ensure_ascii=False)
    configuration=[c for c in sanitizer.configuration if json.dumps(c['id']) in declared or '{{input:'+c['id']+'}}' in declared]
    targets={e['to'] for e in edges}
    entrypoints=[n['id'] for n in converted if n['operation'] in ('input','schedule')] or [n['id'] for n in converted if n['id'] not in targets]
    if not entrypoints:return None,'no-entrypoint'
    category,role,domain_skills=DOMAIN.get(rel.split('/')[0],('automation-and-tools','automation-engineer',['automation-contract','data-quality-auditor']))
    domain_skills=[s if s in skill_ids else 'social-content' for s in domain_skills]
    source={'repository':REPOSITORY,'revision':REVISION,'path':rel,'git_blob':expected,
            'sha256':hashlib.sha256(raw).hexdigest(),'url':f'https://github.com/{REPOSITORY}/blob/{REVISION}/'+quote(rel,safe='/'),
            'author':'Enes Cingoz and template contributors','license':'CC-BY-4.0',
            'adaptation':'Muse operation graph, provider-neutral model bindings, named configuration inputs and connected skill methods'}
    graph={'schema':SCHEMA,'id':identity,'title':title,'nodes':converted,'edges':edges,
           'terminal_branches':[x for x in terminal if x['from'] in connected],
           'entrypoints':entrypoints,'configuration':configuration,'source':source}
    workflow_library.validate_graph(graph)
    ordered=workflow_library.plan(graph)
    order=[key for wave in ordered['waves'] for key in wave]+ordered['iterative_nodes']+ordered['waiting_on_iteration']
    by_id={n['id']:n for n in converted}
    stages=[]
    for key in order:
        node=by_id[key]; skill,heading,action,output,check=OPERATOR[node['operation']]
        context=[]
        for field in ('resource','operation','method','mode','format','dataType','documentType'):
            v=node['parameters'].get(field)
            if isinstance(v,(str,int,bool)) and v not in ('',None):context.append(field+' = '+str(v))
        detail=(' Operation settings: '+', '.join(context)+'.') if context else ''
        params=' Read `'+identity+'/WORKFLOW.json`, node `'+key+'`, for its exact field mappings, expressions, and settings.'
        incoming=[f"{e['from']} ({e['channel']}, branch {e['branch']}, input {e.get('input',0)})" for e in edges if e['to']==key]
        deps=(' Use the output from '+', '.join(incoming)+'.') if incoming else ' Start from the configured inputs.'
        ends=[str(x['branch']) for x in graph['terminal_branches'] if x['from']==key and x['channel']=='main']
        if ends:deps+=' Branch '+', '.join(ends)+' ends here; return its result without continuing to another operation.'
        stages.append({'title':node['label'],'skill_id':skill,
                       'action':action+detail+params+deps,
                       'output':node['label']+': '+output,
                       'check':check})
    skills=list(dict.fromkeys([s['skill_id'] for s in stages]))
    if len(skills)<2:
        skill=next(s for s in domain_skills if s not in skills) if any(s not in skills for s in domain_skills) else 'bounded-review'
        stages.append({'title':'Check the finished result','skill_id':skill,
            'action':'Inspect the complete result against the original task, the selected source, and the requested output format.',
            'output':'A checked result with its source and next action.','check':'The deliverable addresses the task and matches the selected source material.'})
        skills.append(skill)
    adapters=sorted({n['adapter'] for n in converted}-{ 'local','muse','model','embedding','session-store'})
    inputs=['The request and source material for '+title+'.',
            'The selected records, date range, and output destination.',
            'Complete the named fields in '+identity+'/INPUTS.json.']
    if adapters:inputs.append('Configured connections or tools for '+', '.join(adapters)+'.')
    if any(n['adapter'] in ('model','embedding') for n in converted):
        inputs.append('An available model or embedding capability with the requested format and cost limits.')
    finish='Deliver the requested result for “'+title+'”, including the source record identifiers and completed output location.'
    roles=list(dict.fromkeys([role,'automation-engineer']))
    row={'id':identity,'title':title,'goal':'Complete “'+title+'” with the connected steps, field mappings, and result checks below.',
         'roles':roles,'skills':skills,'steps':stages,'inputs':inputs,
         'checks':['Trace a representative input through the selected branches to its final result.',
                   'Check record counts, required fields, and the requested output format.',
                   'Read back each requested service change and preserve its returned identifier.'],
         'finish':finish,'source':source,
         'resources':{'path':'workflow-assets/'+identity,'files':{}}}
    return (row,graph,category,role),None


def starter_for(row,graph,category,role):
    title=row['title'];identity='task-'+row['id'][5:]
    base=EXTENSION_BASE.get(role,role)
    prompt=('Complete this task: “'+title+'”. Use the source material I provide, '
            'the selected records and date range, and my intended output destination. '
            'Follow the included workflow’s branches and field mappings, then return the finished result with the source identifiers and output location.')
    record={'id':identity,'title':title,'category':category,'base_role':base,
        'purpose':'Use the matching tools and data flow to complete “'+title+'”.',
        'first_task':prompt,'output':row['finish'],
        'tone':'Practical and clear; explain decisions that change the result.',
        'onboarding':[row['inputs'][0], 'Fill the named settings in the included INPUTS.json and select the available connections.'],
        'acceptance':row['checks'],'skills':row['skills'][:8],'workflows':[row['id']],
        'automatic_external_actions':False,'workflow_task':{'workflow':row['id'],'mode':'outcome'}}
    if role in EXTENSION_BASE:record['specialist_role']=role
    return record


FOCUS = {
  'branch': ('Test the decision rules', 'Use representative input records to test each decision rule in {title}. For {node}, show the field values, the selected branch, and an example that reaches the fallback. Return a compact branch test table and corrected conditions where a case routes incorrectly.', 'A branch test table with matching, nonmatching, and fallback examples.'),
  'map-fields': ('Prepare the field mapping', 'Map my source records for {title}. At {node}, preserve the intended field assignments and types, identify missing fields, and provide a before-and-after record example I can use in the workflow.', 'A field mapping, required-input list, and a checked sample output record.'),
  'extract-fields': ('Build the extraction schema', 'For {title}, use my source documents to define and check the field schema at {node}. Include source locations for extracted values, a missing-value rule, and examples of a valid and incomplete result.', 'An extraction schema and two source-linked example records.'),
  'retrieve': ('Check the retrieval inputs', 'Prepare the evidence retrieval for {title}. For {node}, inspect the supplied corpus, define a representative query set, and compare the returned source passages against those questions. Return the retrieval settings and a source-linked result table.', 'A query set, retrieval settings, and source-linked relevance checks.'),
  'aggregate': ('Reconcile the summary totals', 'For {title}, reconcile the grouped output at {node} against my supplied records. State the grouping keys, eligible-record count, missing-value treatment, and the calculation behind each total.', 'A reconciliation table with group sizes, calculation inputs, and explained differences.'),
  'transform': ('Verify the data transformation', 'Check the transformation at {node} in {title} using my sample input. Work through a normal record, an empty value, and an unusual boundary case, and return the transformed records with any necessary correction to the transformation.', 'Three checked transformation examples and a corrected mapping or calculation where needed.'),
  'classify': ('Calibrate the classification rules', 'Calibrate {node} for {title} using my sample messages or records. Define the labels, classify the samples with supporting text, and identify ambiguous examples that need a clearer category rule.', 'Category definitions, labeled examples, and a list of ambiguous cases.'),
  'deduplicate': ('Choose stable record identities', 'For {title}, inspect my repeated and near-duplicate records at {node}. Choose the identity fields, distinguish an exact repeat from a changed record, and return the retained records with a duplicate summary.', 'Stable identity fields, retained records, and an explained duplicate count.'),
  'parse': ('Validate the response structure', 'For {title}, validate the structured response at {node} against the sample payloads I provide. Keep the original failed payloads, identify the exact invalid fields, and return a corrected schema plus valid and invalid examples.', 'A response schema, passing examples, and field-level validation errors.'),
  'batch': ('Prepare a restartable batch', 'Prepare the batch step {node} for {title} using my record count, ordering requirement, and interruption scenario. Choose the batch boundary, define the saved cursor, and show which records a restart should process next.', 'A batch plan and an explicit restart example with record identifiers.'),
  'join': ('Check the record join', 'For {title}, check the join at {node} using my two input tables. Identify the matching keys and cardinality, then show matched records, unmatched records, and the effect of duplicate keys.', 'A join specification with matched, unmatched, and duplicate-key examples.'),
  'extract-document': ('Verify the document extraction', 'Check document extraction at {node} for {title} using my sample file. Compare representative text, tables, and page references with the original, then return a structured extraction with any unreadable sections identified.', 'A source-linked extraction and a page or section comparison table.'),
  'summarize': ('Shape the source summary', 'Create the summary at {node} for {title} using my source and intended audience. Preserve the consequential facts, identify the supporting passage for each key point, and deliver the summary in the workflow’s expected format.', 'A concise source-faithful summary with supporting passage references.'),
  'http': ('Prepare the API request contract', 'Prepare the API step {node} for {title} from the configured endpoint and sample response I provide. Define the method, required fields, pagination or job polling, and success/error response shapes, then return a request example and validation checklist.', 'A request contract, response examples, and pagination or polling instructions.'),
}


def focus_starters(imported, needed=120):
    pools=defaultdict(list)
    for row,graph,category,role in imported:
        for node in graph['nodes']:
            if node['operation'] in FOCUS:
                pools[node['operation']].append((row,graph,category,role,node))
    selected=[];seen=set();per_workflow=Counter()
    while len(selected)<needed:
        progressed=False
        for op in sorted(pools):
            while pools[op]:
                row,graph,category,role,node=pools[op].pop(0)
                signature=(op,re.sub(r'\d+$','',node['label']).lower(),
                           hashlib.sha256(json_bytes(node['parameters'])).hexdigest())
                if signature in seen or per_workflow[row['id']]>=1:continue
                seen.add(signature);per_workflow[row['id']]+=1
                heading,prompt,result=FOCUS[op]
                record=starter_for(row,graph,category,role)
                record['id']='focus-'+row['id'][5:]
                record['title']=heading+' — '+row['title']
                record['purpose']=heading+' for '+row['title']+' using the actual operation settings.'
                record['first_task']=prompt.format(title=row['title'],node=node['label'])
                record['output']=result
                record['workflow_task']={'workflow':row['id'],'mode':'operation','node':node['id']}
                record['acceptance']=[result+' All examples use the supplied source records.',
                  'The operation settings and selected fields match the included workflow graph.',
                  'The final examples cover the normal input and a relevant missing or boundary input.']
                selected.append(record);progressed=True;break
            if len(selected)>=needed:break
        if not progressed:break
    return selected


def main(argv=None):
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--source',type=Path,required=True)
    parser.add_argument('--tree',type=Path,required=True)
    parser.add_argument('--root',type=Path,default=ROOT)
    parser.add_argument('--report',type=Path,required=True)
    args=parser.parse_args(argv)
    root=args.root.resolve();source_root=args.source.resolve()
    tree_doc=json.loads(args.tree.read_bytes())
    if tree_doc.get('sha')!=REVISION or tree_doc.get('truncated') is not False:
        raise ValueError('complete pinned source tree required')
    tree={x['path']:x['sha'] for x in tree_doc['tree'] if x['type']=='blob'}
    skill_ids={x['id'] for x in json.loads((root/'collections/muse-starters-v1/skills.json').read_bytes())}
    skill_ids.update(x['id'] for x in json.loads((root/'collections/library/catalog.json').read_bytes())['skills'])
    imported=[];rejected=[];fingerprints=set();titles=set()
    for rel in sorted(tree):
        if not rel.endswith('.json'):continue
        path=source_root/rel
        try:result,reason=convert(path,source_root,tree,skill_ids)
        except (ValueError,TypeError,KeyError) as exc:
            rejected.append({'path':rel,'reason':str(exc)});continue
        if result is None:rejected.append({'path':rel,'reason':reason});continue
        row,graph,category,role=result
        signature=hashlib.sha256(json_bytes({'nodes':graph['nodes'],'edges':graph['edges']})).hexdigest()
        normalized=slug(row['title'],240)
        if signature in fingerprints or normalized in titles:
            rejected.append({'path':rel,'reason':'duplicate-graph-or-outcome'});continue
        fingerprints.add(signature);titles.add(normalized);imported.append(result)
    if len(imported)<200:raise ValueError('too few complete distinct workflows')
    license_raw=(source_root/'LICENSE').read_text(encoding='utf-8').replace('\r\n','\n').encode('utf-8')
    library=root/'collections/library'
    catalog=json.loads((library/'workflows.json').read_bytes())
    previous={row['id']:row for row in catalog['workflows'] if row.get('source',{}).get('repository')==REPOSITORY}
    catalog['workflows']=[row for row in catalog['workflows'] if row.get('source',{}).get('repository')!=REPOSITORY]
    current_ids={r['id'] for r in catalog['workflows']}
    for row,graph,category,role in imported:
        if row['id'] in current_ids:raise ValueError('workflow identifier collision')
        folder=library/row['resources']['path'];folder.mkdir(parents=True,exist_ok=True)
        inputs={'schema':'muse-workflow-inputs/v1','workflow':row['id'],
                'request':'Describe the result and provide the source material.',
                'selection':{'records':None,'date_range':None,'output_destination':None},
                'settings':{x['id']:None for x in graph['configuration']},
                'adapters':{a:{'connection':None} for a in sorted({n['adapter'] for n in graph['nodes']} - {'local','muse'})}}
        files={'WORKFLOW.json':json_bytes(graph),'INPUTS.json':json_bytes(inputs),'SOURCE_LICENSE.txt':license_raw}
        for name,raw in files.items():(folder/name).write_bytes(raw)
        row['resources']['files']={name:hashlib.sha256(raw).hexdigest() for name,raw in files.items()}
        catalog['workflows'].append(row)
    retained={row['id'] for row,_,_,_ in imported}
    for identity,old in previous.items():
        if identity in retained:continue
        resources=workflow_library.validate_resources(old)
        folder=library/resources['path']
        for name,digest in resources['files'].items():
            path=folder/name
            if not path.is_file() or path.is_symlink() or hashlib.sha256(path.read_bytes()).hexdigest()!=digest:
                raise ValueError('modified generated resource requires review: '+str(path))
        if set(p.name for p in folder.iterdir())!=set(resources['files']):
            raise ValueError('additional workflow files require review: '+str(folder))
        for name in resources['files']:(folder/name).unlink()
        folder.rmdir()
    starter_path=root/'collections/muse-starters-v1/starters.json'
    starters=[x for x in json.loads(starter_path.read_bytes()) if not x.get('workflow_task')]
    starters += [starter_for(*item) for item in imported]
    starters += focus_starters(imported, max(120, 505-len(starters)))
    if len(starters)<=500:raise ValueError('starter expansion incomplete')
    if len({s['id'] for s in starters})!=len(starters) or len({s['first_task'] for s in starters})!=len(starters):
        raise ValueError('duplicate task starter')
    (library/'workflows.json').write_bytes(json_bytes(catalog));starter_path.write_bytes(json_bytes(starters))
    args.report.write_bytes(json_bytes({'source':{'repository':REPOSITORY,'revision':REVISION},
        'added_workflows':len(imported),'total_library_workflows':len(catalog['workflows']),
        'total_starters':len(starters),'nodes':sum(len(g['nodes']) for _,g,_,_ in imported),
        'edges':sum(len(g['edges']) for _,g,_,_ in imported),
        'categories':dict(Counter(c for _,_,c,_ in imported)),'rejected':rejected}))
    print(json.dumps({'added_workflows':len(imported),'total_workflows':len(catalog['workflows'])+25,
                      'task_starters':len(starters),'source_revision':REVISION}))


if __name__=='__main__':
    main()
