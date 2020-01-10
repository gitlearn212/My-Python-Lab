list1 = [1,2,3]
list2 = []
#list2 = [[i for i in [list1]] for i in range(4)]
 # OR
for i in range(4):
   for i in [list1]:
       list2.append([i])

print()
print(list2)

