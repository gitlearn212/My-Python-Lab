#using this list: 
basket = ["Banana", ["Apples", ["Oranges"], "Blueberries"]];
# access "Oranges" and print it:

# ["Banana", ["Apples", ["Oranges"], "Blueberries"]]; 

print(basket[0]) # print banana
print(basket[1]) # print's ['Apples', ['Oranges'], 'Blueberries']
print(basket[1][1])# print's ['Oranges']
print(basket[1][1][0])# print's 'Oranges'
print(basket[1][0:])# print's['Apples', ['Oranges'], 'Blueberries']
print(basket[1][0:1])# print's['Apples']
print(basket[1][0:2])# print's['Apples', ['Oranges']]
print(basket[1][0:3])# print's['Apples', ['Oranges'], 'Blueberries']
print(basket[1][0:-1])# print's['Apples', ['Oranges']
print(basket[1][0:-2])# print's['Apples']
print(basket[1][-1:][0])# print's['Blueberries']
print(basket[1][-2:][1])# print's['Blueberries']
print(basket[1][-1])# print's Bluberries
print(basket[1][0])# print's Apples
print(basket[1][2])# print's Bluberries
print(basket[1][1])# print's [oranges]
print(basket[1][1][0])# print's oranges




