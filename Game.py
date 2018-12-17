# Created By Guru Sarath
# 16 Dec 2018

"""

#Only 2 player Games
class game:

	self.CurrentPlayer - 0 ot 1 - [0-Computer; 1-Human]

	def __init__(self,CurrentBoardState, CurrentPlayer):

	def nextPlayer(self):
		return nextPlayer [0 or 1]

	def nextGameStates(self):
		return list_Of_nextGameState (list of objects of type game)

"""

import copy


class TicTacTo:


	CurrentBoardState = [[' ', ' ', ' '],[' ', ' ', ' '],[' ', ' ', ' ']]

	player0_Symbol = 'X' #Computer
	player1_Symbol = 'O' #User
	CurrentPlayer = 0
	Winner = 'None'


	def __init__(self, CurrentBoardState = [[' ', ' ', ' '],[' ', ' ', ' '],[' ', ' ', ' ']],CurrentPlayer = 0):
		self.CurrentPlayer = CurrentPlayer
		self.CurrentBoardState = CurrentBoardState

	@property
	def openingBook(self):
		#return TicTacTo([[' ', ' ', ' '],[' ', 'X', ' '],[' ', ' ', ' ']], self.nextPlayer)
		return False

	@property
	def nextPlayer(self):
		if self.CurrentPlayer == 0: 
			return 1
		else: 
			return 0

	@property
	def placePlayerSymbol(self):
		if self.CurrentPlayer == 0: 
			return self.player0_Symbol
		else: 
			return self.player1_Symbol


	@property
	def GameStatus(self):

		for i in range(3):
			if self.CurrentBoardState[i][0] == self.CurrentBoardState[i][1] == self.CurrentBoardState[i][2]:

				if self.CurrentBoardState[i][0] == self.player0_Symbol:
					return self.player0_Symbol
				elif self.CurrentBoardState[i][0] == self.player1_Symbol:
					return self.player1_Symbol

			if self.CurrentBoardState[0][i] == self.CurrentBoardState[1][i] == self.CurrentBoardState[2][i]:

				if self.CurrentBoardState[0][i] == self.player0_Symbol:
					return self.player0_Symbol
				elif self.CurrentBoardState[0][i] == self.player1_Symbol:
					return self.player1_Symbol

		if self.CurrentBoardState[0][0] == self.CurrentBoardState[1][1] == self.CurrentBoardState[2][2]:

			if self.CurrentBoardState[0][0] == self.player0_Symbol:
				return self.player0_Symbol
			elif self.CurrentBoardState[0][0] == self.player1_Symbol:
				return self.player1_Symbol				

		if self.CurrentBoardState[0][2] == self.CurrentBoardState[1][1] == self.CurrentBoardState[2][0]:
				
			if self.CurrentBoardState[0][2] == self.player0_Symbol:
				return self.player0_Symbol
			elif self.CurrentBoardState[0][2] == self.player1_Symbol:
				return self.player1_Symbol


		for rowX in self.CurrentBoardState:
			for boxX in rowX:
				if boxX == ' ':
					return 'Game_in_Progress'

		return 'Tie'


	@property
	def nextGameStates(self):

		nextGameStates_List = []

		rowNum = 0
		for RowX in self.CurrentBoardState:

			colNum = 0
			for BoxX in RowX:
				if BoxX == ' ':
					nextBoardX = copy.deepcopy(self.CurrentBoardState)
					nextBoardX[rowNum][colNum] = self.placePlayerSymbol
					nextGameStates_List.append(TicTacTo(nextBoardX, self.nextPlayer))
					#nextGameStates_List.append(nextBoardX)

				colNum += 1

			rowNum += 1

		return nextGameStates_List


	@property
	def heuristicValue(self):

		#print('--')

		numberOfWinsForPlayer_0 = 0
		numberOfWinsForPlayer_1 = 0

		rowNum = 0
		for rowX in self.CurrentBoardState:
			colNum = 0
			for boxX in rowX:
				if boxX == ' ':
					nextStateHypotheticalState = copy.deepcopy(self.CurrentBoardState)
					nextStateHypotheticalState[rowNum][colNum] = self.player0_Symbol
					nextStateHypotheticalState = TicTacTo(nextStateHypotheticalState)

					if nextStateHypotheticalState.GameStatus == self.player0_Symbol:
						numberOfWinsForPlayer_0 += 1

					nextStateHypotheticalState = copy.deepcopy(self.CurrentBoardState)
					nextStateHypotheticalState[rowNum][colNum] = self.player1_Symbol
					nextStateHypotheticalState = TicTacTo(nextStateHypotheticalState)

					if nextStateHypotheticalState.GameStatus == self.player1_Symbol:
						numberOfWinsForPlayer_1 += 1
				colNum += 1
			rowNum += 1

			#print('END--')

		return numberOfWinsForPlayer_0 - numberOfWinsForPlayer_1
	

	@property
	def isTerminal(self):
		if self.GameStatus != 'Game_in_Progress':
			return True
		else:
			return False

	@property
	def utility(self):
		if self.GameStatus == self.player1_Symbol:
			return float('-inf')
		elif self.GameStatus == self.player0_Symbol:
			return float('inf')
		else:
			return self.heuristicValue


	def printGameState(self):

		print('----+---+----')
		for rowX in self.CurrentBoardState:
			print('|', end='')
			for BoxX in rowX:
				print(' '+ BoxX + ' |', end='')
			print('\n----+---+----')

	def __str__(self):
		self.printGameState()
		return ''

	def humanPlayerInput(self):
		#print('Your turn :)')
		rowNum = input('Row Number - ')
		colNum = input('Col Number - ')

		if int(rowNum) > 3 or int(rowNum) < 1 or int(colNum) > 3 or int(colNum) < 1:
			print('Invalid Move')
			return None

		if self.CurrentBoardState[int(rowNum)-1][int(colNum) -1] == ' ':
			nextState = copy.deepcopy(self.CurrentBoardState)
			nextState[int(rowNum)-1][int(colNum)-1] = self.player1_Symbol
			return TicTacTo(nextState, self.nextPlayer)
		else:
			print('Invalid Move')
			return None



if __name__ == '__main__':

	T1 = TicTacTo([['O', 'O', 'X'], ['X', ' ', 'O'], ['O', 'O', 'X']])
	#T1 = TicTacTo()

	print(T1.printGameState())