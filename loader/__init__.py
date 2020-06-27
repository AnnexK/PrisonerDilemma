from .loader import load_prisoner, load_pitter
from numpy import array


def load_task(payload):
    pit = load_pitter(payload)
    P = array([load_prisoner(fn) for fn in payload.pris])
    return pit, P
