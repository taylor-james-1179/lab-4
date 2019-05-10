#! /usr/bin/env python3
import pytest

from part_2 import _is_consonant, count_consonants


def test_empty_input():
    with pytest.raises(ValueError):
        count_consonants("")


@pytest.mark.parametrize(
    "input, expected",
    [
        ("A", False),
        ("a", False),
        ("B", True),
        ("b", True),
        ("C", True),
        ("c", True),
        ("E", False),
        ("e", False),
        ("I", False),
        ("i", False),
        ("O", False),
        ("o", False),
        ("U", False),
        ("u", False),
        ("X", True),
        ("x", True),
        ("Y", True),
        ("y", True),
        ("Z", True),
        ("z", True),
    ],
)
def test_is_consonant(input, expected):
    assert _is_consonant(input) == expected


@pytest.mark.parametrize(
    "input, expected",
    [
        ("wall", 3),
        ("WALL", 3),
        ("wAlL", 3),
        ("WaLl", 3),
        ("Tis but a scratch.", 10),
        (
            """Don't say another word. Up
until now, I've been polite. If you say"
anything else - word one - I will kill"
myself. And when my tainted spirit"
finds its destination, I will topple the"
master of that dark place. From my black"
throne, I will lash together a Machine of"
bone and blood, and powered by my hatred"
for you this fear engine will bore a hole"
between this world and that one. "

When it begins, you will hear the"
sound of children screaming - as"
though from a great distance. A"
smoking orb of nothing will grow"
above your bed, and from it will"
emerge a thousand starving crows."
As I slip through the widening maw in"
my new form, you will catch only a"
glimpse of my radiance before you"
are incinerated. Then, as tears of"
bubbling pitch stream down my face,"
My dark work will begin."

I will open one of my six mouths, and "
I will sing the song that ends the"
Earth.""",
            428,
        ),
    ],
)
def test_count_consonants(input, expected):
    assert count_consonants(input) == expected
