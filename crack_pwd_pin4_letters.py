from string import ascii_letters

for i in ascii_letters:
    for j in ascii_letters:
        for k in ascii_letters:
            for l in ascii_letters:
                print(i, j, k, l)

# 26lettres en minuscule + 26lettres en Majuscule -> 52lettres -> 52*4 -> 7 311 616 posibilités