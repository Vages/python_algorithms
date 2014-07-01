import randomDAG

'''
Made as a solution to task 4-19.
It would be possible to redesign topsort to use the last node,
but this would require maintaining a separate array. I interpreted
the task in a bit of a creative way: by reversing the edges, you are really
selecting the last node when you are selecting the first.
'''

def topsortLastNode(G):
	reversedEdges = reverseGraphDict(G)

	print(reversedEdges)

	result = topsort(reversedEdges)
	
	result.reverse()

	return result

def topsort(G): # Taken from the book
	count = {u:0 for u in G}

	for u in G:
		for v in G[u]:
			count[v] += 1

	Q = [u for u in G if count[u] == 0]
	S = []

	while Q:
		u = Q.pop()
		S.append(u)
		for v in G[u]:
			count[v] -= 1
			if count[v] == 0:
				Q.append(v)

	return S


def reverseGraphDict(G):
	H = {u:[] for u in G}

	for u in G:
		for v in G[u]:
			H[v].append(u)

	return H

def main():
	a = randomDAG.randomDAGdict(6)
	print(a)
	b = topsortLastNode(a)
	print(b)

if __name__ == '__main__':
	main()