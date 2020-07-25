# -*- coding:utf-8 -*-

import json


def generate_diff(path_to_file1, path_to_file2):
    """Generate diff logic."""
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
