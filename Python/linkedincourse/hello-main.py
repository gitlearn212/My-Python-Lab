#! /usr/bin/env python3
''' This is function
It calls the print function the format and the python version ("This is python version {}".format(platform.python_version()))
from in side the message function and the message function is called from the main function.
Finally the main function is call (at the bottom line) with the conditional (if) statement.
'''
import platform


def main():
    message()
    second_message()


def message():
    print("This is python version {}" .format(platform.python_version()))


def second_message():
    print("This is my second line")


if __name__ == "__main__":
    main()
