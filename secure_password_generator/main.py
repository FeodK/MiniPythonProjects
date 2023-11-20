import random 
digits = '0123456789'
low_letters = 'abcdefghijklmnopqrstuvwxyz'
up_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
punctuation = '!#$%*+-=?@^_'

chars = ''
n = int(input('Enter the number of passwords to generate: '))
length = int(input('Enter password length: '))
add_digits = input('Iclude numbers? (y = yes / n = no): ')
add_low_letters = input('Iclude lowecase letters? (y = yes / n = no): ')
add_up_letters  = input('Iclude uppercase letters? (y = yes / n = no): ')
add_pun = input('Iclude characters such as !#$%*+-=?@^_? (y = yes / n = no): ')
rem_badsymbols = input('Exclude symbols il1Lo0O? (y = yes / n = no): ')

if add_digits == 'y':
    chars += digits
if add_low_letters == 'y':
    chars += low_letters
if add_up_letters == 'y':
    chars += up_letters
if add_pun == 'y':
    chars += punctuation
if rem_badsymbols == 'y':
    for el in 'il1Lo0O':
        chars = chars.replace(el, '')

def generatr_paaword(length, chars):
    password = ''
    for _ in range(length):
        password += random.choice(chars)
    return password

for _ in range(n):
    print(generatr_paaword(length, chars))