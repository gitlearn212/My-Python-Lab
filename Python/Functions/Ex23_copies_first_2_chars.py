# Write a Python program to copy the first 2 chars of the givne string
# If the chars are less then 2 then return the whole string with n copies


def substring_copy(str, n):
    flenth = 2
    if flenth > len(str):
        flenth = len(str)
    substr = str[:flenth]
    result = ""
    for i in range(n):
        result += substr
    return result


print(substring_copy('ewrwe', 2))
print(substring_copy('e', 3))
