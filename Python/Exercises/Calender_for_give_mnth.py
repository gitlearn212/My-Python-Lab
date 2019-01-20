# Write a program to print the calendar for the given month and the year
import calendar
yr = int(input('enter a year: '))
mnth = int(input('enter a month: '))
# dt = int(input('enter a date : '))
print(calendar.month(yr, mnth))
