#Andrew's Adventure

def andrew_adventure():
	x = input('Would you like to play a game? y/n ')
	while str.lower(x) == 'y':
		print('You have 6 moves to find your way out of this maze. Choose your moves wisely... ')
		print('You find yourself in a room. There is a door in front of you, to the left of you, and to the right of you')
		move = 6
		roomlist = [True, False, False, False, False, False, False]
		while move >= 1:	
			while roomlist[0] == True:
				firstmove = input('Which room do you choose? Front, left, or right? ')
				if str.lower(firstmove) == 'front':
					roomlist[0] = False
					roomlist[1] = True
					move = move - 1
					print(move)
				elif str.lower(firstmove) == 'left':
					roomlist[0] = False
					roomlist[2] = True
					move = move - 1
					print(move)
				elif str.lower(firstmove) == 'right':
					roomlist[0] = False
					roomlist[3] = True
					move = move - 1
					print(move)
			while roomlist[1] == True:
				secondmove = input('Which room do you choose? Back or left? ')
				if str.lower(secondmove) == 'back':
					roomlist[1] = False
					roomlist[0] = True
					move = move - 1
					print(move)
				elif str.lower(secondmove) == 'left':
					roomlist[1] = False
					roomlist[4] = True
					move = move - 1
					print(move)
			while roomlist[2] == True:
				thirdmove = input('Which room do you choose? Front or right? ')
				if str.lower(thirdmove) == 'front':
					roomlist[2] = False
					roomlist[4] = True
					move = move - 1
					print(move)
				elif str.lower(thirdmove) == 'right':
					roomlist[2] = False
					roomlist[0] = True
					move = move - 1
					print(move)
			while roomlist[3] == True:
					print('You are stuck and are forced back!')
					roomlist[3] = False
					roomlist[0] = True
					move = move - 1
					print(move)
			while roomlist[4] == True:
				fifthmove = input('Would you like to proceed front, back, or right? ')
				if str.lower(fifthmove) == 'front':
					roomlist[4] = False
					roomlist[5] = True
					move = move - 1
					print(move)
				elif str.lower(fifthmove) == 'back':
					roomlist[4] = False
					roomlist[2] = True
					move = move - 1
					print(move)
				elif str.lower(fifthmove) == 'right':
					roomlist[4] = False
					roomlist[1] = True
					move = move - 1
					print(move)
			while roomlist[5] == True:
				sixthmove = input('Would you like to proceed left or back? ')
				if str.lower(sixthmove) == 'left':
					roomlist[5] == False
					roomlist[6] == True
					print("You escape!!!! ")
					move = 0
					break
				if str.lower(sixthmove) == 'back':
					roomlist[5] == False
					roomlist[4] == True
					move = move - 1
					print(move)				
			while roomlist[6] == True:
				roomlist[6] == False
				move = 0		
		x = input('Would you like to try again? y/n ')










andrew_adventure()