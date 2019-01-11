# Functions5.py
#


def hello_func(greeting, name="h"):
    return '{}, {}'.format(greeting, name)


print(hello_func("Hello", name="Johny 5"))
print(hello_func("Hello", name="Johny 5").upper())
print(len(hello_func("Hello ", name="Johny 5")))
