list = [324,56,89,23,45,0,234,56,78,1,546,2,7,9,45,56,78,342,67,78,324,576,89,100]
for x in range(len(list)-1,0,-1):
     for y in range(x):
        if list[y] > list[y+1]:
                list[y],list[y+1] = list[y+1],list[y]
print(list)
#print(" ")

#for a in range(len(list)-1,0,-1):
#    for b in range(a):
#        if list[b] > list[b+1]:
#            temp = list[b]
#            list[b+1] = list[b]
#            list[b] = temp
#print(list)

#list.sort()

#print(" ")
#print(list)
