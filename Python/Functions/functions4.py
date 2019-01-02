# Functions4.py
# Setting default value for the argument (num_apples = 10) and
# # remove the numbers from the calling function


def greet_customer(name, num_apples=10):

    print("Hello, " + name)
    print("We have " + str(num_apples) + " apples in the store")


greet_customer("Mark")
greet_customer("Brook")
greet_customer("Greg")
