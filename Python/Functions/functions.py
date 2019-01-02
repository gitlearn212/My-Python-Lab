# Learning Function to reduce code duplication for this
# we use the below code to produce a function.
# Define Function
# Functions.py
"""print("Hello, Mark")
print("We have 6 apples in the store")

print("Hello, Brook")
print("We have 6 apples in the store")

print("Hello, Greg")
print("We have 6 apples in the store")
"""


def greet_mark():
    print("Hello, Mark")
    print("We have 6 apples in the store")


def greet_brook():
    print("Hello, Brook")
    print("We have 6 apples in the store")


def greet_greg():
    print("Hello, Greg")
    print("We have 6 apples in the store")


greet_mark()
greet_brook()
greet_greg()
