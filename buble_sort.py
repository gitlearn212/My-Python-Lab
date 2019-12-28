# List comprahancen method
list1 = []
num = int(input(" howmany Numbers: "))
print("Enter values: ")
list1=[int(input()) for x in range(num)]

# OR 
#num = int(input(" howmany Numbers: "))
#print("enter values")
#for k in range(num):
#    list1.append(int(input()))

print("Unsorted list: ", list1)

for j in range(len(list1)-1,0,-1): #Method2 for j in range(len(list1)-1):  #Method3  for j in range(len(list1)-1):
    for i in range(j):             #Method2 for i in range(len(list1)-1-j): #Method3 for i in range(len(list1)-1-j) 
        if list1[i] > list1[i+1]:
            list1[i],list1[i+1] = list1[i+1], list1[i]
            print(list1)
        else:
            print(list1)
    print(" = "*num, "\n")

print("sorted list:",list1)
                           
