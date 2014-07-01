# NOT FINISHED

'''s is the node currently explored, p is the predecessor, B are the Balance factors, d is a dictionary of depth'''

def balanceFactors(G, s, B=None, D=None, p=None): 
	if B == None:
		B = {}

	if D == None:
		D = {}

	if p == None:
		D[s] = 0
	else:
		D[s] = D[p] + 1

	if len(G[s]) > 0:
		for v in G[s]:
			balanceFactors(G, v, B, D, s)

		B[s] = D[G[s][0]] - D[G[s][1]]

		return B

	else:
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

if __name__ == '__main__':
	main()