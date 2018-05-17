
#  File: EasterSunday.py

#  Description: EasterSunday assignment

#  Student Name: Lei Liu

#  Student UT EID: LL28379

#  Course Name: CS 303E

#  Unique Number: 51200

#  Date Created: 9/10/16

#  Date Last Modified: 9/10/16

months=["January", "February", "March", "April", "May"]

def main():
	y=input('Enter year: ')
	y=int(y)
	a=y%19
	b=y/100
	b=int(b)
	c=y%100
	d=b/4
	d=int(d)
	e=b%4
	g=((8*b)+13)/25
	g=int(g)
	h=((19*a)+b-d-g+15)%30
	j=c/4
	j=int(j)
	k=c%4
	m=(a+(11*h))/319
	m=int(m)
	r=((2*e)+(2*j)-k-h+m+32)%7
	n=(h-m+r+90)/25
	n=int(n)
	p=(h-m+r+n+19)%32
	print('')
	y=str(y)
	p=str(p)
	n=int(n)
	print('In ' + y + ' Easter Sunday is on ' + p + ' ' + months[n-1] + '.')

main()