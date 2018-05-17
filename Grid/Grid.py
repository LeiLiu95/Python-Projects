
#  File: Grid.py

#  Description: Calculating the largest product in the grid

#  Student Name: Lei Liu

#  Student UT EID: ll28379

#  Partner Name:

#  Partner UT EID:

#  Course Name: CS 303E

#  Unique Number: 51200

#  Date Created: 11/13/2016

#  Date Last Modified: 11/14/2016

def main():
	in_file=open("grid.txt","r")

	dim=in_file.readline()
	dim=dim.strip()
	dim=int(dim)
	grid=[]
	product=0
	temp=0
	#populate the gride
	for i in range(dim):
		line=in_file.readline()
		line=line.strip()
		row=line.split()
		for j in range (dim):
			row[j]=int(row[j])
		grid.append(row)
	in_file.close()

	#read each row in blocks of four
	for row in grid:
		for i in range(dim-3):
			temp=1
			for j in range(i,i+4):
				temp=temp*row[j]
			if(temp>product):
				product=temp

	#read each column in blocks of four
	for j in range(dim):
		for i in range(dim-3):
			temp=1
			for k in range(i, i+4):
				temp=temp*grid[k][j]
			if(temp>product):
				product=temp

	#read all major diagonals
	for i in range(dim-3):
		temp=1
		for j in range(i,i+4):
			temp=temp*grid[j][j]
		if(temp>product):
			product=temp

	#read all diagonals left to right
	for i in range (dim-3):
		for j in range(dim-3):
			temp=1
			for k in range(4):
				temp=temp*grid[i+k][j+k]
			if(temp>product):
				product=temp

	for i in range(dim-3):
		temp=1
		for j in range(i,i+4):
			temp=temp*grid[j][dim-1-j]
		if(temp>product):
			product=temp

	for i in range(0,dim-3):
		for j in range(3,dim):
			temp=1
			for k in range(4):
				temp=temp*grid[i+k][j-k]
			if(temp>product):
				product=temp
	print("The greatest product is " + str(product)+".")
main()