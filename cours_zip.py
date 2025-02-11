# La fonction Zip permet d'assembler des listes en format une autre liste
users_names = ['jeems', 'aliss', 'jyjy', 'alice']
users_emails = ['jeems@gmail.com', 'aliss33@gmail.com',
                'jyjy@gmail.com', 'alice10@gmail.com']
users_phones = ['10101010', '20202020', '30303030', '40404040']

print(list(zip(users_names, users_emails, users_phones)))
