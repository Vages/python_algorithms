# Not yet finished

def dfsFinishTime(G, s):
	S, D, F, Q = set(), [s], [], [] # S are Seen, D are times of discovery, F are Finish times, Q is a Queue
	
	S.add(s)
	Q.append((s, None))
	for v in G[s]:
		Q.append((s, v))

	while Q:
		u,v = Q.pop()

		if v == None:
			F.append(u)
		else:
			if v in S: continue
			S.add(v)
			Q.append((v, None))
			D.append(v)
			for w in G[v]:
				Q.append((v, w))
			

	return D, F
	

def main():
	a, b, c, d, e, f, g = range(7)
	G = {a:[b, c], b:[a, d, e], c:[a, f, g], d:[b], e:[b, f], f:[c, e], g:[c]}

	disc, fin = dfsFinishTime(G, a)

	print(disc)
	print(fin)

if __name__ == '__main__':
	main()