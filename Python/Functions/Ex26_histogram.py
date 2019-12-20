# Write a histogram program for given number
def histogram(items):
    for n in items:
        output = ''
        # times = n
        while (n > 0):  # or while(times > 0)
            output += '*'
            n -= 1  # times-=1
        print(output)


histogram([3, 4, 5, 6, 7])
