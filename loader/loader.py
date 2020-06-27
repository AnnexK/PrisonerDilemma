import importlib
import pitter


def load_prisoner(fname):
    pkg = 'prisoners'
    mod = importlib.import_module('.'+fname, pkg)
    return mod.Prisoner()


def load_pitter(payload):
    pdct = {'basic': pitter.BasicPitter}

    return pdct[payload.ttype](pitter.PaymentMatrix(*payload.mtx),
                               payload.n)
