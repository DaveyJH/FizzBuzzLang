#!/usr/bin/env python
"Translates any text document into an .fb file"

import sys
from fizz_buzz_dict import LOOK_UP


class Translator():
    """Prepares common FizzBuzzLang functions and retrieves file text content

    ---
    Attributes:
        INPUT: str -- text content of file passed in CLI
        STORE_CHAR: str -- allows storing of character at data-space location
        MOVE_FORWARD: str -- move pointer forward one space in data-space
        STORE_POS_FIZZ: str -- stores current data-space location in FIZZ loc.
        END_OF_CODE: str -- prints data
        TERMINATE_COMMAND: str -- termination command to end fbi
        FBL_TEXT_ARRAY: list -- INPUT written in finary
    """

    def __init__(self) -> None:
        self.INPUT = self._retrieve_file()
        self.STORE_CHAR = "BUZZ FIZZBUZZ FIZZBUZZ "
        self.MOVE_FORWARD = "FIZZ FIZZ FIZZ"
        self.STORE_POS_FIZZ = "FIZZ FIZZBUZZ FIZZ"
        self.END_OF_CODE = """BUZZ FIZZBUZZ FIZZBUZZ BUZZ FIZZ BUZZ FIZZ
FIZZ FIZZBUZZ FIZZBUZZ FIZZ
FIZZBUZZ FIZZ FIZZBUZZBUZZ
BUZZ BUZZ
FIZZ FIZZ FIZZ
FIZZBUZZ BUZZ FIZZ FIZZBUZZBUZZ"""
        self.TERMINATE_COMMAND = "FIZZBUZZ FIZZBUZZ"
        self.FBL_TEXT_ARRAY = self._convert_to_fbl()

    def _retrieve_file(self):
        """Retrieves text from file

        Accepts CLI argument

        ---
        returns:
            str: -- document contents as string

        raises:
            IndexError: -- if no file name provided
            FileNotFoundError: -- if file is not found

            All errors will terminate program
        """

        try:
            file_name = sys.argv[1]
        except IndexError:
            print("Error, no file argument given when running file.")
            print("Program will terminate.")
            exit()

        while True:
            try:
                with open(file_name, "r") as f:
                    INPUT = f.read()
                    break
            except FileNotFoundError as e:
                print(f"{e}")
                print("Program will terminate.")
                exit()
        return INPUT

    def _convert_to_fbl(self):
        """Creates a list of FBL characters

        ---
        returns:
            list: -- list of FBL converted ASCII characters
        """

        fbl_text = []
        for char in self.INPUT:
            # add check/create new function using binary lookup
            char_finary = LOOK_UP[char]
            fbl_text.append(self.STORE_CHAR + char_finary)

        return fbl_text

    def print_fbl_doc(self):
        """Prints a runnable FBL script"""

        print(self.STORE_POS_FIZZ)
        for char in self.FBL_TEXT_ARRAY:
            print(char)
            print(self.MOVE_FORWARD)
        print(self.END_OF_CODE)
        print(self.TERMINATE_COMMAND)


if __name__ == "__main__":
    FBL = Translator()
    FBL.print_fbl_doc()
