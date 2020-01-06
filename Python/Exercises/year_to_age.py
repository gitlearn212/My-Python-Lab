# The year is 2020.
# Find the age for each element from the given list year of birth
# Usin FOR LOOP

import time
years_of_birth = [1990, 1991, 1990, 2001, 2012, 2019]

current_year = int(time.strftime("%Y"))
ages = []
for year in years_of_birth:
    ages.append(2020 - year)
print(ages)

# Using ONE LINE CODE
# ages = [2020 - year for year in years_of_birth]
ages = [current_year - year for year in years_of_birth]
print(ages)
