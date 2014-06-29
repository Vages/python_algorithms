'''
A solution to task 4-4 in the book: 

A node is called central if the greatest (unweighted) distance from that node to any other 
in the same graph is minimum. That is, if you sort the nodes by their greatest distance to 
any other node, the central nodes will be at the beginning. Explain why an unrooted tree has 
either one or two central nodes, and describe an algorithm for finding them.
'''

def centralNodes(G):
	count = dict((u, 0) for u in G)		# Create an empty count dictionary
	


	for u in G:
		for v in G[u]:
			count[u] += 1		# Count the number of neighbors each node has

	Q = [u for u in G if count[u] == 1]	# A dictionary of all nodes that are leaf nodes
	S = [u for u in G] 			# A copy of all nodes in the original G dictionary; the solution set
	
	if len(S) <= 2:
		return S

	hasLeafNodes = True

	while hasLeafNodes:
		R = []					# A list of candidates for the next round

		while Q:				# As long as there are unprocessed nodes with too few friends
			u = Q.pop()			# Take a node that has too few friends 
			S.remove(u)			# Remove it from the solution set
			for v in G[u]:			# For each friend v, decrease their friend count, now that u is gone.
				count[v] -= 1
				if count[v] == 1:	# Should a node reach a count below K, add this to Q
					R.append(v)

		if len(S) > 2:
			Q = R[:]
		else:
			hasLeafNodes = False
	
	return S

def main():
	x, y = range(2)
	H = {y:[x], x:[y]}
	print(centralNodes(H))

	a, b, c, d, e, f, g, h, i = range(9)
	G = {a:[d], b:[d], c:[d], d:[a, b, c, g], e:[g, i], f:[g], g:[d, e, f, h], h:[g], i:[e]}
	print(centralNodes(G))

if __name__ == '__main__':
		main()	