from __future__ import absolute_import, division, print_function
from __future__ import unicode_literals

import os
import getpass
import json

import requests

from bullet_journal import __host__, __prefix__, utils


def logout():
    utils.validate_auth()
    utils.remove_file(__prefix__, 'credentials')


def main(args):
    # Call the check function with the arguments from the command line
    return logout()
