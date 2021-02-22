def createGame():	
	#Odd inversions means unsolvable
	#Create Puzzle with even inversions
	numTaken = [1 for i in range(8)]


def calculateInversions(ls):
	inversions = 0
	for foo in range(len(ls)):
		for lee in range(foo,len(ls)):
			if lee < foo:
				inversions += 1
	return inversions

def solvableGame(numOfInversion):
	if numOfInverions % 2 == 0:
		return True
	else:
		return False



if __name__ == '__main__':
	foo = createGame()
	# solvePuzzle(foo)