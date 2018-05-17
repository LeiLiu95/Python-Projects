#  File: CreditCard.py

#  Description: credit card determination

#  Student Name: Lei Liu

#  Student UT EID: ll28379

#  Course Name: CS 303E

#  Unique Number: 51200

#  Date Created: 11/15/2016

#  Date Last Modified: 11/16/2016

# This function checks if a credit card number is valid
def is_valid(cc_num):
	cc_arr=[]
	while(cc_num>0):
		num=cc_num%10
		cc_arr.insert(0,num)
		cc_num=cc_num//10
	sum=0
	if(len(cc_arr)==16):
		for i in range(0,len(cc_arr),2):
			cc_arr[i]=cc_arr[i]*2
			if(cc_arr[i]>=10):
				cc_arr[i]=cc_arr[i]//10+cc_arr[i]%10
	else:
		for i in range(1,len(cc_arr),2):
			cc_arr[i]=cc_arr[i]*2
			if(cc_arr[i]>=10):
				cc_arr[i]=cc_arr[i]//10+cc_arr[i]%10
	for i in range(0,len(cc_arr)):
		sum+=cc_arr[i]
	if(sum%10==0):
		return True
	else:
		return False

# This function returns the type of credit card
def cc_type(cc_num):
	cc_arr=[]
	while(cc_num>0):
		num=cc_num%10
		cc_arr.insert(0,num)
		cc_num=cc_num//10
	if(cc_arr[0]==4):
		return "Visa "
	elif(cc_arr[0]==5):
		if(cc_arr[1]>=0 and cc_arr[1]<=5):
			return "MasterCard "
	elif(cc_arr[0]==6):
		if(cc_arr[1]==0):
			if(cc_arr[2]==1):
				if(cc_arr[3]==1):
					return "Discover "
		if(cc_arr[1]==4):
			if(cc_arr[2]==4):
					return "Discover "
		if(cc_arr[1]==5):
					return "Discover "
		return ""
	elif(cc_arr[0]==3):
		if(cc_arr[1]==4 or cc_arr[1]==7):
			return "American Express "
	else:
		return ""
def main(): 
	card=int(input("Enter 15 or 16-digit credit card number: "))
	print()
	if(len(str(card))==15 or len(str(card))==16):
		check=is_valid(card)
		if(check==True):
			print("Valid " + cc_type(card) + "credit card number")
		else:
			print("Invalid credit card number")
	else:
		print("Not a 15 or 16-digit number")
main()