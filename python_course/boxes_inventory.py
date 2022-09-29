boxes = [
	[
	[['a', 5] , ['b', 7], ['c', 2], ['d', 4], ['e', 8]],
	[['f', 1] , ['g', 3], ['h', 4], ['i', 8], ['j', 12]], 
	[['k', 24], ['l', 15],['m', 1], ['n', 0], ['ñ', 3]]
	],
	[
	[['o', 4], ['p', 8], ['q', 6], ['r', 6], ['s', 7]],
	[['t', 2], ['u', 9], ['v', 8], ['w', 8], ['x', 4]],
	[['y', 1], ['z', 7], ['', 0], ['', 0], ['', 0]]]
	]
'''
# here with 3 for cicles we are getting access to the element
#first for enter to main list, 2nd to the boxes and 3 to the rows.
#then is printed with index 0
#program that shows the options for users
#show inventory, sell a letter, refill a letter and exit.

'''
while True:
	print()
	print('1. Show inventory')
	print('2. Sell a letter')
	print('3. Add a letter')
	print('4. Exit')
	print()

	option = input('----> ')

	if option == '1':
		for item in boxes:
			for row in item:
				for space in row:
					print(f'{space[0]:2}:{space[1]:2}     ', end = '')
				print()
			print()
	elif option == '2':
		letter = input('Type the letter that you want to sell: ')
		qty = int(input('Quantity to sell: '))
		for x in boxes:
			for y in x:
				for z in y:
					if z[0] == letter.lower():
							z[1] -= qty
							print(f'You have sold {qty} letters, {z[0]} letters left {z[1]}')

	elif option == '3':
		letter_to_add = input('Type the letter that you would like to add: ')
		qty = int(input('Quantity to add: '))
		for x in boxes:
			for y in x:
				for z in y:
					if z[0] == letter_to_add.lower():
						z[1] += qty	
						print("We have the letter,",letter_to_add," in the box, we've added the amount of",qty,"to that letter.")
	elif option == '4':
		print('Inventory has been closed')
		break