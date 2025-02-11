# La fonction reduce, permet de retourner un résultat unique
from functools import reduce

prices_list = [100, 200, 300, 400, 500]


def total_price(accumulator, price):
    return accumulator + price


print(reduce(total_price, prices_list, 0))
