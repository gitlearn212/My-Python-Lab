# count the number of integer 4 in the list and output the total
def count_num_four(x):
    result = 0
    for i in (x):
        if i == 4:
            result += 1
    return result


a = (4, 5, 3, 4, 7, 88, 4, 4, 34, 4, 6)
print(count_num_four(a))
