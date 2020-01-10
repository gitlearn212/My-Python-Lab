# use codinbat.com
print(
    '''Given a string, we'll say that
    the front is the first 3 chars of the string.
    If the string length is less than 3,
    the front is whatever is there. Return a new string
    which is 3 copies of the front.

    front3('Java') → 'JavJavJav'
    front3('Chocolate') → 'ChoChoCho'
    front3('abc') → 'abcabcabc'
''')

   
def front3(str):
  # Figure the end of the front
  front_end = 3
  if len(str) < front_end:
    front_end = len(str)
  front = str[:front_end]
  # OR
  #front = str[0:front_end]
  #return front + front + front
  # OR========
  return front *3

  # Could omit the if logic, and write simply front = str[:3]
  # since the slice is silent about out-of-bounds conditions.

'''  
print(front3('Java'))# → 'JavJavJav'
print(front3('Chocolate'))# → 'ChoChoCho'
print(front3('abc'))# → 'abcabcabc'
'''

print(front3('Java'))# → 'JavJavJav'	'JavJavJav'	OK	
print(front3('Chocolate'))# → 'ChoChoCho'	'ChoChoCho'	OK	
print(front3('abc'))# → 'abcabcabc'	'abcabcabc'	OK	
print(front3('abcXYZ'))# → 'abcabcabc'	'abcabcabc'	OK	
print(front3('ab'))# → 'ababab'	'ababab'	OK	
print(front3('a'))# → 'aaa'	'aaa'	OK	
print(front3(''))# → ''	''	OK	
