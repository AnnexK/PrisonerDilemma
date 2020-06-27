from .args import parse_args
from .orgfile import parse_orgfile


def get_task():
    orgfname = parse_args()
    payload = parse_orgfile(orgfname)
    return payload
