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
def menu()
	print()
	print(" ----> Type the number of the option that you want <----")
	print()
	print("1. For ADDITION press 1 -> ")
	print("2. For SUBSTRACTION press 2 -> ")
	print("3. For MULTIPLICATION press 3 -> ")
	print("4. For DIVISION press 4 -> ")
	print()

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

def options(user_option):
#function to validate user option.
	if user_option == '1':
		return sum(n1,n2)
	elif user_option == '2':
		return substract(n1,n2)
	elif user_option == '3':
		return multiply(n1,n2)
	elif user_option == '4':
		return div(n1,n2)
	else:
		return None


flag = True

while flag:
	#welcome screens
	welcome()
	menu()

	#saving the user input
	user_option = user_input()

	#chosing the request.
	if options(user_option) != None:
		n1 = int(input("Type first number"))
		n2 = int(input("Type second number"))
		result = options(user_option)
		print(f"The result is {result}")
		print()
		break
	else:
		()
