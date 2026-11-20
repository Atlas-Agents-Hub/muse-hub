"""Persistent task board using Muse Hub's notebook and request contracts."""
from __future__ import annotations

import hashlib
import json
from pathlib import Path
import sys

sys.path.insert(0,str(Path(__file__).resolve().parents[2]/'src'))
from muse_presets.personal_companion import PersonalCompanion
from muse_presets.space_companion import SpaceCompanion

SCHEMA='muse-task-board/v1'
NOTE_ID='muse-task-board'
STATES=('todo','doing','done')
PRIORITIES=('high','normal','low')
MAX_CARDS=24


def validate_board(board):
    import re
    if not isinstance(board,dict) or set(board)!={'schema','cards'} or board['schema']!=SCHEMA:
        raise ValueError('INVALID_BOARD')
    cards=board['cards']
    if not isinstance(cards,list) or len(cards)>MAX_CARDS:raise ValueError('CARD_LIMIT')
    ids=set()
    for card in cards:
        if not isinstance(card,dict) or set(card)!={'id','title','details','status','priority'}:
            raise ValueError('INVALID_CARD_FIELDS')
        if (not isinstance(card['id'],str) or not re.fullmatch(r'[a-zA-Z0-9_-]{1,60}',card['id'])
                or card['id'] in ids):raise ValueError('INVALID_CARD_ID')
        ids.add(card['id'])
        for key,limit in (('title',120),('details',240)):
            value=card[key]
            if not isinstance(value,str) or len(value)>limit or '\0' in value:
                raise ValueError('INVALID_CARD_TEXT')
        if not card['title'].strip():raise ValueError('CARD_TITLE_REQUIRED')
        if card['status'] not in STATES or card['priority'] not in PRIORITIES:
            raise ValueError('INVALID_CARD_STATE')
    if len(json.dumps(board,ensure_ascii=False,separators=(',',':')))>7500:
        raise ValueError('BOARD_SIZE_LIMIT')
    return board


def encode(board):
    validate_board(board)
    return json.dumps(board,ensure_ascii=False,separators=(',',':'))


class TaskBoard:
    def __init__(self,database,*,authority):
        self.database=database;self.authority=authority

    def snapshot(self):
        with PersonalCompanion(self.database,authority=self.authority) as store:
            record=store.note(NOTE_ID)
        if record is None:return {'board':{'schema':SCHEMA,'cards':[]},'revision':0}
        return {'board':validate_board(json.loads(record['text'])),'revision':record['revision']}

    def save(self,board,*,expected_revision):
        text=encode(board)
        with PersonalCompanion(self.database,authority=self.authority) as store:
            record=store.put_note(NOTE_ID,text,expected_revision=expected_revision)
        return {'board':board,'revision':record['revision']}

    def export(self):
        return (json.dumps(self.snapshot()['board'],ensure_ascii=False,indent=2)+'\n').encode('utf-8')

    def import_cards(self,raw,*,expected_revision):
        if not isinstance(raw,bytes) or len(raw)>65536:raise ValueError('INVALID_IMPORT')
        incoming=validate_board(json.loads(raw))
        current=self.snapshot()
        if current['revision']!=expected_revision:raise ValueError('STALE_REVISION')
        merged=json.loads(encode(current['board']));by_id={c['id']:c for c in merged['cards']}
        for card in incoming['cards']:
            old=by_id.get(card['id'])
            if old is not None and old!=card:raise ValueError('CARD_CONFLICT')
            if old is None:merged['cards'].append(card);by_id[card['id']]=card
        return self.save(merged,expected_revision=expected_revision)

    def queue_plan(self,request_id):
        board=self.snapshot()['board']
        prompt=json.dumps({'schema':'muse-board-plan/v1','task':'Choose the next three concrete actions from this board.',
            'cards':[{k:c[k] for k in ('id','title','status','priority')} for c in board['cards']]},ensure_ascii=False)
        with SpaceCompanion(self.database,authority=self.authority) as jobs:
            policy=jobs.snapshot()
            if not policy['enabled']:jobs.configure(enabled=True,expected_revision=policy['revision'])
            return jobs.request(request_id,prompt)


def next_actions(board,limit=3):
    validate_board(board)
    if type(limit) is not int or not 1<=limit<=10:raise ValueError('INVALID_LIMIT')
    indexed=[(i,c) for i,c in enumerate(board['cards']) if c['status']!='done']
    indexed.sort(key=lambda x:(x[1]['status']!='doing',PRIORITIES.index(x[1]['priority']),x[0]))
    return [{'card_id':c['id'],'action':('Continue: ' if c['status']=='doing' else 'Start: ')+c['title'],
             'priority':c['priority']} for _,c in indexed[:limit]]


def demo(database,authority):
    board=TaskBoard(database,authority=authority)
    initial={'schema':SCHEMA,'cards':[
        {'id':'draft','title':'Finish the project brief','details':'Include scope and the first milestone.','status':'doing','priority':'normal'},
        {'id':'review','title':'Review the dataset','details':'Check missing values and duplicates.','status':'todo','priority':'high'},
        {'id':'notes','title':'Collect reference notes','details':'','status':'done','priority':'normal'}]}
    board.save(initial,expected_revision=0)
    reopened=TaskBoard(database,authority=authority)
    assert reopened.snapshot()['board']==initial
    request=reopened.queue_plan('board-plan-example')
    result={'schema':'muse-board-result/v1','actions':next_actions(initial)}
    encoded=json.dumps(result,ensure_ascii=False,sort_keys=True)
    # This trusted in-process example binds a concrete result before accepting
    # its callback. A host adapter supplies its own authenticated verifier.
    expected_hash=hashlib.sha256(encoded.encode()).hexdigest()
    verifier=lambda event:hashlib.sha256(event['result'].encode()).hexdigest()==expected_hash
    with SpaceCompanion(database,authority=authority,callback_verifier=verifier) as jobs:
        claimed=jobs.claim(request['request_id'],expected_revision=request['revision'],operation_id='board-plan-operation')
        event={'request_id':request['request_id'],'operation_id':claimed['operation_id'],
               'request_sha256':claimed['request_sha256'],'event_id':'board-plan-result',
               'status':'SUCCEEDED','result':encoded}
        completed=jobs.callback(event)
        assert jobs.callback(event)['revision']==completed['revision']
    with SpaceCompanion(database,authority=authority) as jobs:
        assert json.loads(jobs.get(request['request_id'])['result'])==result
    return {'status':'PASS','cards_saved':len(initial['cards']),'reopened':True,
            'request_state':completed['state'],'actions':result['actions'],
            'export_bytes':len(reopened.export())}
