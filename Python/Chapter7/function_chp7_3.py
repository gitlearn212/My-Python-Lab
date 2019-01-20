# Function Exercise 1
def main():
    kitten(5,)  # Notice it has 3 arguments


# Notice there is only 2 argments.
# This is a mistake  on execution stating an argument is missing.
# To overcome add an other argument in print a,b,c
def kitten(a, b, c):
    print('Cat : meow')
    print(a, b)


'''
def kitten(a, b=1, c=0):  # So as this line
    print('Cat : meow')
    print(a, b, c)
'''

if __name__ == "__main__":
    main()
