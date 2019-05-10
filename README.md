# CS162 Lab 4

## Introduction

The following lab exercises are intended to give you more experience writing recursive code. Before starting writing your solution think the problem through. Identify the base case(s) as well as the recursive case(s). Yes, there may be more than one of either. When should your recursion end? Under what circumstances should your function call itself recursively?

For each part of the lab you will want to break down the overall problem into smaller pieces, each of which can be solved functions that do exactly one task. Don't be afraid to write small helper functions as necessary. In some cases, this has been scaffolded for you. For example, in Part 1 of the lab you will see that there are function headers and tests for a function named `is_palindrome` as well as one named `_reverse_number`. The latter is a helper function that is meant to perform one specific task: take a positive integer and return a new integer consisting of the digits in the original number but in reverse order. You are _not_ limited to these helper functions, however. Where you think it necessary feel free to write your own helpers. When you do, write at least one test for them to ensure their correct function.

Also in this lab you will begin doing some basic work with Python exceptions, namely raising them if something, well, _exceptional_ happens. You can read Real Python's [Python Exceptions: An Introduction](https://realpython.com/python-exceptions/#raising-an-exception) or watch SelfTuts' [Raising exception in Python](https://www.youtube.com/watch?v=x_ZnVVIWH_s) video. The tests will guide you as to exactly what exception(s) are expected to be raised and under what circumstances.

## Directions

1. Clone this repository to your development computer.

1. (optional) Open the file `.travis.yml` and enter your email address in place of "`user@example.com`". This will ensure that you are notified about the success or failure of the automated tests that are run against your code.

   ```yaml
   notifications:
     email:
       recipients:
         - user@example.com
       on_success: always
       on_failure: always
   ```

1. Don't forget that docstrings are a requirement for your code. Example module and function docstrings are provided below.

   ```python
   """
   Brief assignment description.

   Longer, more detailed explanation of your solution. This may be anywhere from
   a couple of sentences to several paragraphs depending on how complex the
   assignment is. It should be detailed enough that someone who has never seen the
   code can understand what it does just by reading this explanation. You may
   also want to include examples of using the program if it accepts command line
   arguments.

   Your name
   Your partner's/collaborator's name
   """
   ```

   ```python
    def random_number_generator(arg1, arg2):
    """
    Summary line.

    Extended description of function.

    Parameters
    ----------
    arg1 : int
        Description of arg1.
    arg2 : str
        Description of arg2.

    Returns
    -------
    int
        Description of return value. This may be omitted if the function does not explicitly return a value.

    """
   ```

## Exercises

### Part 1

Given an integer, write a recursive function that returns `True` if the given number is palindrome, else `False`. For example, 12321 is palindrome, but 1451 is not palindrome.

**Hint:** You will want to verify good input _before_ doing any with with the argument passed in.

### Part 2

Given a string, count total number of consonants in it.

#### Examples

```Text
Input : abc de
Output : 3
There are three consonants b, c and d.

Input : CS162 is more fun that any other class
Output : 19
```

### Part 3

Using the "animated" in-class demo code as a starting point, write a version of the Towers of Hanoi using 5 rods and a number of disks between 1 and 12.

**Note:** You are _not_ required to use any third-party modules such as `cutie` or `inflect`. However, if you choose to do so you will need to add them to the install section of the `.travis.yml` file. An example of installing `cutie` is shown below.

```yml
install:
  - "pip install pytest pylint pycodestyle pydocstyle cutie"
```

Due 11:59:59PM, May 16.
