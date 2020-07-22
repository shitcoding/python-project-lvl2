# -*- coding:utf-8 -*-

"""Gendiff script."""

import argparse
import os
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


# Parsing arguments from CLI.
parser = argparse.ArgumentParser(description='Generate diff')
parser.add_argument('first_file', type=str)
parser.add_argument('second_file', type=str)
parser.add_argument('-f', '--format', type=str, help='set format of output')
args = parser.parse_args()


# Handling absolute and relative paths.
if os.path.isabs(args.first_file):
    path_to_file1 = args.first_file
else:
    path_to_file1 = os.path.abspath(args.first_file)
if os.path.isabs(args.second_file):
    path_to_file2 = args.second_file
else:
    path_to_file2 = os.path.abspath(args.second_file)


def main():
    """Generate diff string between first_file and second_file."""
    diff = generate_diff(path_to_file1, path_to_file2)
    print(diff)


if __name__ == '__main__':
    main()

