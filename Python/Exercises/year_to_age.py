# The year is 2018.
# Find the age for each element from the given list year of birth
# Usin FOR LOOP
years_of_birth = [1990, 1991, 1990, 1990, 1992, 1991]
ages = []
for year in years_of_birth:
    ages.append(2018 - year)
print(ages)

# Using ONE LINE CODE
# ages = [2018 - year for year in years_of_birth]
ages = [2018 - year for year in years_of_birth]
print(ages)
