def main():
    kitten('meow', 'grrr', 'purr')


def kitten(*args):
    if len(args):  # checking if the lenght is > 0
        for s in args:  # Then sequence get the items in the list and print.
            print(s)
    else:
        print('MEOW')  # thisis printed when the kitten is empty(kitten())


if __name__ == "__main__":
    main()
