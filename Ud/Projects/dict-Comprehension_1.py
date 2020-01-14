# Set Comprehensions
# ditionary

simple1_dict = {
    'a': 1,
    'b': 2
}

for k, v in simple1_dict.items():

    if v % 2 == 0:
        print({k: v})
# OR

simple_dict = {
    'a': 1,
    'b': 2
}
my_dict = {k: v ** 2 for k, v in simple_dict.items() if v % 2 == 0}
print(my_dict)

# OR
my_dict = {num: num*2 for num in [1, 2, 3]}
print(my_dict)
for num in [1, 2, 3]:
    print({num: num*2})
