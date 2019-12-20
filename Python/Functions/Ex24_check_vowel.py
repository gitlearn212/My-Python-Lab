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
    vowels = 'aeiou'  # or vowles = ['a','e','i','o','u']
    if char in vowels:
        print(f'Is VOWEL {char}')
    else:
        print(f'NOT A VOWEL {char}')


let = str(input('Enter a letter: '))
is_vowel(let)
