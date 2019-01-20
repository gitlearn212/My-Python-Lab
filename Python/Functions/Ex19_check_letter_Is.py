# Inset and print the whole word if Is missing at the begining of the words
# If not print the whole word with is


def new_string(str):
    if len(str) >= 2 and str[:2] == 'Is':
        return str
    return 'Is ' + str


print(new_string('an array'))
print(new_string('Isempty'))
print(new_string('the room Clean?'))
