# Diego Magdaleno
# dmmagdal
# Question.py Programming assignment 5
# Guessing game part 2 using Binary Search to guess user's number

def binSearch(L, count):
	left = 0
	right = len(L)-1
	Response = ['e', 'E', 'g', 'G', 'l', 'L']
	while left <= right:
		m = (left+right)//2
		T = (L[m], count)
		if (right == left): # there is only 1 guess to be had
			return T
		print()
		print("Is your number Less than, Greater than, or Equal to "+str(L[m])+"?")
		n = input("Type 'L', 'G' or 'E': ")
		while n not in Response: # n is not any of the specified string variables
			print()
			n = input("Please type 'L', 'G' or 'E': ")
		if (n == "e" or n == "E"): # L[m] is the correct number
			return T
		elif (n == "l" or n == "L"): # the corret number is less than L[m]
			right = m-1
			count += 1
		elif (n == "g" or n == "G"): # the correct number is greater than L[m] / n == "g" or n == "G"
			left = m+1
			count += 1 
	T = ("null", 0)
	return T


print("Enter two numbers, low then high.")
x = int(input("low = "))
y = int(input("high = "))

while x > y:
	print("Please enter the smaller number followed by the larger number.")
	x = int(input("low = "))
	y = int(input("high = "))

print()
print("Think of a number in the range "+str(x)+" to "+str(y)+".")
L = list(range(x, y+1)) # create list with numebers from x to y inclusive
count = 1 # counter variable for number of guesses
if (x == y): # x and y are the same so there aren't any guesses
	count = 0;
	print()
	print("Your number is "+str(L[0])+". I found it in "+str(count)+"guesses.")
T = binSearch(L, count)
print()
if (T[1] == 1):
	print("Your number is "+str(T[0])+". I found it in "+str(T[1])+" guess.")
elif (T[0] == "null"):
	print("Your answers have not been consistant.")
else:
	print("Your number is "+str(T[0])+". I found it in "+str(T[1])+" guesses.")