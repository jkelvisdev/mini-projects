import random

file = open('recipes.txt')

week = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
carbos = []
protein = []
veggies = []
menu = {}

#ordering elements by category ex: carbos, protein, veggies
for letter in file:
	word = letter.split()
	if word[0] not in carbos:
		carbos.append(word[0])
	if word[1] not in protein: 
		protein.append(word[1])
	if word[2] not in veggies:  
		veggies.append(word[2])


for day in range(len(week)):
	menu[week[day]] = [random.choice(carbos), random.choice(protein), random.choice(veggies)]
print()

for k,v in menu.items():
		print(f"{k} -> {v[0]}, {v[1]} y {v[2]}")

print()