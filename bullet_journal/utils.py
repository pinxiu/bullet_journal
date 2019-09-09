from __future__ import absolute_import, division, print_function
from __future__ import unicode_literals

import datetime
import hashlib
import os
import random
import re
import string


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


def write_file(directory, content):
    with open(f'{directory}/{get_hash(content)}', 'w') as f:
        f.write(content)


def read_file(directory, file_name):
    with open(f'{directory}/{file_name}', 'r') as f:
        content = f.read()
    return content


def move_file(directory_src, directory_dst, file_name):
    src = f'{directory_src}/{file_name}'
    dst = f'{directory_dst}/{file_name}'
    os.rename(src, dst) 


def random_string(string_length=32):
    """Generate a random string of fixed length """
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(string_length))


def get_hash(content):
    sha = hashlib.sha256()
    sha.update(content.encode())
    sha.update(random_string().encode())
    return sha.hexdigest()[:32]


def loop_dir(directory):
    return [f for f in os.listdir(directory) if not f.startswith('.')]
