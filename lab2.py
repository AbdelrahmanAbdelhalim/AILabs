import random as rand

"""
	createGame():
		creates a solvable 8 game puzzle by random
		Not very efficiend, maybe needs a fix
"""
def createGame():	
	#Odd inversions means unsolvable
	#Create Puzzle with even inversions
	ls = []
	available = [i for i in range(1,9)]
	for i in range(8):
		nww = rand.randint(0,len(available) - 1	)
		ls.append(available[nww])
		available.pop(nww)
	ls.append(0)
	inversions = calculateInversions(ls)
	if solvableGame(inversions):
		return ls
	else:
		return createGame()

def calculateHeuristic(ls):
	heuristic = 0
	manDistance = 0
	for i in range(len(ls)):
		if ls[i] == 0:
			continue
		if i + 1 != ls[i]:
			heuristic += 1
	for i in range(len(ls)):
		if ls[i] == 0 :
			continue
		goalSquare = ls[i] - 1
		diffY = abs((int(i/3) - int(goalSquare/3)))
		diffX = abs((i%3 - goalSquare%3))
		manDistance += (diffX + diffY)
	print(manDistance)
	heuristic += manDistance
	return heuristic
def calculateInversions(ls):
	inversions = 0
	for foo in range(len(ls)):
		for lee in range(foo,len(ls)):
			if ls[foo] == 0 or ls[lee] == 0:
				continue
			if ls[lee] < ls[foo]:
				inversions += 1
	return inversions
	
def solvableGame(numOfInversions):
	if numOfInversions % 2 == 0:
		return True
	else:
		return False

def printBoard(ls):
	for k in range(len(ls)):
		if k % 3 == 0:
			print()
		print(ls[k],end = ' ')
	print()
def swapValuesInList(ls,index1,index2):
	placeHolder = ls[index1]
	ls[index1] = ls[index2]
	ls[index2] = placeHolder

def solve(ls,solutions,closedNodes):
	zeroIndex = None
	validLists = []
	heuristicValues = []
	if calculateInversions(ls) != 0:
		for i in range(len(ls)):
			if ls[i] == 0:
				zeroIndex = i
		ls1 = ls.copy()
		if zeroIndex - 1 >= 0:
			swapValuesInList(ls1,zeroIndex,zeroIndex - 1)
			printBoard(ls1)
			ls1Heur = calculateHeuristic(ls1)
			validLists.append(ls1)
			heuristicValues.append(ls1Heur)

		ls2 = ls.copy()
		if zeroIndex + 1 < len(ls):
			swapValuesInList(ls2,zeroIndex,zeroIndex + 1)
			printBoard(ls2)
			ls2Heur = calculateHeuristic(ls2)
			validLists.append(ls2)
			heuristicValues.append(ls2Heur)

		ls3 = ls.copy()
		if zeroIndex - 3 >= 0:
			swapValuesInList(ls3,zeroIndex,zeroIndex - 3)
			printBoard(ls3)
			ls3Heur = calculateHeuristic(ls3)
			validLists.append(ls3)
			heuristicValues.append(ls3Heur)

		ls4 = ls.copy()
		if zeroIndex + 3 < len(ls):
			swapValuesInList(ls4,zeroIndex,zeroIndex + 3)
			printBoard(ls4)
			ls4Heur = calculateHeuristic(ls4)
			validLists.append(ls4)
			heuristicValues.append(ls4Heur)
		minHeursitic = 1000
		minHeursiticIndex = 0
		for i in range(len(heuristicValues)):
			if heuristicValues[i] < minHeursitic:
				minHeursiticIndex = i
		# solve(validLists[minHeursiticIndex],solutions)

if __name__ == '__main__':
	foo = createGame()
	printBoard(foo)
	boards = []
	closed = [foo]
	solve(foo,boards,closed)
	
