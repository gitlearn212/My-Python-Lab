# check if passed letter is vowel
# If vowel True else False

'''
def is_vowel(char):
    vowels = 'aeiou'
    # return char not in vowels
    return char in vowels
print(is_vowel('c'))
print(is_vowel('e'))
'''


def is_vowel(char):
    vowels = vowles = ['a','e','i','o','u','A','E','I','O','U'] # Or 'aeiou'
    if char in vowels:
        print(f'Is VOWEL {char}')
    else:
        print(f'NOT A VOWEL {char}')


string = str(input('Enter a letter: '))
is_vowel(string)
