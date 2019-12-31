def doublechar(str):
    result = ''
    for char in str:
        result+=(char*2)
    return result
    
print(doublechar("abc"))
print(doublechar("aabb"))
print(doublechar("aabbcc"))
print(doublechar("abcdef"))

        
