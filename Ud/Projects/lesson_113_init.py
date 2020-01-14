print(''' Udemy Tutorial Lesson 113 __init__ 113''')


class PlayerCharacter:
    # Class Object Attribute
    membership = True
    # def__init__ is a constructer and self
    # means PlayerCharacter

    def __init__(self, name, age):
        # Here
        # if (self.membership):
        # OR User the class name
        if(PlayerCharacter.membership):
            self.name = name
            self.age = age

    def shout(self):
        print(f'My name is {self.name}')

    def run(self):
        print('run')
        return 'done'


player1 = PlayerCharacter("Cindy", " 28")
player2 = PlayerCharacter("Tom", " 29")

print(player1.shout())
print(player1.membership)
print(player2.membership)
#print(player1.name, end='')
# print(player1.age)
# print(player1.run())
#print(player2.name, end='')
# print(player2.age)
# print(player2.run())
