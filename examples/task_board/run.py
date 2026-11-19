#!/usr/bin/env python3
"""Open the Muse Task Board or run its complete save, plan and result example."""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
import secrets
import sys
import tempfile

HERE=Path(__file__).resolve().parent
sys.path.insert(0,str(HERE));sys.path.insert(0,str(HERE.parents[1]/'src'))
from board import demo
from muse_presets.personal_companion import CompanionScope
from muse_presets.space_server import make_server,RequestRefused


def make_board_server(database,*,token,authority,port=0):
    server=make_server(database,token=token,authority=authority,port=port)
    pages={}
    try:
        vendor=json.loads((HERE/'assets/vendor/SOURCE.json').read_bytes())
        for entry in vendor['files']:
            raw=(HERE/'assets/vendor'/entry['path']).read_bytes()
            if hashlib.sha256(raw).hexdigest()!=entry['sha256']:raise ValueError('VENDOR_FILE_CHANGED')
        for route,name,mime in [('/', 'index.html','text/html; charset=utf-8'),
            ('/board.js','board.js','text/javascript; charset=utf-8'),
            ('/board.css','board.css','text/css; charset=utf-8'),
            ('/sortable.min.js','vendor/sortable.min.js','text/javascript; charset=utf-8')]:
            path=HERE/'assets'/name
            if path.is_symlink() or not path.is_file() or path.stat().st_size>131072:raise ValueError('BOARD_ASSET_INVALID')
            pages[route]=(mime,path.read_bytes())
    except BaseException:server.server_close();raise
    parent=server.RequestHandlerClass
    class BoardHandler(parent):
        def do_GET(self):
            if self.path not in pages:return super().do_GET()
            try:
                self._headers(False)
                mime,raw=pages[self.path]
                self._reply(200,raw,mime)
            except RequestRefused as error:self._reply(error.status,{'error':error.code})
    server.RequestHandlerClass=BoardHandler
    return server


def main(argv=None):
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--serve',action='store_true');p.add_argument('--database',type=Path)
    p.add_argument('--port',type=int,default=0);args=p.parse_args(argv)
    scope=CompanionScope('board-owner','task-board','board-owner',True)
    if not args.serve:
        with tempfile.TemporaryDirectory() as directory:
            print(json.dumps(demo(Path(directory)/'board.db',lambda:scope),ensure_ascii=False,indent=2))
        return 0
    if args.database is None:p.error('--serve requires an absolute --database path in an existing directory')
    token=secrets.token_urlsafe(36)
    server=make_board_server(args.database,token=token,authority=lambda:scope,port=args.port)
    print('Muse Task Board',flush=True)
    print('Open http://127.0.0.1:'+str(server.server_address[1]),flush=True)
    print('Session key: '+token,flush=True)
    try:server.serve_forever()
    except KeyboardInterrupt:pass
    finally:server.server_close()
    return 0


if __name__=='__main__':raise SystemExit(main())
