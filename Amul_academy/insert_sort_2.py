def insertation_sort(list1):
    for i in range(1, len(list1)):
        key = list1[i]

        while i > 0 and list1[i-1] > key:  # i is 1 and i-1 is 0

            # list[i] first assigns 32 then 5 then 1-64-3
            list1[i] = list1[i-1]

            i -= 1
            print("i-1", i)
            list1[i] = key
        print(list1)
    return list1


list1 = [32, 5, 1, 64, 3]
print(insertation_sort(list1))
