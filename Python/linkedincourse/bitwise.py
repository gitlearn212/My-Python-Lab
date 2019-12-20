# Bitwise
# Using & operator
# bit set means 1's (11111111)
'''
x = 0x0a    #   Initialized using Hexdecimal literal number
y = 0x02    #   Initialized using Hexdecimal literal number
z = x & y   #   Assigned Hexdecimal literal number to z

print(f'(hex) x is {x:02x}, y is {y:02x}, z is {z:02x}')  # print in Hex decimal {x:02x} print x with leading 0, the field 2 is 2 char wide and th x hex decimal format ((hex) x is 0a, y is 02, z is 02)
print(f'(bin) x is {x:08b}, y is {y:08b}, z is {z:08b}')  # print in binary {x:08b} print x with leading 0, the filed is 8 char wide b is binary rep of the value  
                                                          # (bin) x is 00001010, y is 00000010, z is 00000010 the first 4 digit is are hexdecimal 0s and the second 4 digits are the value of a which is 10

# In the above operation x & y. Only both the same value
# x is 00001010, y is 00000010, z will print only the same values from x and why this case 00000010
'''
'''
# Using | operator
x = 0x0a    #   Initialized using Hexdecimal literal number
y = 0x02    #   Initialized using Hexdecimal literal number
z = x | y   #   Assigned Hexdecimal literal number to z

print(f'(hex) x is {x:02x}, y is {y:02x}, z is {z:02x}')  # print in Hex decimal {x:02x} print x with leading 0, the field 2 is 2 char wide and th x hex decimal format ((hex) x is 0a, y is 02, z is 0a
print(f'(bin) x is {x:08b}, y is {y:08b}, z is {z:08b}')  # print in binary {x:08b} print x with leading 0, the filed is 8 char wide b is binary rep of the value  
                                                          # (bin) x is 00001010, y is 00000010, z is 00001010 the first 4 digit is are hexdecimal 0s and the second 4 digits are the value of a which is 10

# In the above operation x | y. check for the left or right bit is set
# x is 00001010, y is 00000010, z will print the set this case 00001010
'''
'''
# Change the value in y to y = 0x05
x = 0x0a    #   Initialized using Hexdecimal literal number
y = 0x05    #   Initialized using Hexdecimal literal number
z = x | y   #   Assigned Hexdecimal literal number to z

print(f'(hex) x is {x:02x}, y is {y:02x}, z is {z:02x}')  # print in Hex decimal {x:02x} print x with leading 0, the field 2 is 2 char wide and th x hex decimal format ((hex) x is 0a, y is 05, z is 0f
print(f'(bin) x is {x:08b}, y is {y:08b}, z is {z:08b}')  # print in binary {x:08b} print x with leading 0, the filed is 8 char wide b is binary rep of the value  
                                                          # (bin) x is 00001010, y is 00000101, z is 00001111, z is 00001010 the first 4 digit is are hexdecimal 0s and the second 4 digits are the value of a which is 10

# In the above operation x | y. and changing y = 0x05 the z value set all the bit
# x is 00001010, y is 00000101, z is 00001111 z will print the set this case 00001111

'''
'''
# Change the value in y to y = 0x0f
# change the operator to ^ Xor
x = 0x0a    #   Initialized using Hexdecimal literal number
y = 0x0f    #   Initialized using Hexdecimal literal number
z = x ^ y   #   Assigned Hexdecimal literal number to z

print(f'(hex) x is {x:02x}, y is {y:02x}, z is {z:02x}')    # print in Hex decimal {x:02x} print x with leading 0, the field 2 is 2 char wide and th x hex decimal format ((hex) x is 0a, y is 0f, z is 05
print(f'(bin) x is {x:08b}, y is {y:08b}, z is {z:08b}')    # (bin) x is 00001010, y is 00001111, z is 00000101, z is 00001010 the first 4 digit is are hexdecimal 0s and the second 4 digits are the value of a which is 10

# In the above operation x ^ y. compare the bit set and prints the differences
# (bin) x is 00001010, y is 00001111, z is 00000101 z will print the set this case 00000101
'''
'''
# Change the value in y to y = 0x01
# change the operator to shift left <<
x = 0x0a    #   Initialized using Hexdecimal literal number
y = 0x01    #   Initialized using Hexdecimal literal number
z = x << y   #   Assigned Hexdecimal literal number to z

print(f'(hex) x is {x:02x}, y is {y:02x}, z is {z:02x}')    # print in Hex decimal {x:02x} print x with leading 0, the field 2 is 2 char wide and th x hex decimal format ((hex) x is 0a, y is 01, z is 14
print(f'(bin) x is {x:08b}, y is {y:08b}, z is {z:08b}')    # (bin) x is 00001010, y is 00000001, z is 00010100, z is 00001010 the first 4 digit is are hexdecimal 0s and the second 4 digits are the value of a which is 10

# In the above operation x << y. compare the bit set and prints the differences
# (bin) x is 00001010, y is 00000001, z is 00010100 bits from x is shifted by one 000010100

'''

# Change the value in y to y = 0x01
# change the operator to shift right >>
x = 0x0a    #   Initialized using Hexdecimal literal number
y = 0x01    #   Initialized using Hexdecimal literal number
z = x >> y  #   Assigned Hexdecimal literal number to z

print(f'(hex) x is {x:02x}, y is {y:02x}, z is {z:02x}')    # print in Hex decimal {x:02x} print x with leading 0, the field 2 is 2 char wide and th x hex decimal format ((hex) x is 0a, y is 01, z is 05
print(f'(bin) x is {x:08b}, y is {y:08b}, z is {z:08b}')    # (bin) x is 00001010, y is 00000001, z is 00000101, z is 00001010 the first 4 digit is are hexdecimal 0s and the second 4 digits are the value of a which is 10

# In the above operation x >> y. compare the bit set and prints the differences
# (bin) x is 00001010, y is 00000001, z is 00000101, bits x is s shifted by one 00001010












