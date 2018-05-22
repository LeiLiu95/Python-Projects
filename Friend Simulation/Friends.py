#  File: Friends.py
#  Description: Friends file that keeps tracks of friends
#  Student's Name: Lei Liu
#  Student's UT EID: LL28379
#  Course Name: CS 313E 
#  Unique Number: 51915
#
#  Date Created: 3/27/17
#  Date Last Modified: 4/7/17

class LinkedList():
    def __init__(self):     #initialize linked list with a pointer to null
        self.root=None

    def addFirst (self, item):
        temp=item
        temp.setNext(self.root)
        self.root=temp
     # Add an item to the beginning of the list
     
    def addLast (self, item):
        temp=item
        index=self.root
        previous=None
        if(index==None):        #iterates through linked list until last element then add
            temp.setNext(self.root)
            self.root=temp
            return
        while(index!=None):
            previous=index
            index=index.getNext()
        previous.setNext(temp)
     # Add an item to the end of a list

    def getLength (self):   #returns the length off the linked list
        counter=0
        index=self.root
        while(index!=None):
            counter+=1
            index=index.getNext()
        return counter
     # Return the number of items in the list 
     
    def findUnordered (self, item):
        index=self.root 
        while(index!=None): #iterate through linked list to find value or return false
            if(item==index.getData().getName()):
                return True
            index=index.getNext()
        return False
     # Search in an unordered list
     #    Return True if the item is in the list, False
     #    otherwise.
     
    def findFriend(self, item): #iterates through to see if item is in linked list
        index=self.root
        while(index!=None):
            if(item==index.getData().getName()):
                return index.getData()          #returns the friend class
            index=index.getNext()
        return None
    
    def delete (self, item):
        index=self.root
        previous=None
        found=False
        while(found==False and index!=None):    #iterate until the value is found or not found then remove
            if index.getData().getName()==item:
                found = True
            else:
                previous = index
                index = index.getNext()
        if(found==True):
            if previous == None:
                self.root = index.getNext()
            else:
                previous.setNext(index.getNext())
        return found
     # Delete an item from an unordered list
     #    if found, return True; otherwise, return False
     
    def returnString(self): #returns a string to print in the correct format
        index=self.root
        ret_String="    [ "
        while(index!=None):
            ret_String += index.getData().getName() + " "
            index = index.getNext()
        return ret_String + "]"
    
class Node(object):
    def __init__(self,initdata):    #node has a value and a pointer to next node
        self.data = initdata
        self.next = None            # always do this – saves a lot
        
    def getData (self):
        return self.data            # returns a POINTER

    def getNext (self):
        return self.next            # returns a POINTER

    def setData (self, newData):    # changes a POINTER
        self.data = newData

    def setNext (self,newNext):
        self.next = newNext         # changes a POINTER

class User():
    def __init__(self, name):   #user class with a name and linkedlist containing users
        self.name = name
        self.friendsList = LinkedList()
        
    def getName (self):
        return self.name            # returns name

    def getList (self):
        return self.friendsList     # returns a POINTER

    def addFriend(self, item):      # adds a user to the user's friends list
        self.friendsList.addFirst(item)
        
    def __str__(self):              # returns a string to print
        return self.friendsList.returnString()
    
    def friendLength(self):         #returns the length of the linked list of friends
        return self.friendsList.getLength()
    
    def deleteFriend(self, item):   #removes item from linked list
        self.friendsList.delete(item)
    
def getInformation(param): #a function to parse a string of words and return it in a list
    items=[]
    word=""
    for i in param:  #loop to iterate through to get each word and append to list
        if(i!=" "):
            word+=i
        else:
            items.append(word)
            word=""
    items.append(word)
    return items

def main():
    friends = LinkedList()
    friends_Input = open("FriendData.txt", "r")
    
    for i in friends_Input:
        i=i.strip()
        data = getInformation(i)    #parses data into readable information
    
        if(data[0]=="Person"):  #if command is person then add user to linked list
            print("--> Person " + data[1])
            if(friends.findUnordered(data[1])==False):
                person = User(data[1])
                node = Node(person)
                friends.addLast(node)
                print("    " + data[1] + " now has an account.")
            else:               #if user is already created then ignore
                print("    A person with name " + data[1] + " already exists.")
            print()
            
        elif(data[0]=="Friend"):    #add each user to each others friends list only if both users exist and are not currently friends
            print("--> Friend " + data[1] + " " + data[2])
            if(data[1]==data[2]):
                print("    " + "A person cannot friend him/herself.")
            elif(friends.findUnordered(data[1])==False):
                print("    A person with name " + data[1] + " does not currently exist.")
            elif(friends.findUnordered(data[2])==False):
                print("    A person with name " + data[2] + " does not currently exist.")
            else:
                user1=friends.findFriend(data[1])
                user2=friends.findFriend(data[2])
                if(user1.friendsList.findFriend(data[2]) or user2.friendsList.findFriend(data[1])):
                    print("    " + data[1] + " and " + data[2] + " are already friends.")
                else:
                    user1=friends.findFriend(data[1])
                    user2=User(data[2])
                    user2=Node(user2)
                    user1.addFriend(user2)
                    
                    user2=friends.findFriend(data[2])
                    user1=User(data[1])
                    user1=Node(user1)
                    user2.addFriend(user1)
                    print("    " + data[1] + " and " + data[2] + " are now friends.")
            print()
            
        elif(data[0]=="Unfriend"):  #remove each user from each others friends list only if both users exist and are currently friends
            print("--> Unfriend " + data[1] + " " + data[2])
            if(data[1]==data[2]):
                print("    " + "A person cannot unfriend him/herself.")
            elif(friends.findUnordered(data[1])==False):
                print("    A person with name " + data[1] + " does not currently exist.")
            elif(friends.findUnordered(data[2])==False):
                print("    A person with name " + data[2] + " does not currently exist.")
            else:
                user1=friends.findFriend(data[1])
                user2=friends.findFriend(data[2])
                if(user1.friendsList.findFriend(data[2])):
                    user1.deleteFriend(data[2])
                    user2.deleteFriend(data[1])
                    print("    " + data[1] + " and " + data[2] + " are no longer friends.")
                else:
                    print("    " + data[1] + " and " + data[2] + " aren't friends, so you can't unfriend them.")
            print()
            
        elif(data[0]=="List"):  #list out a users friends list and displays all the current users names
            print("--> List " + data[1])
            if(friends.findUnordered(data[1])==False):
                print("    A person with name " + data[1] + " doesn not currently exist.")
            else:
                user=friends.findFriend(data[1])
                if(user.friendLength()==0):
                    print("    " + data[1] + " has no friends.")
                else:
                    print(user)
            print()
            
        elif(data[0]=="Query"): #checks the status of two users, if they are friends or not only if they both exist
            print("--> Query " + data[1] + " " + data[2])
            if(data[1]==data[2]):
                print("    " + "A person cannot query him/herself.")
            elif(friends.findUnordered(data[1])==False):
                print("    A person with name " + data[1] + " does not currently exist.")
            elif(friends.findUnordered(data[2])==False):
                print("    A person with name " + data[2] + " does not currently exist.")
            else:
                user1=friends.findFriend(data[1])
                if(user1.friendsList.findFriend(data[2])):
                    print("    " + data[1] + " and " + data[2] + " are friends.")
                else:
                    print("    " + data[1] + " and " + data[2] + " are not friends.")
            print()
                   
        elif(data[0]=="Exit"):  #exits program
            print("--> Exit")
            print("    Exiting...")
            break
    friends_Input.close()
main()
