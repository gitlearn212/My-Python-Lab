# calculate number of days between two days [2014,7,2][2014-7-11]
from datetime import date

# To Fo with function
'''
def days_between(x, y):
    delta = 0
    f_date = x
    l_date = y
    delta = y - x
    return(delta.days)


f_date = (2014, 7, 2)
l_date = (2014, 7, 11)
print(days_between(f_date, l_date))
print(days_between(delta.days))

'''
f_date = date(2014, 7, 2)
l_date = date(2014, 7, 11)
delta = l_date - f_date
print(delta.days)
# or with the time 0:00:00
result = (f'{(l_date) - (f_date)}')
print(result)
