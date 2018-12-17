# Created by Guru Sarath
# 16 December 2018

def minimaxDecision(gameState, depth = float('inf')):

	nextStates = gameState.nextGameStates

	maxValue = float('-inf')
	nextBestState = None

	#print(nextStates)

	for state in nextStates:
		valFromTreeBelow = minValue(state, depth - 1)
		#print(state, valFromTreeBelow)

		if valFromTreeBelow > maxValue:
			maxValue = valFromTreeBelow
			nextBestState = state

	#print(maxValue)

	return nextBestState


def minValue(gameState, depth = float('inf')):

	if gameState.isTerminal:
		#gameState.printGameState()
		#print('Min',gameState.utility)
		return gameState.utility
	elif depth == 0:
		#gameState.printGameState()
		#print('Min',gameState.utility)
		return gameState.utility


	nextStates = gameState.nextGameStates

	minValueX = float('inf')

	for state in nextStates:

		valFromTreeBelow = maxValue(state,depth-1)

		if valFromTreeBelow < minValueX:
			minValueX = valFromTreeBelow 

	return minValueX




def maxValue(gameState, depth = float('inf')):
	if gameState.isTerminal:
		#gameState.printGameState()
		#print('Max',gameState.utility)
		return gameState.utility
	elif depth == 0:
		#gameState.printGameState()
		#print('Max',gameState.utility)
		return gameState.utility

	nextStates = gameState.nextGameStates

	maxValueX = float('-inf')

	for state in nextStates:

		valFromTreeBelow = minValue(state,depth-1)

		if valFromTreeBelow > maxValueX:
			maxValueX = valFromTreeBelow 

	return maxValueX