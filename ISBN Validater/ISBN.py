#  File: ISBN.py

#  Description: Checks if ISBN is valid

#  Student Name: Lei Liu

#  Student UT EID: ll28379

#  Course Name: CS 303E

#  Unique Number: 51200

#  Date Created: 10/31/16

#  Date Last Modified: 10/31/16
def check(isbn):
	isbn=isbn.upper()
	check=[]
	if len(isbn)!=10:
		return False
	for x in range(0,len(isbn)-1):
		if(isbn[x].isdigit()==False):
			return False
	if (isbn[len(isbn)-1].isdigit()==False and isbn[len(isbn)-1]!='X'):
		return False
	for x in range(0,len(isbn)-1):
		check.append(eval(isbn[x]))
	if(isbn[len(isbn)-1]=='X'):
		check.append(10)
	else:
		check.append(eval(isbn[len(isbn)-1]))
	s1=[]
	s2=[]

	for x in range(len(isbn)):
		s1.append(0)
		s2.append(0)
		for y in range(x+1):
			s1[x]+=check[y]
		for y in range(x+1):
			s2[x]+=s1[y]
	return (s2[len(s2)-1]%11==0)


	return True
def main():
	in_file=open("isbn.txt","r")
	write_file=open("isbnOut.txt","w")
	print(in_file)
	isbn=in_file.readline()
	print(isbn)
	isbn=isbn.strip('\n')
	print(isbn)
	while(isbn!=''):
		isbn=isbn.replace('-','')
		if(check(isbn)==False):
			write_file.write(isbn+ '  invalid\n')
		else:
			write_file.write(isbn+ '  valid\n')
		isbn=in_file.readline()
		isbn=isbn.strip('\n')
	in_file.close()
	write_file.close()
main()
