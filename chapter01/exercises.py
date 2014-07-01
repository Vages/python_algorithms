# 1-1
'''I do not find this true. That is because: As computers get faster and
cheaper, the problems they solve are getting progressively more complex
and hard. Thus, relying on this to save us will not work.'''

# 1-2
import re

def extractAlphabeticCharacters(inputString):
	outputString = ""

	for char in inputString:
		if char.isalpha():
			outputString = outputString + char

	return outputString

def countLetterOccurrences(inputString):
	# Note: this is actually my own implementation of a simple collections.Counter()!
	occurrenceDict = dict()

	for char in inputString:
		if char in occurrenceDict:
			occurrenceDict[char] = occurrenceDict[char] + 1

		else:
			occurrenceDict[char] = 1

	return occurrenceDict

def isAnagrams(string1, string2):
	string1 = string1.lower()
	string2 = string2.lower()

	string1occurrences = countLetterOccurrences(string1)
	string2occurrences = countLetterOccurrences(string2)

	string1keyList = string1occurrences.keys()
	string1keyList.sort()
	string2keyList = string2occurrences.keys()
	string2keyList.sort()

	if string1keyList != string2keyList:
		return False

	else:
		for key in string1keyList:
			if string1occurrences[key] != string2occurrences[key]:
				return False

		return True

def main():
	string1 = "Agnes i senga"
	string2 = "Senga i Agnes!"

	string1 = extractAlphabeticCharacters(string1)
	string2 = extractAlphabeticCharacters(string2)

	print(isAnagrams(string1, string2))

main()

''' I think this solution scales quite well, but I am not certain of it.
The process of extracting alphabetic characters should be linear 
(unless appending to the string has some enormous overhead).
The hashing process involved in counting letter occurences should have
a linear cost as well. Sorting the key list has an a*log(a) running time,
but this sorting operation will never scale beyond a=26 because the size
of the hash table will never exceed the number of characters in the 
alphabet. '''

