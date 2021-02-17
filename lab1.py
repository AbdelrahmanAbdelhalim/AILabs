import random as rand
import itertools

solutionsV = []
solutionsS = []

def genRandomNumbers():
	ls = [rand.randint(1,13) for i in range(4)]
	return ls

def findPermutations(ls):
	return list(itertools.permutations(ls))


def solve24(permutation):
	permutations = findPermutations(foo)
	for permutation in permutations:
		solve(permutation,0,[],[])
	# for permutation in permutations:
	# 	solve(permuatation[1:],ls[0])

def solve(ls,total,values,signs):
	if len(ls) == 0:
		if total == 24:
			print("found solution")
			solutions.append(values)
			solutions.append(signs)
		return

	solve(ls[1:],total + ls[0],values.append(total),signs.append("+"))
	if ls[0] != 0:
		solve(ls[1:],total / ls[0],values.append(total),signs.append("/"))
	solve(ls[1:],total * ls[0],values.append(total),signs.append("x"))
	solve(ls[1:],total - ls[0],values.append(total),signs.append("-"))



if __name__ == "__main__":
	foo = genRandomNumbers()
	solve24(foo)
