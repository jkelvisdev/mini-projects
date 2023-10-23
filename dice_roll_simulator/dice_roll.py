import random
import time

answer = input('Do you want to roll the dice? Yes/no ')

if answer.lower() == 'yes' or answer.lower() == 'y':
    count = 0
    while True:
        dice = range(1,7)
        while count < 3:
            time.sleep(1)
            print('We are shaking the dice.')
            count = count + 1
        print('dice was thrown')
        time.sleep(1)
        print('the dice is showing the number', random.choice(dice))
        again = input('Do you want to roll the dice again? Yes/No ')
        count = 0
        if again.lower() == 'no' or again.lower() == 'n':
            print('The game is closed')
            break
elif answer.lower() == 'no' or answer.lower() == 'n':
    print('The game will be closed.')
else: 
    print('You should select a valid option')