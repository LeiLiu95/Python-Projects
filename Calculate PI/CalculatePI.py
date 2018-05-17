#  File: CalculatePI.py

#  Description: Random darts thrown at board to calculate pi

#  Student Name: Lei Liu

#  Student UT EID: LL28379

#  Course Name: CS 303E

#  Unique Number: 51200

#  Date Created: October 11, 2016

#  Date Last Modified: October 13, 2016

import math
import random

def computePI(numThrows):
	inside=0.0
	outside=0.0
	for i in range(0, numThrows+1):
		x=random.uniform(-1.0,1.0)
		y=random.uniform(-1.0,1.0)
		distance=math.hypot(x,y)
		if(distance<1):
			inside+=1
	return inside/numThrows
def main():
	x = 100
	spaces=8
	while(x<=10000000):
		computed=computePI(x)*4
		difference=(computed-math.pi)
		z=str(x)
		print("num = " + z + " "*spaces + "Calculated PI = %.6f" % (computed) + "   " + "Difference = %+-6f" % (difference))
		x=x*10
		spaces-=1
	print()
	print("Difference = Calculated PI - math.pi")
main()