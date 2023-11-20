print('Welcome to the caesar cipher')
code = input('Encrypt or decrypt the text? e - Encrypt, d - Decrypt\n')
lang = (26, 32)[input('Language? r - russian, a - english\n') == 'r']
text = input('\nEnter text:\n').replace('ё', 'е').replace('Ё', 'Е')
rot = int(input('Entrer the number of shift:\n'))

if lang == 26:
    var_1 = 'A'
    var_2 = 'a'
else:
    var_1 = 'А'
    var_2 = 'а'

if code == 'ee':
    new_line = [(i, chr(ord((var_1, var_2)[i.islower()]) + (ord(i) - ord((var_1, var_2)[i.islower()]) + rot) % lang))[i.isalpha()] for i in text]
else:
    new_line = [(i, chr(ord((var_1, var_2)[i.islower()]) + lang - 1 - (ord((var_1, var_2)[i.islower()]) + lang - 1 - ord(i) + rot) % lang))[i.isalpha()] for i in text]

print(*new_line, sep='')