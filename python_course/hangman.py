import random
import os

#hangman draw
hangman = ['''
     +---+
     |   |
	 |
	 |
	 |
	 |
   ======''', 
'''
     +---+
     |   |
     O   |
	 |
	 |
	 |
   ======''', 
'''
     +---+
     |   |
     O   |
     |   |
	 |
	 |
   ======''', 
'''
     +---+
     |   |
     O   |
    /|   |
	 |
	 |
   ======''', 
'''
     +---+
     |   |
     O   |
    /|\  |
	 |
	 |
   ======''', 
'''
     +---+
     |   |
     O   |
    /|\  |
    /    |
	 |
   ======''', 
'''
     +---+
     |   |
     O   |
    /|\  |
    / \  |
	 |
   ======''']

#word list

words = ["hello", "plain", "sky", "water", "river", "ice", "iceberg", 
	"rain", "thunder","truck", "deliver", "heart", "love", "glass", "word", "world",
	"cheese", "bread", "avocado", "thumb"]

#variables and chosing a random word

word = random.choice(words)
hidden_word = ['_'] * len(word)
fail = 0
dictionary = "abcdefghijklmnopqrstuvwxyz"

while True:

	os.system('cls')

#showing hangman draw + fail attemps

	draw = hangman[0 + fail]

#welcome screen
	print(' ############# WELCOME TO HANGMAN ############# ')
	print()
	print()
	print(draw)
	print()
	print()

#validating winner
	if '_' not in hidden_word:
		hidden_word = ''.join(hidden_word)
		if hidden_word == word:
			print('      ####### YOU WON #######        ')
			break


	for y in hidden_word:
		print(f"{y.upper():2}", end = ' ')
	print()
	print()

#win or lose validator
	if fail <= 5:
		user_letter = input("Type a word -> ").lower()
	else: 
		print('      ####### GAME OVER #######        ')
		print()
		print('The word was:', word)
		print()
		break
#input validator

	if len(user_letter) != 1 or user_letter not in dictionary:
		print("You must type a valid option")
		print()
		break

#underscore replacemente if letter is in the hidden word
#if user don't guess the number the hangman index will increase(else part)

	if user_letter in word:
		print(user_letter)
		for i in range(len(word)):
			if word[i] == user_letter:
				hidden_word[i] = user_letter
	else:
		fail += 1