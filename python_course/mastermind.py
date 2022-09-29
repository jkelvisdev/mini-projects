import random
import time
print()
print()
print('**************** WELCOME TO MASTERMIND GAME ****************')
print()
print("HOW TO PLAY")
print()
print("You'll need to guess a 4 digits number")
print("HOW TO PLAY: You'll need to guess a 4 digits number")
print("If you guess the number at least 1 of the 4 numbers and its position then you'll get a STAR")
print("If you guess one of the numbers but not its position then you'll get an at (@)")
print()
print("RULES:")
print()
print("1. You must user 4 different numbers ex: 5463")
print("2. You have 15 attemps")
print()
input("Press any key to start ->")
print()


#defining variable


numbers = [*range(10)]
random.shuffle(numbers)
ia = numbers[:4]
stars = 0
ats = 0
attemps = 0
flag = True

#starting the game

while flag:
	attemps += 1
	print()
	print(f"Your ats are: {ats}")
	print(f"Your stars are: {stars}")
	print(f"Attemps left: {15-attemps}")
	print()

#Validator
	while True:
		user_number = input('Insert a 4 digits number -> ')
		print()
		repeated = []
		if len(user_number) == 4:
			for n in range(4):
				if int(user_number[n]) not in repeated:
					repeated.append(int(user_number[n]))
				else:
					print()
					print(" !!! Number must be different !!!")
					print()
		else:
			print()
			print(' ### Numbers must be 4 digits long ### ')
			print()
		if len(repeated) == 4:
			break

#defining rewards or winner
	if repeated == ia:
		print()
		print(f" ######### You won, number guessed '{ia} ######### '")
		break

	for x in range(4):
		if repeated[x] in ia:
			if ia[x] == repeated[x]:
				stars += 1
				print(f" ### You won 1 star ### ")
			else: 
				ats += 1
				print(f" ### You won 1 at ###")

	print()
	print(f"You have {ats} ats")
	print()
	print(f"You have {stars} stars")
	print()
	print(f"Attemps have {attemps} attemps left")
	print()

	if attemps > 15:
		print()
		print(f" ### Game over, you've exceded the 15 attemps ### ")
		flag = False

	while True:
		user_option = input("Do you want to keep playing?(y/n) -> ").lower()
			
		if user_option == 'y':
			break
		elif user_option == 'n':
			flag = False
			print()
			print('### Game was closed. ###')
			print()
			break
		else:
			print()
			print("I didn't understand your answer")
			print()