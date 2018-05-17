#  File: Spiral.py

#  Description: Count numbers in a spiral

#  Student Name: Lei Liu

#  Student UT EID: ll28379

#  Partner Name: Gabriela Dudzic

#  Partner UT EID: gd7237

#  Course Name: CS 303E

#  Unique Number: 51200

#  Date Created: 11/19/2016

#  Date Last Modified:11/21/2016

def main():
	dim=int(input("Enter dimension: "))
	if (dim%2==0):
		dim+=1
	spiral=int(input("Enter number in spiral: "))
	if (spiral>(dim*dim)):
		print("Number not in Range.")
		return
	square=[]

	# make a 2d list for the square and fill with random ints
	for i in range(0,dim):
		temp=[]
		for j in range(0,dim):
			temp.append(0)
		square.append(temp)
	num=1
	count=0
	twice=1
	x=dim//2
	y=x
	direction=-1
	while(num<=(dim*dim)):
		if (count==0):
			square[y][x]=num
			num+=1
		else:
			for i in range(0,count):
				if(direction==0):
					x+=1
				elif(direction==1):
					y+=1
				elif(direction==2):
					x-=1
				elif(direction==3):
					y-=1
				square[y][x]=num
				num+=1
				if(num>(dim*dim)):
					break
		twice+=1
		if(twice%2==0 and twice>0):
			twice=0
			count+=1
		direction+=1
		if(direction>3):
			direction=0
	found=False
	y=0
	x=0
	for y2 in range (0,dim):
		x=0
		for x2 in range(0,dim):
			if (square[y2][x2]==spiral):
				found=True
				break
			x+=1
		if(found==True):
			break
		y+=1
	if(x==0 or x==dim-1 or y==0 or y==dim-1):
		print("Number on Outer Edge.")
	else:
		print(str(square[y-1][x-1]) + " " + str(square[y-1][x]) + " " + str(square[y-1][x+1]))
		print(str(square[y][x-1]) + " " + str(square[y][x]) + " " + str(square[y][x+1]))
		print(str(square[y+1][x-1]) + " " + str(square[y+1][x]) + " " + str(square[y+1][x+1]))
main()