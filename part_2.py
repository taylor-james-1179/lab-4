#! /usr/bin/env python3
"""A recursive Python program to count consonants in a string."""


def _is_consonant(char):
    """
    Test whether a character is an English consonant.

    Parameters
    ----------
    character : str
        The character being tested.

    Returns
    -------
    bool
        True if char is a consonant in the English alphabet, otherwise False.

    """
    return not (char.upper() in ["A", "E", "I", "O", "U"]) and char.isalpha()


def count_consonants(text):
    """
    Count the English consonants in a string.

    Consonants are any English letter other than "a", ",," "i", "o", or "u"
    irrespective of case. Every instance of a constant is counted. For example,
    the word "bull" has three consonants in it.

    Parameters:
    -----------
    text : str
        The string in which consonants are to be counted.

    Returns
    -------
    int
        The total number of consonants found in text.

    """
    if text == "":
        raise ValueError
    return (1 if _is_consonant(text[0]) else 0) + (
        0 if text[1:] == "" else count_consonants(text[1:])
    )
