# Diego Magdaleno
# dmmagdal
# Probability.py Programming Assignment 6
# rolls N number of dice of M sides to get stastics of their sum

import random

rnd = random.Random(237)

def throwDice(m, n):
	DiceList = []
	for i in range(n):
		DiceList.append(rnd.randrange(1, m+1))
	tuple(DiceList)
	return DiceList


#main------------------------------------------------------------------------------
n = int(input("Enter the number of dice: "))
while n < 1:
	n = int(input("The number of dice must be at least 1 \nPlease enter the number of dice: "))
print()
m = int(input("Enter the number of sides on each dice: "))
while m < 2:
	m = int(input("The number of sides on each dice should be at least 2 \nPlease enter the number of sides on each die: "))
print()
t = int(input("Enter the number of trials to perform: "))
while t < 1:
	t = int(input("The number of trials to perform should be at least 1 \nPlease enter the number of trials to perform: "))
print()

# variable setup
minimum = n
maximum = n*m
frequency = [0]*(maximum+1)

# roll dice and record results to frequency
for i in range(t):
	T = throwDice(m, n)
	throwSum = 0
	for j in range(len(T)):
		throwSum += T[j]
	frequency[throwSum] += 1

# compute relative frequency and experimental probability
relativefrequency = [0]*(maximum+1)
experimentalprobability = [0]*(maximum+1)
for i in range(minimum, len(frequency)):
	relativefrequency[i] = frequency[i]/t
	experimentalprobability[i] = relativefrequency[i]*100

# formatimg and printing results
l1 = "{0:<8}{1:<14}{2:<24}{3:<20}"
l2 = 70*"-"
l3 = "{0:>3}{1:>11.0f}{2:>19.5f}{3:>22.2f} %"
print(l1.format(" Sum","Frequency","Relative Frequency","Experimental Probability"))
print(l2)
for i in range(minimum, len(frequency)):
	print(l3.format(i, frequency[i], relativefrequency[i], experimentalprobability[i]))
print()