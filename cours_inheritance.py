# Classe parente
class User():
    def sign_in(self):
        print('Logged In')

# Héritage


class Wizard(User):
    def __init__(self, name, power):
        self.name = name
        self.power = power

    def attack(self):
        print(f'Attack with power of {self.power}')


class Archer(User):
    def __init__(self, name, num_arrows):
        self.name = name
        self.num_arrows = num_arrows

    def attack(self):
        print(f'Attack with arrows: arrows left- {self.num_arrows}')


# Créons des intances des classes
wizard1 = Wizard('Job', 50)
wizard1.attack()

archer1 = Archer('Robin', 1000)
archer1.attack()

# Méthode abstraite
wizard1.sign_in()
archer1.sign_in()
