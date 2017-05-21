# Diego Magdaleno
# dmmagdal@ucsc.edu
# Pa 1
# Sphere.py Takes user input for radius and gives volume and surface area if sphere
import math;

# function for volume and surface area of sphere
def funct(r):
	""" Return (volume, surface area) of sphere of radius r """
	v = 4*math.pi*math.pow(r, 3);
	v = v/3;
	sa = 4*math.pi*math.pow(r, 2);
	return (v, sa);

r = float(input("Enter the radius of the sphere: "));
T = funct(r);

print("The volume is: "+str(T[0]));
print("The surface area is: "+str(T[1]));