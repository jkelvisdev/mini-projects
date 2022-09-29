import random

print('Game has started')

while True:
    s_number = input('Type a number between 0 - 9 ')
    s_number = int(s_number)
    number = random.randint(0, 9)
    if s_number == number:
        print('You have guessed the number ', s_number, ' succefully with ', number)
        x= input('Do you want to play again? y/n ')
        if x.lower() == 'n' or x.lower() == 'no':
            print('The game has been closed')
            break
    elif s_number > 9 and s_number < 0:
        print('You should select a number between 0 and 9')
    else:
        print('The number ', s_number,' doesnt match with ', number)
