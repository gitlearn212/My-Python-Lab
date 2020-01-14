print('''Udemy Tutorila lesson 111''')
class PlayerCharacter:
    def __init__(self, name, age):
        self.name = name
        self.age = age


    def run(self):
        print('run')
        return 'done'


player1 = PlayerCharacter("Cindy", " 28")
player2 = PlayerCharacter("Tom", " 29")


print(player1.name, end='')
print(player1.age)
print(player1.run())
print(player2.name, end='')
print(player2.age)
print(player2.run())
