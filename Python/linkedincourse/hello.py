a = 23
b = 45
# This is the format method. The feature version
print("Hello, World. {}" .format((a+b)*(b+a)))

# or use the f method f = format
a = 23
b = 45
c = (a+b)*(b+a)
# This is the format method. The feature version
print(
    f"This f stands for format this also another way of writting code in python3: {(3*(a+b)*(b+a))}")


a = 23
b = 45
c = a+b
# This is from legasy code from python2. This method is depricated in the feature version so use .format method instead
print("Hello, World, This is a legacy method of coding and this method is  depricated in the feature version %d" % c)

