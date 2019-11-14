from __future__ import absolute_import, division, print_function
from __future__ import unicode_literals

import getpass
import json

import requests

from bullet_journal import __host__, __prefix__, utils


def signup():
    username = input("Username: ")
    if not username:
        print("Username cannot be empty.")
    password = getpass.getpass("Password: ")
    if not password:
        print("Password cannot be empty.")

    response = requests.post(
        f'{__host__}/signup',
        data={
            'username': username,
            'hashed-password': utils.get_hash(password, random=False)
        },
        headers={
            'BJ_REQUEST_ORIGIN': 'bj.cli',
        },
    )
    if response.status_code == 200:
        print(f'Successfully signed up and logged in as {username}.')
    elif response.status_code == 400:
        print('Username unavailable.')
        exit(1)
    else:
        print("Something went wrong.")
        exit(1)

    utils.write_file(__prefix__, response.text, file_name='credentials')


def main(args):
    # Call the check function with the arguments from the command line
    return signup()
