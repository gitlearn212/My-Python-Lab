# use codinbat.com
print(
    '''Given 2 int values, return True
    if one is negative and one is positive.
    Except if the parameter "negative" is True, then return True only
    if both are negative..
''')

def pos_neg(a, b, negative):
    
    if negative:
        #return (a < 0 and b < 0)
        #return ((a < 0 and b > 0) or (a > 0 and b < 0))
        # OR 
        pass
    #return ((a < 0 or a > 0) or (b > 0 or b < 0))
    # OR
    return ((a < 0 and b > 0) or (a > 0 and b < 0) or (a < 0 and b < 0))
'''
# OR
    negative = True
    while negative:
    #while True:
        return ((a < 0 and b > 0) or (a > 0 and b < 0) or (a < 0 and b < 0))
        # OR
        #return ((a < 0 or a > 0) or (b > 0 or b < 0))
 '''   
print(pos_neg(1, -1, False))# → True
print(pos_neg(-1, 1, False))# → True
print(pos_neg(-4, -5, True)) # → True