
def biggest(list1):
    biggest = None
    for value in list1:
        if biggest is None:
            biggest = value
        elif value < biggest:
            biggest = value
    return biggest


laist1 = [23, 45, 7, 90, 6757, 32, 56]
print(biggest(laist1))
