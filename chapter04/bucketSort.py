# Answer to exercise 4-12
# Assumes that the values are evenly distributed in the [0-1) interval

def bucketSort(floatList, n=10):
	bucket = [[] for i in range(n)] 	# Create 10 empty buckets
	
	for i in floatList:
		bucket[int(i*n)].append(i)	# Place in bucket according to first digit

	for b in bucket:
		b.sort()			# Sort each bucket in place

	result = []				# Empty result array for concatenation

	for sortedBucket in bucket:
		result = result + sortedBucket	# Append each bucket to result in order

	return result

def main():
	A = [0.78, 0.17, 0.39, 0.26, 0.72, 0.94, 0.21, 0.12, 0.23, 0.68]
	print(bucketSort(A))

if __name__ == '__main__':
	main()