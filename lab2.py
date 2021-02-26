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

def calculateHeuristic(ls,depth):
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
	heuristic += manDistance
	heuristic += depth
	return heuristic

def calculateInversions(ls):
	inversions = 0
	for l in range(len(ls)):
		for r in range(l,len(ls)):
			if ls[l] != 0 and ls[r] != 0:
				if ls[l] > ls[r]:
					inversions += 1
	return inversions
	
def solvableGame(numOfInversions):
	return numOfInversions % 2 == 0

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

def solve(ls,depth,closedNodes,goal = [1,2,3,4,5,6,7,8,0]):
	zeroIndex = None
	closedNodes.append(ls)
	validLists = []
	printBoard(ls)
	if ls != goal and solvableGame(calculateInversions(ls)):
		for i in range(len(ls)):
			if ls[i] == 0:
				zeroIndex = i
		ls1 = ls.copy()

		# Move Left
		if (zeroIndex + 1)  % 3 != 1 :
			swapValuesInList(ls1,zeroIndex,zeroIndex - 1)
			if ls1 not in closedNodes:
				validLists.append(ls1)
		# Move Right
		ls2 = ls.copy()
		if (zeroIndex + 1) % 3 != 0:
			swapValuesInList(ls2,zeroIndex,zeroIndex + 1)
			if ls2 not in closedNodes:
				validLists.append(ls2)
		# Move Up
		ls3 = ls.copy()
		if zeroIndex - 3 >= 0:
			swapValuesInList(ls3,zeroIndex,zeroIndex - 3)
			if ls3 not in closedNodes:
				validLists.append(ls3)

		# Move Down
		ls4 = ls.copy()
		if zeroIndex + 3 < len(ls):
			swapValuesInList(ls4,zeroIndex,zeroIndex + 3)
			if ls4 not in closedNodes:
				validLists.append(ls4)

		validLists = sorted(validLists,key = lambda x: calculateHeuristic(x,depth))
		print(len(closedNodes))
		depth += 1
		solve(validLists[0],depth,closedNodes)


if __name__ == '__main__':
	foo = createGame()
	printBoard(foo)
	solve(foo,0,[])
	print()
	print("initial State:")
	printBoard(foo)
	# print(calculateInversions([5,2,8,4,1,7,3,6]))
	# print(solvableGame(calculateInversions([1,2,3,7,6,5,0,4,8])))
	
