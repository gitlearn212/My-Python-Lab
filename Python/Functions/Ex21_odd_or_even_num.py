# Check weather the given number odd or even number
def odd_even_num(x):
    if x <= 0:
        print(f'Ivalid number {x} print a possitive number excluding 0')

    elif x % 2 == 0:
        print(f'Even number: {x}')
    else:
        print(f'Odd number: {x}')


number = int(input('Enter a possitive number:'))
odd_even_num(number)
