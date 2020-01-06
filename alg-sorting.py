def algsorting(data, target):
    low = 0
    high = len(data) - 1

    while low <= high:
        mid = (low + high)//2
        if target == data[mid]:
            return True
        elif target < data[mid]:
            high = mid - 1
            
        else:
             low = mid + 1
    return False      

data =[16,18,22,25,31,33,38,40]
target = 22
print(algsorting(data, target))
