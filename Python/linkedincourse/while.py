# Using While loop
# Exercise 1
# In this method list has only 5 string so while is <= 5 should work if the list has 6 or 7 objects then there will be an error OUT OF RANGE
# To Avoid use the second Exercise
# 
''' 
words = ["one", "two", "three", "four", "five"]
n = 0
while(n < 5):
    print(words[n])
    n += 1
'''
# OR use this method 
# Exercise 2
words = ["one", "two", "three", "four", "five","six"]
count = 0
for x in range(len(words)): 
    while(count <= x ):
        print((count+1), words[count])
        count += 1