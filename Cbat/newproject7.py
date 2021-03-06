# use codinbat.com
print(''' Given a non-empty string and an int n,
  return a new string where the char at index n has been removed.
  The value of n will be a valid index of a char in the original string
  (i.e. n will be in the range 0..len(str)-1 inclusive). ''')

def missing_char(char, n):
     
    front = char[:n]   # up to but not including n
    back = char[n+1:]  # n+1 through end of string
    return front + back

print(missing_char('kitten', 1))# → 'ktten'
print(missing_char('kitten', 0))# → 'itten'
print(missing_char('kitten', 4))# → 'kittn'
# or
'''
for i in range(0,5):    
    print(missing_char('kitten', i))
'''

