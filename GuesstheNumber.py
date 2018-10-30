#GuesstheNumber

import random

def GuesstheNumber():
	x = input('Would you like to guess a number? Press "y" to play ')
	while str.lower(x) == 'y':
		z = random.randrange(0, 101, 2)
		answer = False
		y = int(input('Guess a number between 1 and 100'))
		while answer == False:
			if y == z:
				answer = True
				print("Great guess!!")
			elif y < z:
				print("Your number is too low!")
				y = int(input('Guess a number between 1 and 100'))
			elif y > z:
				print("Your number is too high!")
				y = int(input('Guess a number between 1 and 100'))
		x = input('Would you like to guess a number? Press "y" to play ')


GuesstheNumber()