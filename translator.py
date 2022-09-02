#!/usr/bin/env python3
"""Translates any text document into an .fb file

First CLI argument should be a text file to be converted.
Print to `.fb` file extension with ` > output_file.fb`

Example:

./translator.py original_text_file.txt > new_fb_file.fb

Check translation with ./code_runner.py new_fb_file.fb"""

import sys
from io import StringIO


def ascii_code_to_finary(char: str) -> str:
    """Converts a single ascii character to FizzBuzzLang readable finary

    >>> ascii_code_to_finary(101) # "e"
    'BUZZ BUZZ FIZZ FIZZ BUZZ FIZZ BUZZ'
    >>> ascii_code_to_finary(63) # "?"
    'FIZZ BUZZ BUZZ BUZZ BUZZ BUZZ BUZZ'
    >>> ascii_code_to_finary(48) # "0"
    'FIZZ BUZZ BUZZ FIZZ FIZZ FIZZ FIZZ'
    """
    binary = f'{char:07b}'
    return " ".join("FIZZ" if char == "0" else "BUZZ" for char in binary)


FINARY = {chr(i): ascii_code_to_finary(i) for i in range(128)}


class Translator:
    """Translates file to FizzBuzzLang string"""

    # allows storing of character at data-space location
    __STORE_CHAR: str = "BUZZ FIZZBUZZ FIZZBUZZ "
    # move pointer forward one space in data-space
    __MOVE_FORWARD: str = "FIZZ FIZZ FIZZ"
    # stores current data-space location in FIZZ loc
    __STORE_POS_FIZZ: str = "FIZZ FIZZBUZZ FIZZ"
    # prints data in FizzBuzzLang
    __END_OF_CODE: str = """BUZZ FIZZBUZZ FIZZBUZZ BUZZ FIZZ BUZZ FIZZ
FIZZ FIZZBUZZ FIZZBUZZ FIZZ
FIZZBUZZ FIZZ FIZZBUZZBUZZ
BUZZ BUZZ
FIZZ FIZZ FIZZ
FIZZBUZZ BUZZ FIZZ FIZZBUZZBUZZ"""
    # termination command to end fbi.py
    __TERMINATE_COMMAND: str = "FIZZBUZZ FIZZBUZZ"

    def __init__(self, source: str) -> None:
        # text content of file passed in CLI
        self.__SOURCE = source

    def __str__(self):
        """Outputs a runnable FBL script"""

        fbl_doc = StringIO()
        print(self.__STORE_POS_FIZZ, file=fbl_doc)
        for char in self.__SOURCE:
            print(self.__STORE_CHAR + FINARY[char], file=fbl_doc)
            print(self.__MOVE_FORWARD, file=fbl_doc)
        print(self.__END_OF_CODE, file=fbl_doc)
        print(self.__TERMINATE_COMMAND, file=fbl_doc)

        return fbl_doc.getvalue()


def retrieve_file() -> str:
    """Retrieves text from file

    Accepts CLI argument

    ---
    raises:
        IndexError: -- if no file name provided
        FileNotFoundError: -- if file is not found

        # TODO - remove exit()
        All errors will terminate program
    """

    try:
        file_name = sys.argv[1]
    except IndexError:
        print("Error, no file argument given when running file.")
        # TODO - remove exit() and ' raise a custom exception and let the caller figure it out '
        print("Program will terminate.")
        exit()

    try:
        with open(file_name, "r") as f:
            file_contents = f.read()
    except FileNotFoundError as e:
        print(f"{e}")
        # TODO - remove exit() and ' raise a custom exception and let the caller figure it out '
        print("Program will terminate.")
        exit()
    return file_contents


if __name__ == "__main__":
    # import doctest
    # doctest.testmod()
    print(Translator(retrieve_file()))
