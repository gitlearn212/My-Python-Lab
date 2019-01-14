# DCTIONARY as like list Dictionary is mutable so the value can be changed at any point
# At this point we are getting only the keys and we are not getting the values
x = {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5}
for i in x:
    print('i is {}'.format(i))

x = {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5}
for i in x:
    print('i is {}'.format(i))


# Here is how we get the key and value and also how the key value can be changed
x = {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5}
x['three'] = 33
for k, v in x.items():
    print('Key is {}, Value is {}'.format(k, v))

# Here is how we get the value
x = {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5}
for k, v in x.items():
    print('Value is {}'.format(v))

# Here is how we get the key
x = {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5}
for k, v in x.items():
    print('key is {}'.format(k))