#  File: Dice.py
#  Description: Counts the number of times a number is rolled
#  Student's Name: Lei Liu
#  Student's UT EID: LL28379
#  Course Name: CS 313E 
#  Unique Number: 51915
#
#  Date Created: 1/30/17
#  Date Last Modified: 2/2/17
import random

def highest_Value(rolls):           #a method that returns the highest value in a list
    high=rolls[0]                   #sets high to the first element in list
    for i in range(0,len(rolls)):   #for loop that iterates through to check each element if it is the highest value
        if (high<rolls[i]):         #if an element in list is greater than current high value then replace it
            high=rolls[i]
    return high

def main():
    random.seed(1314)               #This statement makes the code pseudorandom
    num_Rolls=int(input("How many times do you want to roll the dice? "))   #Gets the user input to determine how many times to roll the dice
    rolls=[0,0,0,0,0,0,0,0,0,0,0]   #creates a list to store each number of rolls from 2-12
    for i in range (0,num_Rolls):   #for loop to roll 2 die the number of times the user inputs
        roll_Result=random.randint(1,6)+random.randint(1,6)-2
        rolls[roll_Result]+=1
    print("Results: ",end=" ")      #prints the results of each roll of each number that occured
    print(rolls)
    if (num_Rolls>100):             #if the number of rolls is greater than 100 then scale it
        for i in range(0,len(rolls)):   
            rolls[i]=int(round(rolls[i]*(100/num_Rolls),0))
    print()
    height=highest_Value(rolls) #set height to the highest value

    for i in range(0,height):   #for loop to iterate from the highest value to the lowest
        print("|",end="")
        for j in range(0,len(rolls)):   #iterate through the list to see if any "*" needs to be printed in the current line
            if (rolls[j]>=(height-i)):
                print("  *",end="")
            else:                       
                print("   ",end="")
        print()                 
    print("+--+--+--+--+--+--+--+--+--+--+--+-")    #prints the ending line and numbers related to the rolls
    print("   2  3  4  5  6  7  8  9 10 11 12")
main()
