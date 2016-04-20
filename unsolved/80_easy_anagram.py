from sys import exit

"""
Challenge
* https://www.reddit.com/r/dailyprogrammer/comments/x0v3e/7232012_challenge_80_easy_anagrams/
* What is the largest anagram family in the dictionary I supplied? What is the second largest?

Status
* it's hackish code - needs polish
* need to finish the sort
"""

testcases = {
	"apple":""
}

anagrams = {}

def main():
	# so the task is to find the most amount of anagrams in a file full of words
	f = open("filename.txt") # TODO: try/catch
	for word in f.readlines():
		print word, type(word)
		sortedAnagram = str(sorted(word))
		print "sortedAnagram", type(sortedAnagram)

		if sortedAnagram not in anagrams.keys():
			anagrams[sortedAnagram] = {"count": 0, "words": []}

		anagrams[sortedAnagram]["words"].append(word)
		anagrams[sortedAnagram]["count"] += 1
	

	f.close()

	# TODO: sort anagrams by "count"
	#	* then print the top 3 lists
			
	#sorted(anagrams, key=lambda amagram:anagram["count"]) 
	# TODO: ^^ make this work

	pass

main()
