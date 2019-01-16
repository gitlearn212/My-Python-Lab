

# For loop Chapter 6 using Tuple Tuple is () list is [] Dictionary is {}

animals = ('bear', 'bunny', 'dog', 'cat', 'velociraptor')

for pet in animals:
    if pet == 'dog': continue  # this will not print the dog from the list because it shorcut the loop
    if pet == 'cat': break  # this will break the loop once reached cat not printing cat in this case it will only print bear and bunny as cat is skipped from the continue 
    #if pet == 'velociraptor': break # if this line is in use then the else is not executed. IT EXITS the loop NORMALY by EXHAUSTING THE LOOp
    print(pet)
else:
    print ('That is all the animals')

