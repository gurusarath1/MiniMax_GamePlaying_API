# Created by Guru Sarath
# 16 DEcember 2018


import Game
import AdverserialSearch

screeOutput_tie = '''
+-----------------------------+
|                             |
|        Tie                  |
|                             |
+-----------------------------+
'''

screeOutput_youWin = '''
+-----------------------------+
|                             |
|        Your Win             |
|                             |
+-----------------------------+
'''

screeOutput_youLose = '''
+-----------------------------+
|                             |
|        Your Lose            |
|                             |
+-----------------------------+
'''

def play(Game, depth = float('inf')):

	GameX = Game

	steps = 0

	while not GameX.isTerminal:

		#print('-------------------------')

		GameX.printGameState()

		if GameX.CurrentPlayer == 0:
			print('Computer\'s Turn\nThinking...')
			if steps == 0 and GameX.openingBook:
				GameX = GameX.openingBook
			else:
				#print('Here')
				GameX = AdverserialSearch.minimaxDecision(GameX, depth)
		elif GameX.CurrentPlayer == 1:
			print('Your Turn')
			PrevGameX = GameX
			GameX = GameX.humanPlayerInput()

			while not GameX:
				GameX = PrevGameX.humanPlayerInput()

		steps += 1

	GameX.printGameState()
	if GameX.utility == float('-inf'):
		print(screeOutput_youWin)
	elif GameX.utility == float('inf'):
		print('Computer Wins')
		print(screeOutput_youLose)
	else:
		print(screeOutput_tie)

	input('press enter')

if __name__ == '__main__':
	player = input('Do you want to start first ? \n[0-No ; 1-Yes]')

	TicTacToGame = None

	if player == '0' or player == '1':
		TicTacToGame = Game.TicTacTo([[' ', ' ', ' '],[' ', ' ', ' '],[' ', ' ', ' ']],int(player))
		play(TicTacToGame, 4)
	else:
		player = input('Invalid Input \n Press Enter to exit')

