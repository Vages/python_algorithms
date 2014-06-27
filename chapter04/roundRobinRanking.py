'''A solution to task 4-5:

Remember the knights in Chapter 3? After their first tournament, 
which was a round-robin tournament, where each knight jousted one 
of the other, the staff wants to create a ranking. They realize it 
might not be possible to create a unique ranking or even a proper 
topological sorting (because there may be cycles of knights defeating
each other), but they have decided on the following solution: 
order the knights in a sequence K1, K2, ... , Kn, where 
K1 defeated K2, K2 defeated K3, and so forth (Ki–1 defeated Ki, for i=2...n). 

Prove that it is always possible to construct such a sequence 
by designing an algorithm that builds it.
'''

'''
First of all, this is possible to prove by recursion:

Say that we already have a number of knights that have been ordered this way, 
and we want to insert a new knight X, which has a list of opponents that he 
has defeated. Beginning from the start, we find the first knight that this 
knight has defeated and insert this knight before that one. This is completely
safe, because if a knight is not in Xs list of defeated opponents, then he is
(by our knowledge of the problem) in theirs.
'''

def roundRobingRanking(G):
	# G is a complete, directed graph, representing the victories in the round-robin tournament

	Q = set(G.keys())		# Create a set of candidates from the keys of the dictionary

	S = [Q.pop()]			# Fill the array with a set of candidates

	while Q:
		X = Q.pop()			# Pick a random element from the set of candidates

		for i in range(len(S)):		# Go through the earlier solution looking for a suitable place
			if S[i] in G[X]:
				S.insert(i, X)
				break
		else:
			S.append(X)		# If it had not defeated any of the previous, insert at end.

	return S

def main():
	a, b, c, d = range(4)
	G = {a:[b, c, d], b:[c, d], c:[], d:[c]}
	print(roundRobingRanking(G))


if __name__ == '__main__':
	main()
