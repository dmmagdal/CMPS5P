# Diego Magdaleno
# dmmagdal
# Guess.py Programming assignment 3
# This is a short guessing game

import random

rand = random.randint(1, 10); #randomly generated number
#x is user input integer

print("I'm thinkinkg of an integer in the range 1 to 10. You hvae three guesses.\n");
x = int(input("Enter your first guess: "));
if x == rand:
	print("You win!\n");
else:
	if x < rand:
		print("Your guess is too low\n");
	else: #x > rand
		print("Your guess is too high\n");
	x = int(input("Enter your second guess: "));
	if x == rand:
		print("You win!\n");
	else:
		if x < rand:
			print("Your guess is too low\n");
		else: #x > rand
			print("Your guess is too high\n");
		x = int(input("Enter your third guess: "));
		if x == rand:
			print("You win!\n");
		else:
			if x < rand:
				print("Your guess is too low\n");
			else: #x > rand
				print("Your guess is too high\n");
			print("You lose. The number was "+str(rand)+".\n");