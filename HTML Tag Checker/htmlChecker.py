#  File: htmlChecker.py
#  Description: Checks html webpages
#  Student's Name: Lei Liu
#  Student's UT EID: LL28379
#  Course Name: CS 313E 
#  Unique Number: 51915
#
#  Date Created: 2/27/17
#  Date Last Modified: 3/3/17

class Stack:    #stack class with initialization and methods

    def __init__(self):
        self.items = []

    def isEmpty(self):
        return (self.items == [])

    def size(self):
        return(len(self.items))
    
    def push(self,item):
        self.items.append(item)

    def pop(self):
        return(self.items.pop())

    def peek(self):
        return(self.items[-1])

    def __str__ (self):
        return str(self.items)

def getTag(inputString):    #getTag method extracts all tags in the html code and returns a list
    tags_List = []    #list of tags to return
    tagMark = ""
    check=False
    for word in inputString:
        if (word==">"):    #if last character is the > then do not append
            check=False
            if(tagMark.find("meta")>=0):    #check to see if meta is the tag
               tagMark="meta"   #removes all the unecessary data
            tags_List.append(tagMark) #once done append the tag then clear the variable
            tagMark=""
        if(check):
            tagMark+=word
        if (word=="<"):    #marks start of tag
            check=True
    return tags_List

def make_List(tags):    #iterate method for stack to get all values and turn it into a string
    tags_String="["
    temp=[]
    while tags.size()>0:    #pops off all the elements in the stack and appends them to a list
        popped=tags.pop()
        temp.append(popped)
    index=len(temp)-1
    while(index>=0):        #while loop to elements into a string then push back onto the stack
        tags_String+=temp[index]
        if(index!=0):
            tags_String+=", "
        tags.push(temp[index])
        index-=1
    tags_String+="]"    
    return tags_String

def main():
    tagList=[]  #list of tags
    VALIDTAGS=[]    #list of valid tags
    html=open("htmlfile.txt", "r")  #opens the html file to be read
    
    for word in html:   #iterate through to grab each tag in the html file
        word=word.strip()
        tag=getTag(word)
        for i in tag:   #goes through each word in the tag to check for tags
            tagList.append(i)
    tag_Stack=Stack()   #stack to be used for the tags

    list_Tags=""    #string for list of tags to print
    print()   #initialization to show user list of tags in list
    print("List of Tags")
    print()
    
    for i in range(0, len(tagList)):   #iterates and prints out all available tags
        if(i!=0):
            list_Tags+=", "
        list_Tags += tagList[i]

    print(list_Tags)    #prints the list of tags 
    print()
    print("Begin Program")  #begin program for checking tags
    print()
    mismatch = False
    exceptions = ["meta", "br", "hr"]

    for word in tagList:    #loop to iterate through all tags
        if word in exceptions:  #if word is in exceptions then pass on the tag and nothing needs to be pushed
            print("Tag " + word + " does not need to match:  stack is still " + make_List(tag_Stack))
            continue  #if word is in exceptions then skip it
        
        if  word[0]!="/" and word not in VALIDTAGS :  #if tag is not in validtags then add it to list
            VALIDTAGS.append(word)
            print("New tag " + word + " found and added to list of valid tags")
        
        #checks to see if the tag is the beggining, end or mismatch
        if word[0] != "/":  #if tag is the beggining then push onto stack
            tag_Stack.push(word)
            print("Tag " + word + " pushed:  stack is now " + make_List(tag_Stack))

        elif word[0]=="/" and word[1:]==tag_Stack.peek():   #if tag is the end then check it with top element of stack
            tag_Stack.pop()
            print("Tag " + word + " matches top of stack:  stack is now " + make_List(tag_Stack))

        else:   #else there is an error
            mismatch = True
            break

    print ()
    print ("End Program")   #program has finished
    print ()
    if tag_Stack.size() > 0 and not mismatch:  #if no error but elements remain on stack
        print ("Processing complete.  Unmatched tags remain on the stack: " + make_List(tag_Stack))
    elif tag_Stack.size()==0 and not mismatch: #if stack is empty and no error then it is good
        print ("Processing complete.  No mismatches found.")
    else:   #else there is an error
        print ("Error:  tag is " + word + " but top of stack is " + tag_Stack.peek())

    print()
    VALIDTAGS.sort()        #sort validtags and exceptions and then print
    exceptions.sort()
    valid_String="["
    for i in range (0, len(VALIDTAGS)): #makes the validtags list into a string without quotes
        if(i!=0):
            valid_String+=", "
        valid_String+=VALIDTAGS[i]
    valid_String+="]"

    exception_String="["                #makes the exceptions list into a string without quotes
    for i in range(0, len(exceptions)):
        if(i!=0):
            exception_String+=", "
        exception_String+=exceptions[i]
    exception_String+="]"
    
    print ("VALIDTAGS") #print valids and exceptions
    print (valid_String)
    print ()
    print ("EXCEPTIONS")
    print (exception_String)
    
    html.close()
main()
