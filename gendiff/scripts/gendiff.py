# -*- coding:utf-8 -*-

"""Gendiff script."""

import os
import argparse
from gendiff.diff import generate_diff


# Parsing arguments from CLI.
parser = argparse.ArgumentParser(description='Generate diff')
parser.add_argument('first_file', type=str)
parser.add_argument('second_file', type=str)
parser.add_argument('-f', '--format',
                    type=str,
                    default='plain',
                    help='set format of output')


def get_abspath(path_to_file):
    """Return absolute path to file."""
    if not os.path.isabs(path_to_file):
        path_to_file = os.path.abspath(path_to_file)
    return path_to_file


def main():
    """
    Print `diff_str`:
    String with changes between first_file and second_file.
    """
    args = parser.parse_args()
    # Handling absolute and relative paths.
    path_to_file1 = get_abspath(args.first_file)
    path_to_file2 = get_abspath(args.second_file)
    diff_str = generate_diff(path_to_file1, path_to_file2)
    print(diff_str)


if __name__ == '__main__':
    main()
