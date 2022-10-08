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
	print("5. To CLOSE press 5 -> ")
	print()

def option_validator(option):
	#validating user option
	option_list = ['1', '2','3','4','5']
	if user_option	in option_list:
		return option
	return None

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
	if number1.isnumeric() == True and number2.isnumeric() == True:
		number1 = int(number1)
		number2 = int(number2)
		return number1, number2
	else:
		None

flag = True

while flag:
	#welcome screen
	welcome()
	menu()

	#input and option validator.
	while True:
		user_option = input("Type an option -> ")
		if option_validator(user_option) != None:

			n1 = input("Type a number -> ")
			n2 = input("Type a second number -> ")

			if validator(n1, n2) != None:
				n1,n2 = validator(n1,n2)
				break
			else:
				print("You must type a valid number")
		else:
			print("You must select a valid option")


	#doing the operations.
	if user_option == '1':
		print(f"The result is: {sum(n1, n2)} ")
	elif user_option == '2':
		print(f"The result is: {substract(n1, n2)} ")
	elif user_option == '3':
		print(f"The result is: {multiply(n1, n2)} ")
	elif user_option == '4':
		print(f"The result is: {div(n1, n2)} ")
	elif user_option == '5':
		print(" -----> The calculator was closed <----- ")
		break
	else:
		print("You must chose a valid option to operate")

	#Checking if the user wants to keep the calculator open
	while True:
		option = input("Do you want to continue -> (y/n)")

		if option.lower() == 'n':
			print(" ---- Calculator was closed ---- ")
			flag = False
			break
		elif option.lower() == 'y':
			break
		else:
			print("You must type a valid option.")
			print()