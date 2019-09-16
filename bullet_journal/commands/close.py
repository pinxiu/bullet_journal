from __future__ import absolute_import, division, print_function
from __future__ import unicode_literals

import argparse

from bullet_journal import __prefix__, utils


def close(date):
    utils.is_valid_date(date)
    directory_add = f'{__prefix__}/resources/{date}/add'
    directory_close = f'{__prefix__}/resources/{date}/close'
    utils.ensure_directory(directory_add)
    utils.ensure_directory(directory_close)
    records = list()
    print(f"Active items in {date}:")
    for f in utils.loop_dir(directory_add):
        records.append(f)
        print(f"Item {len(records)}: {utils.read_file(directory_add, f)}")
    if not records:
        print(f"There is no active item in {date}.")
        exit(0)
    choices = f"1-{len(records)}" if len(records) > 1 else "1"
    index = input(f"Index of item to close in {date} [{choices}]: ")
    try:
        i = int(index)
    except ValueError:
        #Handle the exception
        print("Please enter an integer")
        exit(1)
    file_name = records[i-1]
    utils.move_file(directory_add, directory_close, file_name)


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
