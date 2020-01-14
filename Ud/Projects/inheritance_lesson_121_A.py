# Inheritance


class User():
    def sign_in(self):
        print('Logged in')


class Wizard(User):
    def __init__(self, name, power):
        self.name = name
        self.power = power

    def attack(self):
        print(f'attacking with power of {self.power}')


class Archer(User):
    def __init__(self, name, num_arrows):
        self.name = name
        self.num_arrows = num_arrows

    def arrow(self):
        print(f'attacked with arrows arroes left : {self.num_arrows}')


# instentiate
wizard1 = Wizard('suhumar', 200)
archer1 = Archer('Jay', 500)

wizard1.sign_in()
wizard1.attack()

archer1.sign_in()
archer1.arrow()
