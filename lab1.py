import random as rand

def genRandomNumbers():
	ls = []
	for i in range(4):			
		x = rand.randint(1,13)
		ls.append(x)
	return ls

def solve24(ls):
		

if __name__ == "__main__":
	foo = genRandomNumbers()
	print(foo)