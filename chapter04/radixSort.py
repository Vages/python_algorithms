# An implementation of radix sort, an answer to 4-11 in the book

def radixSort(intList, sort="asc"):
	maxLen = 0					# The maxmimum length of any integer string
	binaries = []					# An array of integers, converted to base 2
	
	for integer in intList:
		binString = bin(integer)		# Convert integer to binary
		cutString = binString[2:]		# Cut away the "0b" part at the start
		if len(cutString) > maxLen:
			maxLen = len(cutString)		# If it is longer than any string yet, update maxLen
		binaries.append(cutString)


	for i in range(len(binaries)):
		binaries[i] = binaries[i].zfill(maxLen) # Pad converted strings with zeroes

	for i in range(maxLen):
		# Make two arrays that will contain each 

		zeroes = [] 
		ones = []

		for item in binaries:
			if item[-(i+1)] == "1":		# Sort them on the ith least significant digit
				ones.append(item)
			else:
				zeroes.append(item)
		if sort == "asc":
			binaries = zeroes + ones	# Sort ascending	
		else:
			binaries = ones + zeroes	# Sort descending

	for i in range(len(binaries)):
		binaries[i] = int(binaries[i], 2)	# Convert binary strings back to integers

	return binaries

def main():
	a = [203, 18478, 837, 9787, 13, 1]
	print(radixSort(a))
	print(radixSort(a, "desc"))

if __name__ == '__main__':
	main()