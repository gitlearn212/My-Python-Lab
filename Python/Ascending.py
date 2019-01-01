# bubble sort

lot=[99,1,65,2,78,349,25,199,12,0] # Array
for i in range (len(lot)-1,0,-1): # for loop ie for i=lot-1,i>0,--i
 for j in range(i):
  if lot[j]> lot[j+1]:              # Swapping numbers (Ascending order)
      lot[j],lot[j+1]=lot[j+1],lot[j]
print (lot)
