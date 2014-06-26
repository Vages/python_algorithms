''' 
A solution to task 4-3 in the book: Given a connected (implicitly undirected) graph G 
representing your friends, find the maximum number of friends that can attend a party
where everyone knows at least K other people.
'''

def maxParty(G, K): 
	count = dict((u, 0) for u in G)		# Create an empty count dictionary
	
	for u in G:
		for v in G[u]:
			count[u] += 1		# Count the number of friends each node has

	Q = [u for u in G if count[u] < K]	# A dictionary of all nodes that already have less than K friends
	S = [u for u in G] 			# A copy of all nodes in the original G dictionary; the solution set
	
	while Q:				# As long as there are unprocessed nodes with too few friends
		u = Q.pop()			# Take a node that has too few friends 
		S.remove(u)			# Remove it from the solution set
		for v in G[u]:			# For each friend v, decrease their friend count, now that u is gone.
			count[v] -= 1
			if count[v] == K-1:	# Should a node reach a count below K, add this to Q
				Q.append(v)

	return S

def main():
	a, b, c, d, e = range(5)
	G = {a:[b, c], b:[a, c], c:[a, b, e], d:[e], e:[c, d]}
	print(maxParty(G, 2))

if __name__ == '__main__':
		main()	