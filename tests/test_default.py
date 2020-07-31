# -*- coding:utf-8 -*-

"""Diff generation tests."""

from gendiff.diff import generate_diff
from gendiff.views import default_view


def test_default():
    with open('./tests/fixtures/1__expected_default.txt', 'r') as fixture:
        # rstrip() to get rid of \n in the end
        expected = fixture.read().rstrip()

        assert expected == generate_diff(
                './tests/fixtures/1__before.json',
                './tests/fixtures/1__after.json'
        )
        assert expected == generate_diff(
                './tests/fixtures/1__before.yaml',
                './tests/fixtures/1__after.yaml'
        )
        assert expected == generate_diff(
                './tests/fixtures/1__before.yaml',
                './tests/fixtures/1__after.json'
        )

        assert expected == generate_diff(
                './tests/fixtures/1__before.json',
                './tests/fixtures/1__after.yaml'
        )
