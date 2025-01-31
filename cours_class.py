# OOP  Obect Oriented Programming
class PlayerCharacter:
    # class object Attribute
    membership = True

    def __init__(self, name, age):
        self.name = name  # attribute
        self.age = age

    def run(self):
        print('Run')
        return 'done'

    # Methode for the class itself
    @classmethod
    def adding_things(cls, num1, num2):
        return num1 + num2

    # Method for the class itself that not care the constructor attribute
    @staticmethod
    def adding_things2(num1, num2):
        return num1 + num2


player1 = PlayerCharacter('Alou', 20)
player2 = PlayerCharacter('Mateo', 90)
print(player1.name)
print(player1.age)
print(player1.membership)
print(player1.adding_things(5, 10))
print(PlayerCharacter.adding_things(1, 8))
