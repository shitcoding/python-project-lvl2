# -*- coding:utf-8 -*-

import json
import os


def generate_diff(path_to_file1, path_to_file2):
    """Generate diff logic."""
    # Handling absolute and relative paths.
    if not os.path.isabs(path_to_file1):
        path_to_file1 = os.path.abspath(path_to_file1)
    if not os.path.isabs(path_to_file2):
        path_to_file2 = os.path.abspath(path_to_file2)

    dict1 = json.load(open(path_to_file1))
    dict2 = json.load(open(path_to_file2))
    output = '{\n'
    for key, value in dict2.items():
        if key in dict1 and value == dict1[key]:
            output += f'  {key}: {value}\n'
        elif key in dict1 and value != dict1[key]:
            output += f'+ {key}: {value}\n'
            output += f'- {key}: {dict1[key]}\n'
        elif key not in dict1:
            output += f'+ {key}: {value}\n'
    for key, value in dict1.items():
        if key not in dict2:
            output += f'- {key}: {value}\n'
    output += '}'
    return output.lower()
