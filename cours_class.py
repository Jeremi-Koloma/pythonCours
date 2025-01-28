# OOP  Obect Oriented Programming
class PlayerCharacter:
    # class object Attribute
    membership = True
    def __init__(self, name, age):
        self.name = name # attribute
        self.age = age

    def run(self):
        print('Run')
        return 'done'


player1 = PlayerCharacter('Alou', 20)
player2 = PlayerCharacter('Mateo', 90)
print(player1.name)
print(player1.age)
print(player1.membership)