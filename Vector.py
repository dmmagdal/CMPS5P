# Diego Magdaleno
# dmmagdal
# Vector.py Programming Assignment 7
# Module designed to handle vector operations

'''
This module provides functions to perfrom standard vector operations. Vectors
are represented as lists of numbers (floats or ints). Functions that take two
vector arguments may give arbitrary output if the vectors are not compatible,
i.e. of the same dimension.
'''

import math
import random

rnd = random.Random()
Error = "Error: The two vectors are of different dimensions."

'''FUNCTIONS'''
def add(u, v):
	''' Return the vector sum u+v.'''
	if (lenTest(u, v) == True):
		x = [0]*len(v)
		for i in range(len(v)):
			x[i] = u[i] + v[i]
		return x
	return Error

def angle(u, v):
	''' Return the angle (in degrees) between vectors u and v.'''
	if (lenTest(u, v) == True):
		return math.degrees(math.acos(dot(unit(u),unit(v))))
	return Error

def dot(u, v):
	''' Return the dot product of u with v.'''
	if (lenTest(u, v) == True):
		dot = 0
		x = zip(u, v)
		for i in range(len(x)):
			dot += x[i]
		return dot
	return Error

def length(u):
	''' Return the (geometric) length of the vector u.'''
	return math.sqrt(dot(u, u))

def negate(u):
	''' Return the negative -u of the vector u'''
	x = u[:]
	for i in range(len(u)):
		x[i] *= -1
	return x;

def randVector(n, a, b):
	''' Return a vector of dimension n whose components are random floats 
	in the range [a, b).'''
	v = [0]*n
	for i in range(len(v)):
		v[i] = rnd.uniform(a, b)
	return v

def scalarMult(c, u):
	''' Return the scalar product cu of the number c by vector u.'''
	x = u[:]
	for i in range(len(u)):
		x[i] *= c
	return x

def sub(u, v):
	''' Return the vector difference u-v.'''
	if (lenTest(u, v) == True):
		return add(u, negate(v))
	return Error

def unit(v):
	''' Return a unit (geometric length 1) vector in the direction of v.'''
	x = v[:]
	for i in range(len(v)):
		x[i] /= length(v)
	return x

def zip(u, v):
	''' Return the component-wise product of u with v.'''
	if (lenTest(u, v) == True):
		x = [0]*len(v)
		for i in range(len(v)):
			x[i] = u[i]*v[i]
		return x
	return Error

def lenTest(u, v):
	''' Return True if two vectors are of same dimension.'''
	if (len(u) == len(v)):
		return True
	return False
