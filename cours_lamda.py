# Une fonction Lamda sert à exécuter une fonction une seule fois sans la garder dans la mémoire
# C'est une fonction anomyme

from functools import reduce

my_list = [2, 4, 6, 8, 10]

print(list(map(lambda item: item * 2, my_list)))

# La fonction Filter avec lamda

print(list(filter(lambda currentItem: currentItem > 5, my_list)))

# La fonction Reduce avec lamda
print(reduce(lambda acc, item: acc + item, my_list))
