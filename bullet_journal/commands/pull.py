from __future__ import absolute_import, division, print_function
from __future__ import unicode_literals

import argparse
import json
import requests

from bullet_journal import __host__, __prefix__, utils


def pull():
    utils.validate_auth()
    access_token = utils.get_access_token()
    user_id = utils.get_user_id()
    response = requests.get(
        f'{__host__}/{user_id}',
        headers={
            'BJ_REQUEST_ORIGIN': 'bj.cli',
            'BJ_SERVER_ACCESS_TOKEN': access_token,
        },
    )
    if response.status_code == 200:
        print("Successfully pulled bullet journal from remote server.")
    else:
        print("Something went wrong.")
    decrypted_text = utils.decrypt(json.dumps(response.text))
    print(decrypted_text)

    # root_directory = f'{__prefix__}/resources'
    # utils.ensure_directory(root_directory)
    # backup = dict()
    # for date in utils.loop_dir(root_directory):
    #     backup[date] = dict()
    #     for operation in utils.loop_dir(f'{root_directory}/{date}'):
    #         backup[date][operation] = dict()
    #         leaf_directory = f'{root_directory}/{date}/{operation}'
    #         for f in utils.loop_dir(leaf_directory):
    #             backup[date][operation][filename] = utils.read_file(leaf_directory, f)


def main(args):
    # Call the check function with the arguments from the command line
    return pull()
