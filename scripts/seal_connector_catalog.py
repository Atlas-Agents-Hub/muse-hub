"""Refresh the connector bundle's reproducible file inventory after generation."""
from pathlib import Path
import json

from connector_catalog import DIRECTORY, FILES, PIN, REPO, _canonical, _sha, check, load_catalog


def seal():
    doc=load_catalog()
    names=set(FILES)-{'PROVENANCE.json'}
    names.update({'ADAPTER_SOURCES.json','ACTIVEPIECES_LICENSE.txt','RUN_CONNECTORS.md','connector.py'})
    manifest=json.loads((DIRECTORY/'ADAPTER_SOURCES.json').read_bytes())
    for record in manifest['connectors']:
        for name,digest in record['files'].items():
            if _sha((DIRECTORY/name).read_bytes())!=digest:
                raise ValueError('ADAPTER_FILE_CHANGED:'+name)
            names.add(name)
    proof={'schema':'muse-connector-catalog-provenance/v2','connector_count':len(doc['connectors']),
           'source_commit':PIN,'source_repository':REPO,'connector_code_vendored':False,
           'upstream_code_executed':False,'service_adapter_count':len(manifest['connectors']),
           'distributed_files':{'docs/connectors/'+name:_sha((DIRECTORY/name).read_bytes()) for name in sorted(names)}}
    (DIRECTORY/'PROVENANCE.json').write_bytes(_canonical(proof))
    return check()


if __name__=='__main__':
    print(json.dumps(seal(),sort_keys=True))
