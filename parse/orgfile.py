import json


class TaskPayload:
    def __init__(self, mtx, ttype, pris, n):
        self.mtx = mtx
        self.ttype = ttype
        self.pris = pris
        self.n = n


def decode_payload(dct):
    if 'type' not in dct:
        dct['type'] = 'basic'

    return TaskPayload(tuple(dct[c] for c in ('cc', 'cd', 'dc', 'dd')),
                       dct['type'],
                       dct['contestants'],
                       dct['n'])


def parse_orgfile(orgfile):
    with open(orgfile, 'r') as f:
        payload = json.load(f, object_hook=decode_payload)
    return payload
