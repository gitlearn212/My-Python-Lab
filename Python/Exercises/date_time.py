# Write a program to display current date and time

import datetime
# simport time

w = datetime.datetime.now()
print(" Current Date and Time:", w.strftime('%d-%m-%Y %H:%M:%S'))

# print(time.ctime())
