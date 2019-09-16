from __future__ import absolute_import, division, print_function
from __future__ import unicode_literals

import argparse

from bullet_journal import __prefix__, utils


def add(date):
    utils.is_valid_date(date)
    directory = f'{__prefix__}/resources/{date}/add'
    utils.ensure_directory(directory)
    content = input(f"Add item to {date}: ")
    utils.write_file(directory, content)


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
