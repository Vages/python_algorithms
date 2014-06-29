# Partially a solution to task 4-18. Currently it generates random DAG.
# I have not yet found a proper way to check whether a topological 
# sort generates a valid DAG.

from random import randint, shuffle

def randomDAGmatrix(n):	
	# Generates a n*n matrix with only "forward pointing edges"
	# Guarantees that all nodes will have at least one forward pointing edge.

	matrix = [[0]*n for i in range(n)]

	for i in range(n-1):
		for j in randomIntArray(i+1, n):		# See function below
			matrix[i][j] = 1
	
	return matrix

def randomDAGdict(n):
	randDict = {}

	for b in range(n):
		randDict[b] = []				# Fill with empty arrays

	for i in range(n-1):
		randDict[i] = randomIntArray(i+1, n)
		randDict[i].sort()

	return randDict

def randomIntArray(start, stop):
	# Gives a random array of numbers from start and up to (but not including) stop.
	# The number of elements is selected randomly
	
	noOfElements = randint(1, stop-start)

	selectable = [a for a in range(start, stop)]
	shuffle(selectable)

	theNumbers = []

	for i in range(noOfElements):
		theNumbers.append(selectable.pop())

	return theNumbers

def main():
	a = randomDAGmatrix(6)
	for i in a:
		print(i)

	b = randomDAGdict(6)
	print(b)

if __name__ == '__main__':
	main()
