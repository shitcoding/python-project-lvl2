def make_item_string(prefix, key, value):
    return '  {0} {1}: {2}'.format(prefix, key, value)


def make_items_strings(diff_dict):
    strings = []
    for key, (status, value) in sorted(diff_dict.items()):
        if status == 'equal':
            strings.append(make_item_string(' ', key, value))
        elif status == 'added':
            strings.append(make_item_string('+', key, value))
        elif status == 'removed':
            strings.append(make_item_string('-', key, value))
        elif status == 'changed':
            old, new = value
            strings.append(make_item_string('+', key, new))
            strings.append(make_item_string('-', key, old))
    return '\n'.join(strings)


def format(diff_dict):
    return '{\n' + make_items_strings(diff_dict) + '\n}'
