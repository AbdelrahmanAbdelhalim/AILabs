import random as rand
import itertools

def genRandomNumbers():
	ls = [rand.randint(1,13) for i in range(4)]
	return ls

def findPermutations(ls):
	return list(itertools.permutations(ls))


def solve(ls,operation):	
	if len(ls) > 1:
		for l in range(len(ls)):
			for r in range(len(ls)):
				if l == r:
					continue
				newLs = []
				for j in range(len(ls)):
					if j != l and j!= r:
						newLs.append(ls[j])

				newLs.append(ls[l] + ls[r])
				operation.append("plus")
				solve(newLs,operation)
				newLs = newLs[:-1]
				operation = operation[:-1]

				newLs.append(ls[l] - ls[r])
				operation.append("minus")
				solve(newLs,operation)
				newLs = newLs[:-1]
				operation = operation[:-1]

				newLs.append(ls[l] * ls[r])
				operation.append("mul")
				solve(newLs,operation)
				newLs = newLs[:-1]
				operation = operation[:-1]

				if ls[r] != 0:
					newLs.append(ls[l] / ls[r])
					operation.append("divide")
					solve(newLs,operation)
					newLs = newLs[:-1]
					operation = operation[:-1]
	if len(ls) == 1:
		if abs(ls[0] - 24) < 0.0000001:
			print("found solution")
		else:
			print(operation)

if __name__ == "__main__":
	foo = genRandomNumbers()
	print(foo)
	solve(foo,[])
