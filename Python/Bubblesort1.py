arra=[32,45,6,43,1,8,76,99,0]
for i in range(len(arra)-1,0,-1):
  for j in range(i):
    if arra[j] > arra[j+1]:
       arra[j],arra[j+1]=arra[j+1],arra[j]
print(arra)
