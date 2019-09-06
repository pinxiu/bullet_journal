from __future__ import absolute_import, division, print_function
from __future__ import unicode_literals

import argparse

from bullet_journal import utils


def daily_log(date):
    print(f"Showing daily log of {date}")


def main(args):
    parser = argparse.ArgumentParser(prog="bj daily_log")
    parser.add_argument(
        "date",
        nargs="?",
        default=utils.today(),
        metavar="date",
        help="The date to query",
    )

    args = parser.parse_args(args)

    # Call the check function with the arguments from the command line
    return daily_log(args.date)
