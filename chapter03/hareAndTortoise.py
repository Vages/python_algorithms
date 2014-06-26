from random import randrange
from math import ceil

def hareGuess(pickSize): # selects a number and guesses it by bisecting
	number = randrange(pickSize) # Pick a random number
	min = 0
	max = pickSize # The first number that is too great
	ops = 0

	while True:
		if (min + 1) >= max: # We've narrowed it down to one possible number
			break
		else: 
			halfWay = min + ceil((max-min)/2)
			if number < halfWay:
				max = halfWay
			else: 
				min = halfWay
		ops += 1


	print "Generated number:", number
	print "Guess:", min
	print "Operations:", ops


def tortoiseGuess(pickSize):
	number = randrange(pickSize)

	for i in range(pickSize):
		if i == number:
			print "Generated number:", number
			print "Guess:", i 
			break

def main():
	for i in range(0, 10):
		hareGuess(10)

if __name__ == '__main__':
	main()