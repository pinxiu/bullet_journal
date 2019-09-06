from __future__ import absolute_import, division, print_function
from __future__ import unicode_literals

import argparse

from bullet_journal import utils


def migrate(date):
    print(f"Migrating {date}")


def main(args):
    parser = argparse.ArgumentParser(prog="bj migrate")
    parser.add_argument(
        "date",
        nargs="?",
        default=utils.today(),
        metavar="date",
        help="The date to migrate item from",
    )

    args = parser.parse_args(args)

    # Call the check function with the arguments from the command line
    return migrate(args.date)
