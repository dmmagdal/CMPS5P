# Diego Magdaleno
# dmmagdal
# pa 4 Primes.py
# prints out n number of primes 

# find if the integer m is prime, if so, add it to List L
def isPrime(m, L):
	for i in range(len(L)):
		if (m%L[i] == 0):
			# is composite
			return False
		else:
			# is prime, continue along L
			continue
	return True # if False wasn't reached, the number is prime


x = int(input("Enter the number of Primes to compute: ")); # x is the number of roots to be found
# create list for holding n number of roots
PrimeList = [2]

m = 3 # m is the number to test to see if it is prime
while (len(PrimeList) != x): # continue with the loop, increasing m by 1, until the list is the size of x
	if (isPrime(m, PrimeList) == True): # if isPrime() returns true, add the number, m, to the primes list
		PrimeList.append(m)
	m+=1

print(" ")
print("The first "+str(x)+" primes are: ")
for i in range(len(PrimeList)):
	print(PrimeList[i], end = " ")
	if (i+1)%10 == 0:
		print()
#print(PrimeList) # print the resulting primes list