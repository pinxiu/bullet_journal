from __future__ import absolute_import, division, print_function
from __future__ import unicode_literals

import base64
import datetime
import hashlib
import json
import os
import random
import re
import shutil
import string

from Crypto.Cipher import AES

import bullet_journal


def today():
    return get_date_string(datetime.date.today())


def tomorrow():
    return get_date_string(datetime.date.today() + datetime.timedelta(days=1))


def get_date_string(date_obj):
    return date_obj.strftime("%Y_%m_%d")


def is_valid_date(date_string):
    if not date_string:
        return False
    try:
        datetime.datetime.strptime(date_string, '%Y_%m_%d')
    except ValueError:
        print("Incorrect data format, should be yyyy_mm_dd")
        exit(1)
    return True


def ensure_directory(dir_name):
    if not os.path.exists(dir_name):
        os.makedirs(dir_name)


def write_file(directory, content, file_name=None):
    if not file_name:
        file_name = get_hash(content)
    with open(f'{directory}/{file_name}', 'w') as f:
        f.write(content)


def read_file(directory, file_name):
    with open(f'{directory}/{file_name}', 'r') as f:
        content = f.read()
    return content


def move_file(directory_src, directory_dst, file_name):
    src = f'{directory_src}/{file_name}'
    dst = f'{directory_dst}/{file_name}'
    os.rename(src, dst)


def remove_file(directory, file_name):
    os.remove(f'{directory}/{file_name}')


def random_string(string_length=32):
    """Generate a random string of fixed length """
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(string_length))


def get_hash(content, random=True):
    sha = hashlib.sha256()
    sha.update(content.encode())
    if random:
        sha.update(random_string().encode())
    return sha.hexdigest()[:32]


def loop_dir(directory):
    return [f for f in os.listdir(directory) if not f.startswith('.')]


def cleanup():
    shutil.rmtree(f'{bullet_journal.__prefix__}/resources')


def validate_auth():
    if not os.path.exists(f'{bullet_journal.__prefix__}/credentials'):
        print("User is not logged in.")
        exit(1)


def get_access_token():
    with open(f'{bullet_journal.__prefix__}/credentials') as f:
        credentials = json.loads(f.read())
    return credentials['access_token']

def get_user_id():
    with open(f'{bullet_journal.__prefix__}/credentials') as f:
        credentials = json.loads(f.read())
    return credentials['user_id']


def encrypt(msg_text):
    secret_key = get_hash(get_access_token(), random=False)
    cipher = AES.new(secret_key, AES.MODE_ECB)
    msg_text += ' ' * (16 - len(msg_text) % 16)
    return base64.b64encode(cipher.encrypt(msg_text.encode("utf-8"))).hex()


def decrypt(msg_text):
    secret_key = get_hash(get_access_token(), random=False)
    cipher = AES.new(secret_key, AES.MODE_ECB)
    return cipher.decrypt(base64.b64decode(bytes.fromhex(msg_text))).decode("utf-8").strip()
