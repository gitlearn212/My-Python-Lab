# Given the below class:
class Cat:
    species = 'mammal'

    def __init__(self, name, age):

        self.name = name
        self.age = age


# 1 Instantiate the Cat object with 3 cats
tom = Cat("Tom", 5)
silvia = Cat("silvia", 1)
kris = Cat("kris", 4)

# 2 Create a function that finds the oldest cat


def get_oldest_cat(*args):
    return max(args)


def get_youngest_cat(*args):
    return min(args)


# 3 Print out: "The oldest cat is x years old.". x will be the oldest cat age by using the function in #2
print(
    f"\nThe oldest cat is {get_oldest_cat(tom.name, silvia.name, kris.name)} and it is {get_oldest_cat(tom.age, silvia.age, kris.age)} years old.")

# 4 Print out: "The youngest cat is x years old.". x will be the youngest cat age by using the function in #3
print(
    f"\nThe youngest cat is {get_youngest_cat(tom.name, silvia.name, kris.name)} and it is {get_youngest_cat(tom.age, silvia.age, kris.age)} years old.")
