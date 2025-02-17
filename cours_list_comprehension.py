# list, set, dictionary

# list comprehension
my_list = [char for char in 'hello']
my_list2 = [num for num in range(0, 100)]
my_list3 = [num**2 for num in range(0, 100)]
my_list4 = [num**2 for num in range(0, 100) if num % 2 == 0]

print(my_list)
print(my_list2)
print(my_list3)
print(my_list4)

# dictionar comprehension
simple_dict = {
    'a': 1,
    'b': 2
}

my_dict = {k: v**2 for k, v in simple_dict.items() if v % 2 == 0}
print(my_dict)

# set comprehension
# chercher les élements dupliquer
some_list = ['a', 'b', 'c', 'b', 'b', 'd', 'm', 'n', 'n', 'o']
duplicates = list(set([x for x in some_list if some_list.count(x) > 1]))
print(duplicates)
