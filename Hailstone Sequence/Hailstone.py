#  File: Hailstone.py

#  Description: Hailstone project

#  Student Name: Lei Liu

#  Student UT EID: LL28379

#  Course Name: CS 303E

#  Unique Number: 51200

#  Date Created: 9-27-16

#  Date Last Modified: 9-28-16

def main():
	start=int(input("Enter starting number of the range: "))
	end=int(input("Enter ending number of the range: "))
	while(start<=0 or end<=0 or start>end):
		start=int(input("Enter starting number of the range: "))
		end=int(input("Enter ending number of the range: "))
	i=0
	longest=0

	for x in range(start,end+1):
		num=x
		cycle=0
		while(num!=1):
			if(num%2==0):
				num=num//2
				cycle += 1
			else:
				num=num*3 + 1
				cycle += 1
		if(longest<=cycle):
			longest=cycle
			i=x
	i=str(i)
	longest=str(longest)
	print("The number " + i + " has the longest cycle length of " + longest + ".")
main()