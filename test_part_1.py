#! /usr/bin/env python3
import pytest

from part_1 import _reverse_number, is_palindrome


def test_empty_input():
    with pytest.raises(ValueError):
        is_palindrome("")


def test_is_integer_when_string():
    with pytest.raises(ValueError):
        is_palindrome("this is bad input")


def test_is_integer_when_float():
    with pytest.raises(ValueError):
        is_palindrome(121.21)


@pytest.mark.parametrize(
    "input, expected", [(1, 1), (12, 21), (1234, 4321), (12321, 12321)]
)
def test_reverse_number(input, expected):
    assert _reverse_number(input) == expected


@pytest.mark.parametrize(
    "input, expected",
    [
        (1, True),
        (-1, True),
        (12, False),
        (12345678987654321, True),
        (1234564321, False),
    ],
)
def test_many_digits(input, expected):
    assert is_palindrome(input) == expected
