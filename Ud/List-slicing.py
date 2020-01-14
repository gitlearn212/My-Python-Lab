#What is the output of this code?
#Before you clikc RUN, guess the output of each print statement!

new_list = ['a', 'b', 'c']
print(new_list[1]) # print 'b'
print(new_list[-2]) # print 'b'
print(new_list[1:3]) # print ['b','c']
new_list[0] = 'z'
print(new_list) # print ['z', 'b', 'c']

my_list = [1,2,3]
bonus = my_list + [5] # copy bonus from my list and add 5 at the end
my_list[0] = 'z' # change 1 to x in my_list ['z',2','3']
print(my_list) # ['z',2','3']
print(bonus) # ['1',2','3','5']

