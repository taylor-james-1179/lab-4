#! /usr/bin/env python3
"""A recursive Python program to check if a given number is palindrome."""


def _reverse_number(num):
    """
    Reverse a number.

    Return a new numeric value the digits of which are the same as number's
    but in reverse order.

    Parameters
    ----------
    number : int
        The number to be reveresed. number is expected to be a positive
        integer.

    Returns
    -------
    int
        A new value consisting of the digits of number in reversed order.

    """
    return int(
        str(num) if num < 10 else str(num % 10) + str(_reverse_number(num // 10))
    )


def is_palindrome(number):
    """
    Check if number is a palindrome.

    Parameters
    ----------
    arg1 : int
        The number to be tested. Number must be an integer.

    Returns
    -------
    bool
        True is number is a palindrome, otherwise False.

    """
    if not (isinstance(number, int)):
        raise ValueError
    return number == _reverse_number(number)
