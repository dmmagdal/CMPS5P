# FibonacciTurtle.py

import turtle

def fib(n):
	L = [0, 1]
	for i in range(1, n+1):
		nxt = L[-1] + L[-2]
		L.append(nxt)
	return L

x = int(input("Enter the number of turns you want: "))
wn = turtle.Screen()
alice = turtle.Turtle()

Fib = fib(x)
m = 0 # holds the turn number as well as the fibonacci index number
while (m != x):
	alice.forward(5*Fib[m])
	alice.left(90)
	m+=1

wn.mainloop()