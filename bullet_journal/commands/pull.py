from __future__ import absolute_import, division, print_function
from __future__ import unicode_literals

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
    backup = json.loads(utils.decrypt(response.text))
    utils.cleanup()
    root_directory = f'{__prefix__}/resources'
    utils.ensure_directory(root_directory)
    for date in backup:
        utils.ensure_directory(f'{root_directory}/{date}')
        for operation in backup[date]:
            leaf_directory = f'{root_directory}/{date}/{operation}'
            utils.ensure_directory(leaf_directory)
            for f in backup[date][operation]:
                utils.write_file(leaf_directory, backup[date][operation][filename], file_name=f)


def main(args):
    # Call the check function with the arguments from the command line
    return pull()
