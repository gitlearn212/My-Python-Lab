def BinarySearch(list1, key):

    low = 0
    high = len(list1)-1
    Found = False
    while low <= high and not Found:
        mid = (low+high)//2
        if key == list1[mid]:
            Found = True
        elif key < list1[mid]:  # NOTE
             high = mid-1       # NOTE
            
        else:
             low = mid+1        # NOTE
            
    if Found == True:
        print("Key is found")
    else:
        print("Key not found")
        
list1 = [23,56,78,90,99,1,3,2,11]
list1.sort()
print(list1)
key = int(input("Enter a value: "))
BinarySearch(list1, key)
print()

        
# OR =================================

def BinarySearch1(list2, key1):

    low = 0
    high = len(list2)-1
    Found = False
    while low <= high and not Found:
        mid = (low+high)//2
        if key1 == list2[mid]:
            Found = True
        elif key1 > list2[mid]: # NOTE sort
             
            #low = mid+1        # NOTE sort
            high = mid-1        #==> Reverse sort
        else:
            low = mid+1         #==> Reverse sort
            #high = mid-1       # NOTE sort
    if Found == True:
        print("Key is found")
    else:
        print("Key not found")
        
list2 = [23,56,78,3,2,11]
list2.sort(reverse=True)
print(list2)
key1 = int(input("Enter a value: "))
BinarySearch1(list2, key1)




            


    
