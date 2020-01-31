num = input(" Enter an odd length number: ")
length = (len(num))
for row in range(length):
    for col in range(length):
        if row==col or row+col ==length-1:
            print(num[row], end=" ")
        else:
            print(" ", end=" ")
    print(" ")
        
