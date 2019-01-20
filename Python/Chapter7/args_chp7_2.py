# Args_chp7_2.py
def main():
    kitten()


def kitten(*args):
    if len(args):  # checking if the lenght is > 0
        for s in args:  # Then sequence get the items in the list and prints.
            print(s)
    else:
        print('MEOW')  # As the kitten is empty(kitten()) MEOW is printed


if __name__ == "__main__":
    main()
