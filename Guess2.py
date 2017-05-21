# Diego Magdaleno
# dmmagdal
# Guess.py Programming assignment 3
# This is a short guessing game

import random

rand = random.randint(1, 10); #randomly generated number
# x is user input integer
counter = 3;
winner = False;

print("I'm thinkinkg of an integer in the range 1 to 10. You have three guesses.\n");
while counter != 0:
	if counter == 3:
		x = int(input("Enter your first guess: "));
	elif counter == 2:
		x = int(input("Enter your second guess: "));
	else: # counter == 1
		x = int(input("Enter your third guess: "));
	if x == rand:
		print("You win!\n");
		winner = True;
		break;
	elif x < rand:
		print("Your guess is too low\n");
	else: # x > rand
		print("Your guess is too high\n");
	counter-=1;
if winner != True:
	print("You lose. The number was "+str(rand)+".\n");
