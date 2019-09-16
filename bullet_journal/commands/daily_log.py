from __future__ import absolute_import, division, print_function
from __future__ import unicode_literals

import argparse

from bullet_journal import __prefix__, utils


def daily_log(date):
    utils.is_valid_date(date)
    directory_add = f'{__prefix__}/resources/{date}/add'
    directory_close = f'{__prefix__}/resources/{date}/close'
    directory_migrate = f'{__prefix__}/resources/{date}/migrate'
    utils.ensure_directory(directory_add)
    utils.ensure_directory(directory_close)
    utils.ensure_directory(directory_migrate)
    for f in utils.loop_dir(directory_add):
        print(f"+ {utils.read_file(directory_add, f)}")
    for f in utils.loop_dir(directory_close):
        print(f"x {utils.read_file(directory_close, f)}")
    for f in utils.loop_dir(directory_migrate):
        print(f"> {utils.read_file(directory_migrate, f)}")


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
