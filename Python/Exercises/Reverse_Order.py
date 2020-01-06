
# Reverse order


def reverse_v1(x):
    y = x.split()
    result = []
    for word in y:
        #word.split()
        result.insert(0, word)
    return " ".join(result)


a = 'My name is suhumar'

print(reverse_v1(a))
