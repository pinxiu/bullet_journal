from __future__ import absolute_import, division, print_function
from __future__ import unicode_literals

import argparse

from bullet_journal import __prefix__, utils


def migrate(date):
    utils.is_valid_date(date)
    directory_add = f'{__prefix__}/resources/{date}/add'
    directory_migrate = f'{__prefix__}/resources/{date}/migrate'
    utils.ensure_directory(directory_add)
    utils.ensure_directory(directory_migrate)
    records = list()
    print(f"Active items in {date}:")
    for f in utils.loop_dir(directory_add):
        records.append(f)
        print(f"Item {len(records)}: {utils.read_file(directory_add, f)}")
    if not records:
        print(f"There is no active item in {date}.")
        exit(0)
    choices = f"1-{len(records)}" if len(records) > 1 else "1"
    index = input(f"Index of item to migrate in {date} [{choices}]: ")
    try:
        i = int(index)
    except ValueError:
        #Handle the exception
        print("Please enter an integer")
        exit(1)
    file_name = records[i-1]
    utils.move_file(directory_add, directory_migrate, file_name)

    dst_date = input(f"Date to move item to [yyyy_mm_dd] (default {utils.tomorrow()}):")
    if not utils.is_valid_date(dst_date):
        dst_date = utils.tomorrow()
        print(f"Migrated item to default date: {dst_date}")
    directory_dst = f'{__prefix__}/resources/{dst_date}/add'
    utils.ensure_directory(directory_dst)
    utils.write_file(directory_dst, utils.read_file(directory_migrate, file_name))


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
