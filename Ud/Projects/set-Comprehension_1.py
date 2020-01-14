# Set Comprehensions
# set removes dulicate char(s) or num(s)
# set allow only unique numbers or chars
for cha in set('hello'):
    # my_list3.append(cha)
    print(cha, end='')


my_list1 = {char for char in 'hello'}
print(my_list1)

my_list2 = {num*2 for num in range(1, 10)}
print(my_list2)

my_list3 = {num**2 for num in range(1, 10) if num % 2 == 0}
print(my_list3)

my_list4 = {num**2 for num in range(1, 10) if num % 2 != 0}
print(my_list4)
