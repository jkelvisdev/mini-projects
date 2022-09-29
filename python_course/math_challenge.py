import time
import random

print()
print(" *************** MATH CHALLENGE *************** ")
print()
input('Press enter to start')

start_time = time.time()
points = 0
  
while True:
    operation = random.choice(['+', '*'])
    left = random.choice(range(1,11))
    right = random.choice(range(1, 11))
    sum = random.choice(range(1,101))
    sum2 = random.choice(range(1,101))
    if operation == '+':
        result = sum + sum2
        print(sum,'+', sum2)
        user = int(input())
        if result == user:
            print("Correct, you've won: 1 point")
            points += 1
        else:
            print("Incorrect, try again")
    if operation == '*':
        print(left,'*', right)
        result = left * right
        user = int(input(''))
        if result == user:
            print("Correct, you've won: 1 point")
            points += 1
        else:
            print("Incorrect, try again")

    end_time = time.time()
    if end_time - start_time >= 10:
        break

print("the time is over, you've got:", points, 'points')
print("game is over")