from __future__ import absolute_import, division, print_function
from __future__ import unicode_literals

import json
import requests

from bullet_journal import __host__, __prefix__, utils


def push():
    utils.validate_auth()
    access_token = utils.get_access_token()
    user_id = utils.get_user_id()
    root_directory = f'{__prefix__}/resources'
    utils.ensure_directory(root_directory)
    backup = dict()
    for date in utils.loop_dir(root_directory):
        backup[date] = dict()
        for operation in utils.loop_dir(f'{root_directory}/{date}'):
            backup[date][operation] = dict()
            leaf_directory = f'{root_directory}/{date}/{operation}'
            for f in utils.loop_dir(leaf_directory):
                backup[date][operation][f] = utils.read_file(leaf_directory, f)
    encrypted_text = utils.encrypt(json.dumps(backup))
    response = requests.put(
        f'{__host__}/{user_id}',
        headers={
            'BJ_REQUEST_ORIGIN': 'bj.cli',
            'BJ_SERVER_ACCESS_TOKEN': access_token,
        },
        data=encrypted_text,
    )
    if response.status_code == 204:
        print("Successfully pushed bullet journal to remote server.")
    else:
        print("Something went wrong.")


def main(args):
    # Call the check function with the arguments from the command line
    return push()
