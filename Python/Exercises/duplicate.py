# Write a function that list's all the none duplicate members
# (list the members minus the deplicates).
# This is the normal way


def dedupe_v1(x):
    y = []

    for i in x:
        if i not in y:
            y.append(i)
    return y

# This is usig the (set) method


def dedupe_v2(x):
    return list(set(x))


a = ['peter', 'peter', 'roy', 'mohan', 'ram', 'ram', 'mohan']
b = ['jay', 'kav', 'suhh', 'anj', 'suhh', 'kav']
#print(a)
print(" set in a in x", dedupe_v1(a))
print()
print(''' <===Using set method===>''')
print(" set in a in x", dedupe_v2(a))

#print(b)
print(" set in b in x", dedupe_v1(b))
print()
print(''' <===Using set method===>''')
print(" set in b in x", dedupe_v2(b))
