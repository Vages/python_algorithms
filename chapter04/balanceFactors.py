def balanceFactors(G, s, B=None, D=None, MD=None, p=None): 	# G must be a full binary tree, two children except for leaf nodes
	if B == None:
		B = {}						# Dict for balance factors; negative means more on right

	if D == None:
		D = {}						# Dict for depth of nodes; root = 0

	if MD == None:
		MD = {}						# Dict for max depth of nodes subtrees (the lowest depth of leaf nodes)

	if p == None:
		D[s] = 0					# If no parent, this is root node, depth = 0
	else:
		D[s] = D[p] + 1 				# Else, depth of parent +1

	if len(G[s]) > 0:					# If not a leaf node ...
		for v in G[s]:
			balanceFactors(G, v, B, D, MD, s)	# Run function recursively on its children
		leftChild = G[s][0]
		rightChild = G[s][1]

		B[s] = MD[leftChild] - MD[rightChild]		# The balance factor is calculated from the deepest of left to deepest of right.
		MD[s] = max(MD[leftChild], MD[rightChild])	# The max depth of this node

		return B

	else:
		MD[s] = D[s]					# Max depth is the depth of this leaf node
		# Note: It is possible to insert a B[D] = 0 here. I have removed it, for the sake of brevity

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

if __name__ == '__main__':
	main()