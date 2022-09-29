print()
print()
print('---- Bienvenido al crupier automatico ----')
print()
print('Creando el mazo')

time.sleep(1)
print('.')
time.sleep(1)
print('..')
time.sleep(1)
print('...')\

numeros = ['1', '2', '3', '4', '5', '6', '7', '10', '11', '12']
tipo = ['Oro', 'Bastos', 'Copa', 'Espada']
mazo = []

for x in numeros:
	for y in tipo:
		carta = f'{x} de {y}'
		mazo.append(carta)
print()
print('-- Deck Created --')

player_1 = []
player_2 = []
player_3 = []
player_4 = []
count = 0

print('Shuffling deck.')
time.sleep(1)
print('Shuffling deck..')
time.sleep(1)
print()
print('done.')
print()
random.shuffle(mazo)

while count < 4:

	card_1 = mazo.pop(0)
	card_2 = mazo.pop(1)
	card_3 = mazo.pop(2)
	card_4 = mazo.pop(3)

	player_1.append(card_1)
	player_2.append(card_2)
	player_3.append(card_3)
	player_4.append(card_4)
	count += 1

	print(f'Round number {count} is completed')
	print()
	time.sleep(1)


print('--- Cards in Deck ---'.center(60))

for x in range(0, len(mazo), 4):
	print(f' {mazo[x]:15} --- {mazo[x+1]:15} --- {mazo[x+2]:15} --- {mazo[x+3]:15}')


print('---- Players cards -----'.center(60))
print()
print()
print('---- Player 1 ----      ---- Player 2 ----    ---- Player 3 ----     ---- Player 4 ----')

cards = len(player_1) + len(player_2) + len(player_3) + len(player_4)

for y in range(4):
	print(f' {player_1[y]:15} ---- {player_2[y]:15} ----  {player_3[y]:15} ---- {player_4[y]:8} ----')