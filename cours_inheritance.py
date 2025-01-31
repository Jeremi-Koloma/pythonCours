# Classe parente
class User():
    def __init__(self, email):
        self.email = email

    def sign_in(self):
        print('Logged In')

# Héritage


class Wizard(User):
    def __init__(self, name, power, email):
        super().__init__(email)
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
wizard1 = Wizard('Job', 50, 'exawizard@gmail.com')
wizard1.attack()
print(wizard1.email)
archer1 = Archer('Robin', 1000)
archer1.attack()

# Méthode abstraite
wizard1.sign_in()
archer1.sign_in()

# Vérifier si une classe est une instance
print(isinstance(wizard1, Wizard))

# Polymorphisme


def player_attack(player):
    player.attack()


player_attack(wizard1)
player_attack(archer1)
