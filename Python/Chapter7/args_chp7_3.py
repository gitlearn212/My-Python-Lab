# args_chp7_3.py
def main():
    x = ('meow', 'grrr', 'purr', 'hello', 'world',
         'else')  # assigning (tuple) to x
    kitten(*x)


def kitten(*args):
    if len(args):  # checking if the lenght is > 0
        for s in args:  # Then sequence get the items in the list and print.
            print(s, end=' ', flush=True)
            # print(s)

    else:
        print('MEOW')  # thisis printed when the kitten is empty(kitten())


if __name__ == "__main__":
    main()
