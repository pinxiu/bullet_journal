#!/usr/bin/env python
from __future__ import absolute_import, division, print_function
from __future__ import unicode_literals


import argparse
import pkg_resources
import sys

import bullet_journal
from bullet_journal import exceptions

def _registered_commands(group='bullet_journal.registered_commands'):
    registered_commands = pkg_resources.iter_entry_points(group=group)
    return {c.name: c for c in registered_commands}


def dispatch(argv):
    registered_commands = _registered_commands()
    parser = argparse.ArgumentParser(prog="bj")
    parser.add_argument(
        "--version",
        action="version",
        version="%(prog)s version {}".format(
            bullet_journal.__version__,
        ),
    )
    parser.add_argument(
        "command",
        choices=registered_commands.keys(),
    )
    parser.add_argument(
        "args",
        help=argparse.SUPPRESS,
        nargs=argparse.REMAINDER,
    )

    args = parser.parse_args(argv)

    main = registered_commands[args.command].load()

    return main(args.args)


def main():
    if len(sys.argv) == 1:
        return 'Welcome to Bullet Journal Toolkit Version 0.1!'
    try:
        return dispatch(sys.argv[1:])
    except exceptions.BulletJournalException as exc:
        return '{}: {}'.format(exc.__class__.__name__, exc.args[0])


if __name__ == "__main__":
    sys.exit(main())
