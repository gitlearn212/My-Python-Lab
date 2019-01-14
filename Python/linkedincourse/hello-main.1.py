#! /usr/bin/env python3
''' This is function
It calls the print function the format and the python version ("This is python version {}".format(platform.python_version()))
from in side the message function and the message function is called from the main function.
Finally the main function is call (at the bottom line) with the conditional (if) statement.
'''
import platform


def main():
    message()


def message():
    print(" This is python version {}" .format(platform.python_version()))
    print("line 1")
    print("line 2")
    if False:           # Notice that with True all lines 1,2,3 are printed and with False only line 1 and 2 is printed
        print("line 3")
    else:
        print("Not TRUE it is FALSE")


if __name__ == "__main__":
    main()
