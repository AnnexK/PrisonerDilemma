import argparse


def parse_args():
    p = argparse.ArgumentParser()
    p.add_argument('orgfile', help='organizer file containing tournament type (basic if unspecified) and participants\' filenames')
    return p.parse_args().orgfile
