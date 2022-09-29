#rock,papers, cissors simulator.
import random

playagain = True
print('Welcome to rock, paper, scissors game')
open = True

while open:
    ia = random.choice(['rock', 'paper', 'scissors'])
    user_option = int(input('type an option: \n1 - rock\n2 - paper \n3 - scrissor\n'))
    if user_option == 1 or user_option == 2 or user_option == 3:
        user = ['rock', 'paper', 'scissors']
        user_option = user[user_option - 1]
        if user_option == ia:
                print('The computer and you had the same:', ia)
        elif user_option == 'rock' and ia == 'scissors':
                print('You won, the compuer had:', ia, 'that loss agains your:',user_option)
        elif user_option == 'paper' and ia == 'rock':
            print('You won, the compuer had:', ia, 'that loss agains your:',user_option)
        elif user_option == 'scissors' and ia == 'paper':
            print('You won, the compuer had:', ia, 'that loss agains your:',user_option)
        else:
            print('You loss, the computer had:', ia,'and you had:',user_option)
    else:
        print('sorry, I did not understand you answer, try again using 1, 2 or 3')

    while playagain:    
        playing = input('would you like to play again (y/n)')
        if playing == 'n':
            print('Game was closed')
            open = False
            break
        elif playing == 'y':
            break
        else:
            print('sorry, I did not understand you answer, try again using lowercase "y" or "n"')