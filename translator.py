#!/usr/bin/env python3
"""Translates any text document into an .fb file

First CLI argument should be a text file to be converted.
Print to `.fb` file extension with ` > output_file.fb`

Example:

./translator.py original_text_file.txt > new_fb_file.fb

Check translation with ./code_runner.py new_fb_file.fb"""

import sys


class Translator():
    """Translates file to FizzBuzzLang string"""

    def __init__(self, input):
        # self-populating dictionary of finary refs
        self.__look_up = {}
        # text content of file passed in CLI
        self.__INPUT = input
        # allows storing of character at data-space location
        self.__STORE_CHAR = "BUZZ FIZZBUZZ FIZZBUZZ "
        # move pointer forward one space in data-space
        self.__MOVE_FORWARD = "FIZZ FIZZ FIZZ"
        # stores current data-space location in FIZZ loc
        self.__STORE_POS_FIZZ = "FIZZ FIZZBUZZ FIZZ"
        # prints data in FizzBuzzLang
        self.__END_OF_CODE = """BUZZ FIZZBUZZ FIZZBUZZ BUZZ FIZZ BUZZ FIZZ
FIZZ FIZZBUZZ FIZZBUZZ FIZZ
FIZZBUZZ FIZZ FIZZBUZZBUZZ
BUZZ BUZZ
FIZZ FIZZ FIZZ
FIZZBUZZ BUZZ FIZZ FIZZBUZZBUZZ"""
        # termination command to end fbi.py
        self.__TERMINATE_COMMAND = "FIZZBUZZ FIZZBUZZ"
        # self.__INPUT written in finary
        self.__FBL_TEXT_LIST = self._convert_to_fbl()

    # TODO - transfer to helper function
    def _convert_to_fbl(self):
        """Creates a list of FBL characters

        ---
        returns:
        # TODO - create custom type
            list: -- list of FBL converted ASCII characters
        """

        fbl_text = []
        for char in self.__INPUT:
            char_finary = self.__look_up.setdefault(char, " ".join(
                ["FIZZ" if char == "0" else "BUZZ" for char in bin(
                    ord(char))[2:]]))
            fbl_text.append(self.__STORE_CHAR + char_finary)

        return fbl_text

    def print_fbl_doc(self):
        """Prints a runnable FBL script"""

        print(self.__STORE_POS_FIZZ)
        for char in self.__FBL_TEXT_LIST:
            print(char)
            print(self.__MOVE_FORWARD)
        print(self.__END_OF_CODE)
        print(self.__TERMINATE_COMMAND)


def retrieve_file():
    """Retrieves text from file

    Accepts CLI argument

    ---
    returns:
        str: -- document contents as string

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
    FBL = Translator(retrieve_file())
    # TODO - change to __str__ method
    FBL.print_fbl_doc()
