import random
print('Welcome to number guessing game!')
def game():
    num = random.randint(1, 100)
    cnt = 0
    def is_valid(n):
        if str(n).isdigit():
            n = int(n)
            if 1 <= n <= 100:
                return True
            else:
                return False

    while True:
        response = int(input('Enter a number from 1 to 100: '))
        if not is_valid(response):
            print('You have to enter an integer 1 to 100')
            continue
        if response < num:
            print('Your number is less than the hidden one, try again!')
            cnt += 1
        elif response > num:
            print('Your number is more than the hidden one, try again!')
            cnt += 1
        else:
            print(f'You guessed it, congratulations!',
                   f'It took you {cnt} tries to guess')
            break
            
game()

while True:
    print('Do you want to play one more time? Enter Y or N: ')
    answer = input().upper()
    if answer == 'Y':
        game()
    elif answer == 'N':
        print('Thanks for playing. Bye!')
        break
    else:
        print('Enter Y or N: ')
        continue