# -*- coding:utf-8 -*-

"""Gendiff script."""

import argparse


parser = argparse.ArgumentParser(description='Generate diff')
parser.add_argument('first_file', type=str)
parser.add_argument('second_file', type=str)
parser.add_argument('-f', '--format', type=str, help='set format of output')

def main():
    """Run gendiff script."""
    args = parser.parse_args()


if __name__ == '__main__':
    main()

