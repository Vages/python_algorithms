def naive_max_perm(M, A=None): #Listing 4-5
	if A is None:
		A = set(range(len(M)))
	if len(A) == 1: return A
	B = set(M[i] for i in A)
	C = A - B
	if C:
		A.remove(C.pop())
		return naive_max_perm(M, A)
	return A

def max_perm(M):
	n = len(M)
	A = set(range(n))
	count = [0]*n
	for i in M:
		count[i] += 1
	Q = [i for i in A if count[i] == 0]
	while Q:
		i == Q.pop()
		A.remove(i)
		j = M[i]
		count[j] -= 1
		if count[j] == 0:
			Q.append(j)
	return A

def main():
	M =  [2, 2, 0, 5, 3, 5, 7, 4]
	print(naive_max_perm(M))
	print(max_perm(M))

if __name__ == '__main__':
	main()