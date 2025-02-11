# La fonction Map sert à appliquer une action sur tous les élément d'un tableau
def multiply_by2(item):
    return item * 2


print(list(map(multiply_by2, [1, 2, 3, 4, 5])))
