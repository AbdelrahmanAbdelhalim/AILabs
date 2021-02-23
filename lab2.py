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


def calculateInversions(ls):
	inversions = 0
	for foo in range(len(ls)):
		for lee in range(foo,len(ls)):
			if ls[foo] == 0 or ls[lee] == 0:
				continue
			if ls[lee] < ls[foo]:
				inversions += 1
	return inversions
def findHeuristicValeu(ls):
	
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

if __name__ == '__main__':
	foo = createGame()
	printBoard(foo)
	# solvePuzzle(foo)