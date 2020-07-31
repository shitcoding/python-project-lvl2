# -*- coding:utf-8 -*-

import json
from gendiff.views import default_view


def file_to_dict(file_abspath):
    _dict = json.load(open(file_abspath))
    return _dict


def compare_dicts(dict1, dict2):
    """Return diff dictionary."""
    diff_dict = {}
    removed_keys = dict1.keys() - dict2.keys()
    added_keys = dict2.keys() - dict1.keys()
    common_keys = dict1.keys() & dict2.keys()
    for key in removed_keys:
        diff_dict[key] = ('removed', dict1[key])
    for key in added_keys:
        diff_dict[key] = ('added', dict2[key])
    for key in common_keys:
        if dict1[key] == dict2[key]:
            value_status = ('equal', dict1[key])
        else:
            value_status = ('changed', (dict1[key], dict2[key]))
        diff_dict[key] = value_status
    return diff_dict


def generate_diff(first_file, second_file):
    dict1 = file_to_dict(first_file)
    dict2 = file_to_dict(second_file)
    diff_dict = compare_dicts(dict1, dict2)
    diff_str = default_view.format(diff_dict)
    return diff_str
