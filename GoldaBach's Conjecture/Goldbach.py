
#  File: Goldbach.py

#  Description: Find 2 primes that sumes to an even number

#  Student Name: Lei Liu

#  Student UT EID: LL28379

#  Course Name: CS 303E

#  Unique Number: 51200

#  Date Created: October 9, 2016

#  Date Last Modified: October 9, 2016

def is_prime(x):
	for y in range(2, int(x**.5)+1):
		if(x%y==0):
			return False;
	return True;

def main():
	lower=int(input("Enter the lower limit: "))
	upper=int(input("Enter the upper limit: "))
	while(lower<4 or lower>=upper or (lower%2!=0 or upper%2!=0)):
		lower=int(input("Enter the lower limit: "))
		upper=int(input("Enter the upper limit: "))
	for x in range(lower, upper+1,2):
		print(x, end=" ")
		for y in range(2, x):
			for z in range(y, x):
				if(((y+z)==x) and (is_prime(y)==True and is_prime(z)==True)):
					a=str(y)
					b=str(z)
					print(" = " + a + " + " + b, end="")
		print()
main()