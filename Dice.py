#DiceRoller

import random

def dice_Roller():
	x = input('Do you want to roll? y/n ')
	while str.lower(x) == 'y':
		print(random.randint(1,6))
		x = input('Do you want to roll again? y/n')

dice_Roller()