alist = ['word', 'selection', 'sql','microsoft','sql','microsoft','pslq','sharepoint','sharepoint']
duplicates = []
print(" Original list" , alist)
for item in alist:
    if alist.count(item) > 1 :
        if item not in duplicates:
            duplicates.append(item)
print("\n Duplicate items in the list" , duplicates)


for item in alist:
    temp = item 
    if temp not in duplicates:
            duplicates.append(item)
duplicates.sort()
print("\n Non Duplicate items in the list" , duplicates)


