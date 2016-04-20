import math

"""
Challenge
* https://www.reddit.com/r/dailyprogrammer/comments/4dccix/20160404_challenge_261_easy_verifying_3x3_magic/

Design decisions
* appended values to list for debugging purposes. Could alternatively add to variable to save CPU cycles
* calculated the diagonals in the main loop to save CPU cyles. Could have broken out into functions, but I wanted to avoid using range multiple times

"""

testcases = [
	[8, 1, 6, 3, 5, 7, 4, 9, 2], # => true
	[2, 7, 6, 9, 5, 1, 4, 3, 8], # => true
	[3, 5, 7, 8, 1, 6, 4, 9, 2], # => false
	[8, 1, 6, 7, 5, 3, 4, 9, 2]  # => false
]

# it's a 3x3 square - for now
n = 3

def getRowSum(testcase, x):
	base = n*x

	result = sum(testcase[base:base+n]) 
	# print "row", x, ":", testcase[base:base+n], " => " , result

	return result

def getColumnSum(testcase, x):
	# append to array instead of just adding them within the range loop 
	#	for debugging purposes

	column = []
	for i in range(0, n):
		column.append(testcase[x + n*i])

	result = sum(column)
	# print "column", x, column, "=>", result

	return result

def isMagicSquare(testcase):
	# 3x3 square 
	if len(testcase) != 3*3:
		#print "Error: dimensions are incorrect"
		return False 
		
	diag1 = []
	diag2 = []

	# check rows and columns
	for x in range(0, n):
		# check rows
		if getRowSum(testcase, x) != 15:
			#print "Error: row doesn't add up to 15"
			return False
	
		# check columns
		if getColumnSum(testcase, x) != 15:
			#print "Error: column doesn't add up to 15"
			return False
	
		# check down diagonal
		diag1.append(testcase[n * x + x])

		# check up diagonal
		diag2.append(testcase[n*(x+1) - x -1])

	diag1_sum = sum(diag1)
	diag2_sum = sum(diag2)

	#print "diag1: ", diag1, "=>", diag1_sum
	#print "diag2: ", diag2, "=>", diag2_sum

	if (diag1_sum != 15) or (diag2_sum != 15):
		#print "Error: diag doesn't add up to 15"
		return False

	return True
	

for testcase in testcases:
	# print "testcase: ", testcase
	# print "testcase size: ", len(testcase)

	print testcase, "=>", isMagicSquare(testcase)

