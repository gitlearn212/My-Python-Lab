# Ternary condition operator is not supported prior to python version 3 and it is used occasionally
# If variable hungry is True than feed the bear 

hungry = True

x = 'Feed the bear now!' if hungry else 'Do not feed the bear.'
print(x)
# Change the condition to false
hungry = False

y = 'Feed the bear now!' if hungry else 'Do not feed the bear.'
print(y)
