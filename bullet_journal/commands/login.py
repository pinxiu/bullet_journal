from __future__ import absolute_import, division, print_function
from __future__ import unicode_literals

import os
import getpass
import json
import requests

from bullet_journal import __host__, __prefix__, utils


def login():
    if os.path.exists(f'{__prefix__}/credentials'):
        print('Already logged in.')
        exit(1)
    username = input("Username: ")
    password = getpass.getpass("Password: ")

    response = requests.post(
        f'{__host__}/login',
        data={
            'username': username,
            'hashed-password': utils.get_hash(password, random=False)
        },
        headers={
            'BJ_REQUEST_ORIGIN': 'bj.cli',
        },
    )
    if response.status_code == 200:
        print(f'Successfully logged in as {username}.')
    elif response.status_code == 401:
        print('Username or password does not match.')
        exit(1)
    else:
        print("Something went wrong.")
        exit(1)

    utils.write_file(__prefix__, response.text, file_name='credentials')


def main(args):
    # Call the check function with the arguments from the command line
    return login()
