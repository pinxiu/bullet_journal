from __future__ import absolute_import, division, print_function
from __future__ import unicode_literals

import argparse

from bullet_journal import utils


def close(date):
    print(f"Closing in {date}")


def main(args):
    parser = argparse.ArgumentParser(prog="bj close")
    parser.add_argument(
        "date",
        nargs="?",
        default=utils.today(),
        metavar="date",
        help="The date to close item in",
    )

    args = parser.parse_args(args)

    # Call the check function with the arguments from the command line
    return close(args.date)
