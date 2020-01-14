# Lsit Comprehensions
# mutiply all numbers in to 2
my_list1 = [num for num in range(1, 10)]
print(my_list1)

my_list2 = [num * 2 for num in range(1, 10)]
print(my_list2)

# print all the even numbers from the given range
my_even_list = [num ** 2 for num in range(1, 10) if num % 2 == 0]
print(my_even_list)

# print all odd numbers from the given range
my_odd_list = [num1 ** 2 for num1 in range(0, 10) if num1 % 2 != 0]
print(my_odd_list)
