# use codinbat.com
print(
    '''Given a string, return a new string where the
    first and last chars have been exchanged..

    front_back('code') → 'eodc'
    front_back('a') → 'a'
    front_back('ab') → 'ba'
''')
def front_back(str):
  if len(str) <=1:
    return str
  
  #mid = str[1:len(str)-1]  # can be written as str[1:-1]
  mid = str[1:-1]
  #print("This is mid: ",mid)
  #print("This is: " ,str[-1])
  #print("This is: " ,str[len(str)-1])
  #print("This is: ",str[0])
  # last + mid + first
  #return str[len(str)-1] + mid + str[0]
  #===== OR ========
  return str[-1] + mid + str[0]  
'''
print(front_back('code'))# → 'eodc'
print(front_back('a'))# → 'a'
print(front_back('ab'))# → 'ba'

'''
print(front_back('code'))# → 'eodc'	'eodc'	OK	
print(front_back('a'))# → 'a'	'a'	OK	
print(front_back('ab'))# → 'ba'	'ba'	OK	
print(front_back('abc'))# → 'cba'	'cba'	OK	
print(front_back("'"))# → ''	''	OK
print(front_back(" "))# → ''	''	OK
print(front_back('Chocolate'))# → 'ehocolatC'	'ehocolatC'	OK	
print(front_back('aavJ'))# → 'Java'	'Java'	OK	
print(front_back('hello'))# → 'oellh'	'oellh'	OK	


