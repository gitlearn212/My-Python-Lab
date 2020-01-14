def algsorting2(data, target, low, high):
    if low > high:
        return False
    else:
        mid = (low + high)//2
        if target == data[mid]:
            return True
        elif target < data[mid]:
            return algsorting2(data, target, low, mid-1)
        else:
            return algsorting2(data, target, high, mid + 1)
    return False


data = [16, 18, 22, 25, 31, 33, 38, 40]
target = 250
print(algsorting2(data, target, 0, len(data) - 1))
