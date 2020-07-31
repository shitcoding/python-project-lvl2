# -*- coding:utf-8 -*-

from gendiff.views import default_view
from gendiff.load_file import file_to_dict


def compare_dicts(dict1, dict2):
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


def generate_diff(path_to_file1, path_to_file2):
    dict1 = file_to_dict(path_to_file1)
    dict2 = file_to_dict(path_to_file2)
    diff_dict = compare_dicts(dict1, dict2)
    diff_str = default_view.format(diff_dict)
    return diff_str
