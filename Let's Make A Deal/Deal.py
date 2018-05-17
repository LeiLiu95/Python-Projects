# File: Deal.py

# Description: Choose an option from 3 choices

# Student Name: Lei Liu

# Student UT EID: LL28379

# Course Name: CS 303E

# Unique Number: 51200

# Date Created: 10/18/16

# Date Last Modified: 10/19/16

import random

def main():
	plays=int(input("Enter the number of times you want to play: "))
	wins=0
	print()
	print("  Prize      Guess       View    New Guess ")

	for i in range(1, plays+1):
		correct=random.randint(1,3)
		x=str(correct)
		print(" "*4+x,end=" "*10)
		oldguess=random.randint(1,3)
		x=str(oldguess)
		print(x+" "*10,end="")
		guess=oldguess
		view=random.randint(1,3)
		while(view==correct or view==oldguess):
			view=random.randint(1,3)
		x=str(view)
		print(x+" "*10,end="")
		while(guess==oldguess or guess==view):
			guess=random.randint(1,3)
		x=str(guess)
		print(x+"     ")
		if(correct==guess):
			wins+=1
	print()
	x=(wins/plays)
	x=round(x,2)
	y=1-x
	y=round(y,2)	
	x=str(x)
	y=str(y)
	print("Probability of winning if you switch = " + x)
	print("Probability of winning if you do not switch = " + y)
main()