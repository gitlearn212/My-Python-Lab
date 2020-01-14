
def insertation_sort(list1):
    for index in range(1,len(list1)):
        temp = list1[index]
        while temp < list1[index-1] and index > 0:
            list1[index] = list1[index-1]
            index = index-1
        list1[index] = temp
        
list1 = [32, 5, 1, 64, 3]
insertation_sort(list1)
print(list1)

'''
    def insertation_sort(list1):
        for index in range(1,len(list1)):
            temp = list1[index]
            while temp < list1[index-1] and index > 0:# if first element is less then 0 element exit while loop 
                list1[index] = list1[index-1]# if first element is grater then 0 element move next
                index = index-1
            list1[index]  = temp

    list1 = [32, 5, 1, 64, 3]
    insertation_sort(list1)
    print(list1)
'''
