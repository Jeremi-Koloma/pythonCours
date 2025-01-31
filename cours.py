# Fundamental Data Types

# int and float
print(type(10))
print(type(10 + 5))
print(type(30.7))

# math functions
print(round(3.1))
print(abs(-20))

# Operator precedence
print(20 - 3 * 4)

# int number to binary
print(bin(260956))
print(int('0b111111101101011100', 2))

# augmented assignment operator
some_value = 5
some_value += 2
print(some_value)

# formatted strings
name = 'Jeremy'
age = 55
print(f'hi {name}. You are {age} years old')

# string indexes
selfish = 'me me me'
print(selfish[0])
selfish2 = '01234567'
# [start:stop:stepover]
print(selfish2[0:8:2])

# string methods
quote = 'to be or not to be'
print(quote.upper())
print(quote.lower())
print(quote.find('be'))
print(quote.replace('be', 'me'))

# booleans
is_cool = False
print(is_cool)

# Exercice birth year calculator
birth_year = input('what year were you born ?')
age = 2025 - int(birth_year)
print(f'Hello ! You are {age} years old')

# Exercice password checker
username = input('what is your username ?')
password = input('what is your password ?')
password_length = len(password)
hidden_password = '*' * password_length
print(
    f'{username}, your password {hidden_password} is {password_length} letters long'
)

# lists and slicing
amazon_cart = ['notebooks', 'sunglasses', 'toys', 'grapes']
print(amazon_cart)
print(amazon_cart[0:2])
amazon_cart[0] = 'laptop'
print(amazon_cart)
new_cart = amazon_cart[:]
new_cart[0] = 'gum'
print(new_cart)
print(amazon_cart)

# matrix
matrix = [[1, 2, 3], [2, 4, 6], [7, 8, 9]]
print(matrix[0][1])

# list methods
basket = [1, 2, 3, 4, 5]
print(len(basket))
# adding
basket.append(100)
new_list = basket
print(basket)
print(new_list)
# insert
# [index, value]]
basket.insert(4, 200)
print(basket)
# removing
basket.pop()
print(basket)
# [index]]
basket.pop(0)
print(basket)
# [value]]
basket.remove(4)
print(basket)
# clear
basket.clear()
print(basket)
# in
basket = ['a', 'z', 'b', 'x', 'c', 'd', 'e', 'd', 'd']
print('c' in basket)
print('i' in 'hi my name is Ian')
# count
print(basket.count('d'))
# sort
basket.sort()
print(basket)
# range
print(list(range(1, 20)))

# lis unpacking
a, b, c, *other, d = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(a)
print(b)
print(c)
print(other)
print(d)

# dictionary
distonarie = {'a': 1, 'b': 2}
print(distonarie['b'])
my_list = [
    {
        'a': [1, 2, 3],
        'b': 'hello',
        'x': True
    },
    {
        'a': [4, 5, 6],
        'b': 'Mali',
        'x': False
    },
]
print(my_list[0]['a'][2])
print(my_list[1]['b'])

# dictionary methods
user = {'basket': [1, 2, 3], 'greet': 'hello', 'age': 20}
print(user.get('age', 55))
print('basket' in user)
print('size' in user)
print('age' in user.keys())
print('hello' in user.values())
print(user.items())

# tupple immutable
my_tuple = (1, 2, 3, 4, 5)
print(my_tuple[1])
print(5 in my_tuple)

# set
my_set = {1, 2, 3, 4, 5, 5}
print(my_set)
my_set.add(100)
my_set.add(2)
print(my_set)
my_list = [1, 2, 3, 4, 5, 5]
print(set(my_list))
# set methods
your_set = {4, 5, 6, 7, 8, 9, 10}
print(my_set.difference(your_set))
print(my_set.discard(5))
print(my_set)
print(my_set.difference_update(your_set))
print(my_set)
print(my_set.intersection(your_set))
print(my_set.isdisjoint(your_set))
print(my_set.union(your_set))
print(my_set.issubset(your_set))
print(my_set.issuperset(your_set))

# conditional logic
is_old = True
is_licenced = True

if is_old:
    print('You are old enough to drive')
else:
    print('You are not old enough to drive')

if is_old and is_licenced:
    print('you are old enough to drive, and you have a licence!')

# and
if is_old and is_licenced:
    print('you are old enough to drive, and you have a licence!')
else:
    print('you are not old enough to drive, and you do not have a licence!')

# truthy and falsy
is_old = bool('hello')
is_licenced = bool(5)
print(bool('hello'))
print(bool(5))
print(bool(''))
print(bool(0))

# ternary operator
is_friend = True
can_message = "message allowed" if is_friend else "not allowed to message"
print(can_message)

# short circuiting
is_friend = True
is_user = True

if is_friend or is_user:
    print('best friends forever')

# logical operators
print(4 > 5)
print(4 < 5)
print(4 == 5)
print('hello' == 'hello')
print('a' > 'b')
print('a' > 'A')
print(1 < 2 < 3 < 4)
print(1 < 2 > 3 < 4)
print(1 >= 0)
print(1 <= 0)
print(0 != 0)
print(0 != 1)
print(not (True))
print(not (False))
print(not (1 == 1))

# exercise
is_magician = False
is_expert = True

if is_magician and is_expert:
    print('you are a master magician')
elif is_magician and not is_expert:
    print('at least you are getting there')
elif not is_magician:
    print('you need magic powers')

# is vs ==
print(True == 1)
print('' == 1)
print([] == 1)
print(10 == 10.0)
print([] == [])
# print(True is 1)
# print('' is 1)
# print([] is 1)
# print(10 is 10.0)
# print([] is [])

# for loops
for item in 'Zero to Mastery':
    print(item)

for item in [1, 2, 3, 4, 5]:
    print(item)

for item in {1, 2, 3, 4, 5}:
    print(item)

for item in (1, 2, 3, 4, 5):
    for x in ['a', 'b', 'c']:
        print(item, x)

# iterable - list, dictionary, tuple, set, string
# iterate - one by one check each item in the collection
user = {
    'name': 'Golem',
    'age': 5006,
    'can_swim': False
}

for item in user:
    print(item)

for item in user.items():
    print(item)

for item in user.values():
    print(item)

for item in user.keys():
    print(item)

for key, value in user.items():
    print(key, value)

# exercise
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
counter = 0
for item in my_list:
    counter = counter + item
print(counter)

# range
for number in range(0, 10):
    print(number)

for _ in range(0, 10, 2):
    print(_)

for _ in range(10, 0, -1):
    print(_)

for _ in range(2):
    print(list(range(10)))

# enumerate
for i, char in enumerate('Helloooo'):
    print(i, char)

for i, char in enumerate([1, 2, 3]):
    print(i, char)

for i, char in enumerate((1, 2, 3)):
    print(i, char)

for i, char in enumerate(list(range(100))):
    if char == 50:
        print(f'index of 50 is: {i}')

# while loops
i = 0
while i < 20:
    print(i)
    i = i + 1
else:
    print('done with all the work')

my_list = [1, 2, 3]
for item in my_list:
    print(item)
    continue

i = 0
while i < len(my_list):
    print(my_list[i])
    i += 1
    continue

while True:
    response = input('say something: ')
    if (response == 'bye'):
        break

# break, continue, pass
# exercise
picture = [
    [0, 0, 0, 1, 0, 0, 0],
    [0, 0, 1, 1, 1, 0, 0],
    [0, 1, 1, 1, 1, 1, 0],
    [1, 1, 1, 1, 1, 1, 1],
    [0, 0, 0, 1, 0, 0, 0],
    [0, 0, 0, 1, 0, 0, 0]
]

for row in picture:
    for pixel in row:
        if (pixel == 1):
            print('*', end='')
        else:
            print(' ', end='')
    print('')

# exercise
some_list = ['a', 'b', 'c', 'b', 'd', 'm', 'n']

# funciton


def say_helo():
    print('helloooo')


say_helo()

# parameters


def say_helllo(name, emoji):
    print(f'helloooo {name} {emoji}')


# arguments
say_helllo('Jeremy', '😇')
say_helllo('Dan', '😇')
say_helllo('Emily', '😇')

# default parameters


def say_hello(name='Darth Vader', emoji='😈'):

    say_hello(name='Bibi', emoji='😇')

# retrun


def sum(num1, num2):
    return num1 + num2


print(sum(4, 5))

# doctstring


def test(a):
    '''
    Info: this function tests and prints param a
    '''
    print(a)


test(5)

# Walrus operator
a = 'helloooooooooooo'
if ((n := len(a)) > 10):
    print(f'too long {n} elements')

while ((n := len(a)) > 1):
    print(n)
    a = a[:-1]

# oop / obect oriented programming

# Class


class PlayerCharacter:
    def __init__(self, name, age):
        self.name = name  # attribute
        self.age = age

    def run(self):
        print('Run')
        return 'done'


player1 = PlayerCharacter('Alou', 20)
player2 = PlayerCharacter('Mateo', 90)
print(player1.name)
