# Comprehensions exercise

# Normal way
'''
some_list = ['a', 'b', 'c', 'b', 'd', 'm', 'n', 'n']
duplicate = []
for value in some_list:
    if some_list.count(value) > 1:
        if value not in duplicate:
            duplicate.append(value)
print(duplicate)
'''

# OR Normal way using SET
'''
some_list = ['a', 'b', 'c', 'b', 'd', 'm', 'n', 'n']
duplicate = []
for value in some_list:
    if some_list.count(value) > 1:
        duplicate.append(value)
print(set(sorted(duplicate)))
'''
# comprehension way
some_list = ['a', 'b', 'c', 'b', 'd', 'm', 'n', 'n']
duplicate = list(set([x for x in some_list if some_list.count(x) > 1]))

#print(duplicate)
print(sorted(duplicate))
