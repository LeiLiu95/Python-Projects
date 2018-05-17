#  File: Books.py

#  Description: Checks words in books

#  Student Name: Lei Liu

#  Student UT EID: ll28379

#  Course Name: CS 303E

#  Unique Number: 51200

#  Date Created: 12/1/2016

#  Date Last Modified: 12/2/2016

# Create word dictionary from the comprehensive word list 
word_dict = {}
def create_word_dict ():
	words=open('words.txt','r')	#opens the word file to read available words
	for line in words:
		word_dict[line.strip()]=1
	words.close()		#closes the words.txt file

# Removes punctuation marks from a string
def parseString (st):
	prime=''	#variable to hold a string
	for i in range(len(st)):	#goes through the string to check for quotations
		if(st[i]=='\'' and st[i+1]!='\'s'):	#if the end is a new line then add it to the string
			prime+=st[i]
		elif(st[i].isalpha() or st[i].isspace()):
			prime+=st[i]
		else:			#if it is none of those then add a space to the string
			prime+=' '
	return prime

# Returns a dictionary of words and their frequencies
def getWordFreq (file):
	frequency_Dictionary={}
	inFile=open(file,'r')

	for words in inFile:		#for loop to go through each word and add it into dictionary if it is used
		words=words.rstrip()	#removes the line at the end of the word
		words=words.replace('-',' ')	#replaces - with " "
		if(words.endswith('\'s')):	#if it ends with an s then decrement by 2
			words=words[:len(words)-2]
		elif(words.endswith('\'')):		#checks to see if the word ends with a new line
			words=words[:len(words)-1]
		for key in (parseString(words)).split():		#for loop to add parsed words into the dictionary
			if key in frequency_Dictionary:		# if it is in the dictionary then add the element by 1
				frequency_Dictionary[key]+=1
			else:									#else add new entry
				frequency_Dictionary[key]=1
	capital_words=[]		#list used for all capital words
	for key in frequency_Dictionary:
		if(key[0].isupper()):
			capital_words.append(key)		#add key if the word is
	for word in capital_words:				#for each word in capital words check to see if it is in dictionary
		if(word.lower() in frequency_Dictionary):	#adds the value in dictionary by 1
			frequency_Dictionary[word.lower()]+=frequency_Dictionary[word]
		elif(word.lower() in word_dict):		#adds a new entry into the dictionary
			frequency_Dictionary[word.lower()]=frequency_Dictionary[word]
		del frequency_Dictionary[word]	#remove the word from the dictionary
	inFile.close()  		#close the file since we have added all words
	return frequency_Dictionary

def word_total(freq_dict):		#helper function that calculates the total # of words in the passage
	sum=0
	for index in freq_dict:
		sum+=freq_dict[index]
	return sum

# Compares the distinct words in two dictionaries
def wordComparison (author1, freq1, author2, freq2):
	d_words1=len(freq1)
	total_words1=word_total(freq1)
	#calculates the number of distinct words of author 1
	print(author1)
	print("Total distinct words = " + str(d_words1))
	print("Total words (including duplicates) = " + str(total_words1))
	print("Ratio (% of total distinct words to total words) = " + str(format(d_words1*100/total_words1,".10f")))
	print()
	#calculates the number of distinct words of author 2
	d_words2=len(freq2)
	total_words2=word_total(freq2)

	print(author2)
	print("Total distinct words = " + str(d_words2))
	print("Total words (including duplicates) = " + str(total_words2))
	print("Ratio (% of total distinct words to total words) = " + str(format(d_words2*100/total_words2,".10f")))
	print()
	
	unique1=0				#code to check what words the 1st author used that the second did not
	duplicate1=0
	for value in freq1:
		if(not(value in freq2)):
			unique1+=1
			duplicate1+=freq1[value]
			#prints the result
	print(author1 + " used " + str(unique1) + " words that " + author2 + " did not use.")
	print("Relative frequency of words used by " + author1 + " not in common with " + author2 + " = " + str(format(duplicate1*100/total_words1,".10f")))
	print()

	unique2=0
	duplicate2=0
	for value in freq2:		#code to check what words the 2nd author used that the first one did not
		if(not(value in freq1)):
			unique2+=1
			duplicate2+=freq2[value]
			#prints the result
	print(author2 + " used " + str(unique2) + " words that " + author1 + " did not use.")
	print("Relative frequency of words used by " + author2 + " not in common with " + author1 + " = " + str(format(duplicate2*100/total_words2,".10f")))

def main():
	# Create word dictionary from comprehensive word list
	create_word_dict()

	# Enter names of the two books in electronic form
	book1 = input ("Enter name of first book: ")
	book2 = input ("Enter name of second book: ")
	print()

	# Enter names of the two authors
	author1 = input ("Enter last name of first author: ")
	author2 = input ("Enter last name of second author: ")
	print() 
  
	# Get the frequency of words used by the two authors
	wordFreq1 = getWordFreq (book1)
	wordFreq2 = getWordFreq (book2)

	# Compare the relative frequency of uncommon words used
	# by the two authors
	wordComparison (author1, wordFreq1, author2, wordFreq2)

main()