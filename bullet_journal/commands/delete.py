from __future__ import absolute_import, division, print_function
from __future__ import unicode_literals

import argparse

from bullet_journal import __prefix__, utils


def delete(date):
    utils.is_valid_date(date)
    directory_add = f'{__prefix__}/resources/{date}/add'
    utils.ensure_directory(directory_add)
    records = list()
    print(f"Active items in {date}:")
    for f in utils.loop_dir(directory_add):
        records.append(f)
        print(f"Item {len(records)}: {utils.read_file(directory_add, f)}")
    if not records:
        print(f"There is no active item in {date}.")
        exit(0)
    choices = f"1-{len(records)}" if len(records) > 1 else "1"
    index = input(f"Index of item to delete in {date} [{choices}]: ")
    try:
        i = int(index)
    except ValueError:
        #Handle the exception
        print("Please enter an integer")
        exit(1)
    file_name = records[i-1]
    utils.remove_file(directory_add, file_name)


def main(args):
    parser = argparse.ArgumentParser(prog="bj close")
    parser.add_argument(
        "date",
        nargs="?",
        default=utils.today(),
        metavar="date",
        help="The date to delete item from",
    )

    args = parser.parse_args(args)

    # Call the check function with the arguments from the command line
    return delete(args.date)
