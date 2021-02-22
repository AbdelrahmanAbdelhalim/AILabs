import random as rand
import itertools
import time

"""
genRandomNumbers(minn, maxx,range):
	Generate <<rangee>> Random numbers between minn and maxx 
solve(ls,operation,target):
	Finds the operations needed to reach the target sum using the numbers in ls
	uses DFS to find the answer.
	Works by brute forcing through every pair of numbers and performing the 4 arithmetic calculations
	on them and then appending the result to the end of the array, then recursively calling the function
	on the newly generated array.

"""
def genRandomNumbers(minn = 1,maxx = 13,rangee = 4):
	ls = [rand.randint(minn,maxx) for i in range(rangee)]
	return ls
def solve(ls,operation,target):	
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
				operation.append(str(ls[l]) + " plus " + str(ls[r]))
				solve(newLs,operation,target)
				newLs = newLs[:-1]
				operation.pop()

				newLs.append(ls[l] - ls[r])
				operation.append(str(ls[l]) + " minus " + str(ls[r]))
				solve(newLs,operation,target)
				newLs = newLs[:-1]
				operation.pop()

				newLs.append(ls[l] * ls[r])
				operation.append(str(ls[l]) + " mul " + str(ls[r]))
				solve(newLs,operation,target)
				newLs = newLs[:-1]
				operation.pop()

				if ls[r] != 0:
					newLs.append(ls[l] / ls[r])
					operation.append(str(ls[l]) + " divide " + str(ls[r]))
					solve(newLs,operation,target)
					newLs = newLs[:-1]
					operation.pop()
	if len(ls) == 1:
		if abs(ls[0] - target) < 0.0000001:
			print(operation)

if __name__ == "__main__":
	start = time.time()
	foo = genRandomNumbers(1,13,4)
	print(foo)
	solve(foo,[],24)
	end = time.time()
	print(f"Running time of Algorithm: {end - start}")
