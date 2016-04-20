from sys import exit

testcases = {
	"Was it a car or a cat I saw?": True,
	"Are we not drawn onward, we few, drawn onward to new area?": False, # is this right?
	"Dammit I'm mad.\
Evil is a deed as I live.\
God, am I reviled? I rise, my bed on a sun, I melt.\
To be not one man emanating is sad. I piss.\
Alas, it is so late. Who stops to help?\
Man, it is hot. I'm in it. I tell.\
I am not a devil. I level Mad Dog.\
Ah, say burning is, as a deified gulp,\
In my halo of a mired rum tin.\
I erase many men. Oh, to be man, a sin.\
Is evil in a clam? In a trap?\
No. It is open. On it I was stuck.\
Rats peed on hope. Elsewhere dips a web.\
Be still if I fill its ebb.\
Ew, a spider eh?\
We sleep. Oh no!\
Deep, stark cuts saw it in one position.\
Part animal, can I live? Sin is a name.\
Both, one my names are in it\
Murder? I'm a fool.\
A hymn I plug, deified as a sign in ruby ash,\
A Goddam level I lived at.\
On mail let it in. I'm it.\
Oh, sit in ample hot spots. Oh wet!\
A loss it is alas (sip). I'd assign it a name.\
Name not one bottle minus an ode by me:\
Sir, I deliver. I'm a dog\
Evil is a deed as I live.\
Dammit Im mad.": True,
}

def isPalindrome(text):
		text = text.lower()

		text2 = []
		for char in text:
			if char.isalpha():
				text2.append(char)

		text = "".join(text2)
	
		# compare to reversed text	
		if text == text[::-1]: 
			return True

		return False

	

def main():
	# All other types of characters (spaces, punctuation, newlines, etc.) should be ignored
	# not case sensitive
	
	for testcase, answer in testcases.iteritems():
		result = isPalindrome(testcase)
		if result != answer:
			print "failed testcase: %s " % testcase
			exit(0)

		print testcase, "=>", result

	print "\nSuccessfully passed testcases"

main()
