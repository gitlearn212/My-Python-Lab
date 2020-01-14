# Inheritance


class User():
    def sign_in(self):
        print('Welcome to Python Class you are now Logged in')


class Wizard(User):
    def __init__(self, name, power):
        self.name = name
        self.power = power

    def attack(self):
        print(f'{self.name}: attacking with power of {self.power}')


class Archer(User):
    def __init__(self, name, num_arrows):
        self.name = name
        self.num_arrows = num_arrows

    def attack(self):
        print(f'{self.name}: attacked with arrows arroes left : {self.num_arrows}')


# instentiate
wizard1 = Wizard('suhumar', 200)
archer1 = Archer('Jay', 500)
wizard1.sign_in()
# use This method or for loop
'''
def player_atteck(char):
    char.attack

wizard1.attack()
archer1.attack()
'''
# use This loop or the above method
for char in [wizard1, archer1]:
    char.attack()
