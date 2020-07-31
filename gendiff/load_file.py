# -*- coding:utf-8 -*-

import os
import sys
import json
import yaml


def get_abspath(path_to_file):
    """Return absolute path to file."""
    if not os.path.isabs(path_to_file):
        path_to_file = os.path.abspath(path_to_file)
    return path_to_file


def file_to_dict(file_abspath):
    extension = file_abspath.split('.')[-1]
    if extension == 'json':
        _dict = json.load(open(file_abspath))
    elif extension == 'yaml' or extension == 'yml':
        _dict = yaml.safe_load(open(file_abspath))
    else:
        sys.exit('Unsupported file type: Use .json, .yaml, .yml files')
    return _dict
