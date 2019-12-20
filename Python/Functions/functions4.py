# Functions4.py
# Setting default value for the argument (num_apples = 10) and
# # remove the numbers from the calling function


# def greet_customer(name, num_apples=10):
def greet_customer(name, num_apples):

    print("At" + name)
    print("We have " + str(num_apples) + " apples in the store")


greet_customer(" EAST HAM ", 9)
greet_customer(" SCOTLAND ", 7)
greet_customer(" IRELAND ", 5)
