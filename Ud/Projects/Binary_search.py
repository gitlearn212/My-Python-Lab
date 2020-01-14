# Binary Search
def binary_search(arrar, item, left, right):
    if right < left:
        return - 1
    middle = left + (right - left) // 2
    if array[middle] == item:
        return middle
    elif array[middle] > item:
        return binary_search(array, item, left, middle - 1)
    elif array[middle] < item:
        return binary_search(array, item, middle + 1, right)


if __name__ == "__main__":
    array = [1, 4, 7, 8, 9, 10, 20, 22, 25]
    print(binary_search(array, 10, 0, len(array)-1))
