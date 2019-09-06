from __future__ import absolute_import, division, print_function
from __future__ import unicode_literals

import argparse

from bullet_journal import utils


def add(date):
    print(f"Adding to {date}")


def main(args):
    parser = argparse.ArgumentParser(prog="bj add")
    parser.add_argument(
        "date",
        nargs="?",
        default=utils.today(),
        metavar="date",
        help="The date to add item to",
    )

    args = parser.parse_args(args)

    # Call the check function with the arguments from the command line
    return add(args.date)
