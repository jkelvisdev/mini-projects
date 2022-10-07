#Basic calculator using functions
#using learning until now
#functions, operators, list, tuples, built-in functions, some methods(random, time, os)
#last topic learned: functions
#that's why the calculator must be made using functions.

#welcome screen
def welcome():
	print()
	print(" ###################### ")
	print(" ###################### ")
	print(" ##### CALCULATOR ##### ")
	print(" ###################### ")
	print(" ###################### ")
	print()

#menu options screen
def menu():
	print()
	print(" ----> Type the number of the option that you want <----")
	print()
	print("1. For ADDITION press 1 -> ")
	print("2. For SUBSTRACTION press 2 -> ")
	print("3. For MULTIPLICATION press 3 -> ")
	print("4. For DIVISION press 4 -> ")
	print()

def user_input():
	input("Type an option -> ")

def multiply(number1,number2):
#function that return multiplication result between 2 numbers 
	return number1 * number2

def div(number1,number2):
#function that return division result between 2 numbers 
	return number1 / number2

def sum(number1, number2):
#function that return the sum.
	return number1 + number2

def substract(number1, number2):
	return number1 - number2

def validator(number1, number2):
	if n1 == int and n2 == int:
		return True
	else:
		return None

flag = True

while flag:
	#welcome screen
	welcome()
	menu()

	#saving the user input
	user_option = user_input()

	#input validator.
	while True:

		n1 = int(input("Type a number -> "))
		n2 = int(input("Type a second number -> "))
		print(validator(n1,n2))

		if validator is True:
			break
		else:
			print("You must type a valid option.")
			print()

	#doing the operations.
	if user_option == '1':
		print(f"The result is: {sum(n1, n2)} ")
	elif user_option == '2':
		print(f"The result is: {substract(n1, n2)} ")
	elif user_option == '3':
		print(f"The result is: {multiply(n1, n2)} ")
	elif user_option == '4':
		print(f"The result is: {div(n1, n2)} ")
	else:
		print("You must chose a valid option to operate")

	#Checking if the user wants to keep the calculator open
	while True:
		option = input("Do you want to continue -> (y/n)")

		if option.lower() == 'n':
			print(" ---- Calculator was closed ---- ")
			break
			flag = False
		elif option.lower() == 'y':
			break
		else:
			print("You must type a valid option.")
			print()