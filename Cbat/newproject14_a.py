print( ''' ==========THE PROBLEM======
        Given a string, we'll say that the front is
        the first 3 chars of the string.
        If the string length is less than 3,
        the front is whatever is there. Return a new string
        which is 3 copies of the front.
    ''')

print(''' ============THE SOLUTION========
          Assign a variable to a value
          check if the length of the string(str)
          is less then the variable(vlaue).
          if the string lenght is less then the variable(value)
          then do nothing (pass)
          if the length is grater then the variable(given value)
          then  return string which is grater then the variable value and
          multiply the string 3 times

        ''')

print(''' =========THE CODE FOR THE PROBLEM==========
    def front3(str):
  frontend = 3 
  if len(str)< frontend:
    pass
  return str[:frontend]*3

==== OR THE FOLLOWING CODE ALSO WILL WORK =======

def front3(str):
  frontend = 3 
  if len(str)< frontend:
    # == OR ==
    
  #if len(str)> frontend:
    return str[:frontend]*3
    # ==OR pass==
      #pass
  return str[:frontend]*3


print(front3('Java'))# → 'JavJavJav'	'JavJavJav'	OK	
print(front3('Chocolate'))# → 'ChoChoCho'	'ChoChoCho'	OK	
print(front3('abc'))# → 'abcabcabc'	'abcabcabc'	OK	
print(front3('abcXYZ'))# → 'abcabcabc'	'abcabcabc'	OK	
print(front3('ab'))# → 'ababab'	'ababab'	OK	
print(front3('a'))# → 'aaa'	'aaa'	OK	
print(front3(','))# → ''	''	OK	


============== END ===========

''')

def front3(str):
  frontend = 3 
  #if len(str)< frontend:
    #pass
  #return str[:frontend]*3  
    # ==or ==
  if len(str)> frontend:
      pass #OR return str[:frontend]*3
  return str[:frontend]*3
  
      
  

print(front3('Java'))# → 'JavJavJav'	'JavJavJav'	OK	
print(front3('Chocolate'))# → 'ChoChoCho'	'ChoChoCho'	OK	
print(front3('abc'))# → 'abcabcabc'	'abcabcabc'	OK	
print(front3('abcXYZ'))# → 'abcabcabc'	'abcabcabc'	OK	
print(front3('ab'))# → 'ababab'	'ababab'	OK	
print(front3('a'))# → 'aaa'	'aaa'	OK	
print(front3(','))# → ''	''	OK	
