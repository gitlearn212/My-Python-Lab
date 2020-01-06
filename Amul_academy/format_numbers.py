# print numbers in revers order
for i in [20,10,30,3,4][::-1]: # ::-1 are the steps like list(a)-1,0-1)
    print(i)
print()

# list1 = [20,10,3,4]
for i in sorted([20,10,3,4]): # sort the numbers in ascending order
    print(i)
print()

for i in sorted([20,10,3,4],reverse = True): # sort the numbers in reverse order
    print(i)
print()

for i in [20,10,3,4].sort(): # not a valid  programme
    print(i)
print()
