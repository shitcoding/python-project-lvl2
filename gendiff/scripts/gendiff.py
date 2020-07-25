# -*- coding:utf-8 -*-

"""Gendiff script."""

import argparse
from gendiff.diff import generate_diff


# Parsing arguments from CLI.
parser = argparse.ArgumentParser(description='Generate diff')
parser.add_argument('first_file', type=str)
parser.add_argument('second_file', type=str)
parser.add_argument('-f', '--format',
                    type=str,
                    help='set format of output')
args = parser.parse_args()
path_to_file1 = args.first_file
path_to_file2 = args.second_file


def main():
    """
    Generate diff string between first_file and second_file.
    """
    diff_str = generate_diff(path_to_file1, path_to_file2)
    print(diff_str)


if __name__ == '__main__':
    main()
