from sys import exit
from math import sqrt

"""
Challenge
* https://www.reddit.com/r/dailyprogrammer/comments/4bc3el/20160321_challenge_259_easy_clarence_the_slow/

Status
* need a validatation function - validate the testcases against expected result

Keyboard Layout - horizontal/vertical spacing is 1cm
	1  2  3
	4  5  6
	7  8  9
	.  0	


Input
* ().().().() - where "()" is an integer in the range 0-999
"""

testcases = [
	"219.45.143.143", # => 27.38cm 
	"255.255.255.255", 

	# testcases not following input requirements
	"255..255.255.255",
	"255..255.255",
	"7851",
	"123456789.0", 
]


keyboard = ["1", "2", "3", "4", "5", "6", "7", "8", "9", ".", "0"]
coordinates = {}

def populateCoordinates():
	# populate coordinates dict
	for idx, key in enumerate(keyboard):
		row = idx % 3
		col = idx/3 # 3 is the rowSize

		#print row, col
		coordinates[key] = (row, col)

def distance(key1, key2):
	rowDistance = abs(coordinates[key1][0] - coordinates[key2][0])
	colDistance = abs(coordinates[key1][1] - coordinates[key2][1])

	# a^2 + b^2 = c^2
	result = sqrt(pow(rowDistance, 2) + pow(colDistance, 2))	
	
	#print "\t", rowDistance, colDistance, "=>", result
	return result

def validInput(ip):
	#
	# TODO: validate input against ().().().()
	octets = ip.split(".")
	if len(octets) != 4:
		return False
	
	for octet in octets: 
		if not octet.isdigit():
			# will match empty strings caused by two consecutive dots
			# will match negative numbers
			return False

		octet = int(octet)
		if octet < 0 or octet > 999:
			return False

	return True


def main():
	populateCoordinates()
	for testcase in testcases:
		if validInput(testcase):
			idx = 0
			totalDistance = 0
			while idx + 1 < len(testcase):
				totalDistance += distance(testcase[idx], testcase[idx+1])
				idx += 1		

			print testcase, "=>", round(totalDistance, 2), "cm"
		else:
			print testcase, "=> Invalid Input"

main()
