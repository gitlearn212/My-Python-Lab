def evennumber(list1):
   count = 0
   for x in list1:
       if x % 2 == 0:
            count+=1
   return count
list1=[2,1,2,3,4,8,66]
print(evennumber(list1))
       
       
