def algsorting3(data, target, low, high):
    
    if low > high:
        return False
    else:
        mid = (low + high)//2
        if target == data[mid]:
            return True
        elif target < data[mid]:
            return algsorting3(data, target, low, mid-1)
        else:
            return algsorting3(data, target, high, mid+1)
            
    return False      
    
data =[16,18,22,25,31,33,38,40]
target = 29
print(algsorting3(data, target, 0, len(data)-1))

