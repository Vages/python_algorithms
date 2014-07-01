# A solution to task 4-20 in the book

def balanceFactors(G, s, d=0, B=None, MD=None): 		# G must be a full binary tree, two children except for leaf nodes
	if B == None:
		B = {}						# Dict for balance factors; negative means more on right

	if MD == None:
		MD = {}						# Dict for max depth of nodes subtrees (the lowest depth of leaf nodes)

	d += 1 							# Increase depth

	if len(G[s]) > 0:					# If not a leaf node ...
		for v in G[s]:
			balanceFactors(G, v, d, B, MD)		# Run function recursively on its children
		leftChild = G[s][0]
		rightChild = G[s][1]

		B[s] = MD[leftChild] - MD[rightChild]		# The balance factor is calculated from the deepest of left to deepest of right.
		MD[s] = max(MD[leftChild], MD[rightChild])	# The max depth of this node

		return B

	else:
		MD[s] = d					# Max depth is the depth of this leaf node
		B[s] = 0

def main():
	G = {u:[] for u in range(0,21)}
	G[0] = [1,2]
	G[1] = [3,4]
	G[2] = [5,6]
	G[4] = [7,8]
	G[5] = [9,10]
	G[6] = [11,12]
	G[7] = [13,14]
	G[9] = [15,16]
	G[10] = [17,18]
	G[12] = [19,20]

	print(balanceFactors(G, 0))
	# All nodes x should have B[x] == 0, except B[1] == -2, B[4] == 1, and B[6] == -1

if __name__ == '__main__':
	main()