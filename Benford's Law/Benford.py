#  File: Benford.py

#  Description: Detect the number of times a digit occurs

#  Student Name: Lei Liu

#  Student UT EID: ll28379

#  Course Name: CS 303E

#  Unique Number: 51200

#  Date Created: 11/23/2016

#  Date Last Modified: 11/28/2016

def main():
	#creates the dictionary
	pop_freq={}

	#adds all 9 numbers to dictionary
	pop_freq['1']=0
	pop_freq['2']=0
	pop_freq['3']=0
	pop_freq['4']=0
	pop_freq['5']=0
	pop_freq['6']=0
	pop_freq['7']=0
	pop_freq['8']=0
	pop_freq['9']=0

	#opens the file
	in_file=open("Census_2009.txt", "r")

	header=in_file.readline()

	#counter for total number of counts
	num=0
	
	for line in in_file:
		num+=1
		line=line.strip()
		pop_data=line.split()
		pop_num=pop_data[-1]
		for i in range(1,10):
			if pop_num[0]==str(i):
				pop_freq[str(i)]+=1
				break
	#prints the data
	#keeps all the data equally spaced out 
	
	print("Digit\tCount\t%")
	#displays the percentages of all data

	for i in range(1,10):
		print("%d\t%d\t%.1f" % (i, pop_freq[str(i)],100*(pop_freq[str(i)])/num))
	in_file.close()

main()