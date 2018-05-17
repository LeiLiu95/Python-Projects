
#  File: Day.py

#  Description: Calculates what day it is

#  Student Name: Lei Liu

#  Student UT EID: LL28379

#  Course Name: CS 303E

#  Unique Number: 51200

#  Date Created: 9-22-16

#  Date Last Modified: 9-24-16
days=["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
def leap(year):
	if((year%4==0 and year%100!=0) or year%400==0):
		return True
	return False

def main():
	c = int(input("Enter year: "))
	while(c<1900 or c>2100):
		c=int(input("Enter year: "))
	a = int(input("Enter month: "))
	while(a<1 or a>12):
		a=int(input("Enter month: "))
	b = int(input("Enter day: "))
	if(a<=7):
		if(a%2==1):
			while(b<1 or b>31):
				b=int(input("Enter day: "))
		else:
			while(b<1 or b>30):
				b=int(input("Enter day: "))
	if(a>7):
		if(a%2==0):
			while(b<1 or b>31):
				b=int(input("Enter day: "))
		else:
			while(b<1 or b>30):
				b=int(input("Enter day: "))
	if(a==2):
		if(leap(c)):
			while(b<1 or b>29):
				b=int(input("Enter day: "))
		else:
			while(b<1 or b>28):
				b=int(input("Enter day: "))
	if (a>2):
		a-=2
	else:
		a+=10
		c-=1
	d=c//100
	c=c%100
	w=(13*a-1)//5
	x=c//4
	y=d//4
	z=w+x+y+b+c-2*d
	r=z%7
	r=(r+7)%7
	print("The day is " + days[r])	

main()