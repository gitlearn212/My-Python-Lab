# use codinbat.com
print(
    '''Given 2 int values, return True
    if one is negative and one is positive.
    Except if the parameter "negative" is True, then return True only
    if both are negative..
''')

def pos_neg(a, b, negative):
    
    if negative:
        return (a < 0 and b < 0)
    return ((a < 0 and b > 0) or (a > 0 and b < 0))
        


'''
print(pos_neg(1, -1, False))# → True
print(pos_neg(-1, 1, False))# → True
print(pos_neg(-4, -5, True)) # → True
print(pos_neg(-1, 1, True)) # False

'''
print(pos_neg(1, -1, False))# → True	True	OK	
print(pos_neg(-1, 1, False))# → True	True	OK	
print(pos_neg(-4, -5, True))# → True	True	OK	
print(pos_neg(-4, -5, False))# → False	False	OK	
print(pos_neg(-4, 5, False))# → True	True	OK	
print(pos_neg(-4, 5, True))# → False	False	OK	
print(pos_neg(1, 1, False))# → False	False	OK	
print(pos_neg(-1, -1, False))# → False	False	OK	
print(pos_neg(1, -1, True))# → False	False	OK	
print(pos_neg(-1, 1, True))# → False	False	OK	
print(pos_neg(1, 1, True))# → False	False	OK	
print(pos_neg(-1, -1, True))# → True	True	OK	
print(pos_neg(5, -5, False))# → True	True	OK	
print(pos_neg(-6, 6, False))# → True	True	OK	
print(pos_neg(-5, -6, False))# → False	False	OK	
print(pos_neg(-2, -1, False))# → False	False	OK	
print(pos_neg(1, 2, False))# → False	False	OK	
print(pos_neg(-5, 6, True))# → False	False	OK	
print(pos_neg(-5, -5, True))# → True	True	OK	

