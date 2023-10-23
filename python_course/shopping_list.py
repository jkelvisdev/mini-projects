shopping_list = []

while True:
	print()
	print('   -------- Shop List --------   ')
	print('-------- Chose an option --------')
	print()
	print('1. Add a product. ')
	print('2. Delete a product. ')
	print('3. Show the list')
	print('4. Exit')
	print()
	user_option = input('--> ')
	if user_option == '1':
		product = input('Type the product name: ')
		if product.lower() in shopping_list:
			print(f'The product -- {product.lower()} -- is in the list')
		else:
			shopping_list.append(product.lower())
			print(f'The product - {product} - was added to the list')
	elif user_option == '2':
		product = input('Product to remove: ')
		if product.lower() in shopping_list:
			print(f'The product - {product} - was removed from the list')
			shopping_list.remove(product.lower())
		else:
			print(f'The product -- {product.lower()} -- is not in the list')
	elif user_option == '3':
		if len(shopping_list) > 0:
			print('NAME'.center(10))
			for x in shopping_list:
				print(f' -- {x:5} --') 
	elif user_option == '4':
		print('Program was closed')
		break
	else:
		print('Please chose a valid option like: 1,2,3,4.')
		print()