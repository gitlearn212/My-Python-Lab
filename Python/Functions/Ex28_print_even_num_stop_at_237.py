# Print all the even numbers from the given list and stop when it reach 237


def print_even_numbers(numbers):
    for x in numbers:
        if x == 237:
            print(x)
            break
        elif x % 2 == 0:
            print(x)
        else:
            pass


a = [386, 462, 47, 418, 907, 344, 236, 375, 823, 566, 597, 978, 328, 615, 953,
     345, 399, 162, 758, 219, 918, 237, 412, 566,
     826, 950, 626, 949, 687, 217, 815, 67, 104, 58, 512, 24, 892, 894, 767,
     553, 81, 379, 843, 831, 445, 742, 717, 958, 743, 527]

print(print_even_numbers(a))
# print(print_even_numbers(a, end=''))
'''
numbers = [386, 462, 47, 418, 907, 344, 236, 375, 823, 566, 597, 978, 328, 615,
            953, 345, 399, 162, 758, 219, 918, 237, 412, 566,
           826, 950, 626, 949, 687, 217, 815, 67, 104, 58, 512, 24, 892, 894, 
           767, 553, 81, 379, 843, 831, 445, 742, 717, 958, 743, 527]
for x in numbers:
    if x == 237:
        print(x)
        break
    elif x % 2 == 0:
        print(x)
'''
