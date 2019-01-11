# bubble sort

#lot=[99,1,65,2,78,349,25,199,12,0] # Array
lot= [101,33,54,21,65,89,7,3,58,1,54,23,7,2]
for i in range (len(lot)-1,0,-1): # for loop ie for i=lot-1,i>0,--i
 for j in range(i):
  if lot[j]> lot[j+1]:              # Swapping numbers (Ascending order)
      lot[j],lot[j+1]=lot[j+1],lot[j]
print (lot)
