#  File: LinkedList.py
#  Description: Linked list class and methods
#  Student's Name: Lei Liu
#  Student's UT EID: LL28379
#  Course Name: CS 313E 
#  Unique Number: 51915
#
#  Date Created: 3/11/2017
#  Date Last Modified: 3/23/2017

# Copy and paste the following after your class definitions for
# Nodes and LinkedLists.  Do NOT change any of the code in main()!

class Node(object):
    def __init__(self,initdata):    #node has a value and a pointer to next node
        self.data = initdata
        self.next = None            # always do this – saves a lot
        
    def getData (self):
        return self.data            # returns a POINTER

    def getNext (self):
        return self.next            # returns a POINTER

    def setData (self, newData):
        self.data = newData         # changes a POINTER

    def setNext (self,newNext):
        self.next = newNext         # changes a POINTER

class LinkedList():
    def __init__(self):     #initialize linked list with a pointer to null
        self.root=None
        
    def __str__ (self):
        return_String=""        #value to hold string value
        counter=0
        index=self.root
        while(index!=None):     #iterate through the linked list and get each value of node
            return_String+=index.getData() + "  "
            index=index.getNext()
            counter+=1
            if(counter==10):    #set a new line when 10 elements has been read
                counter=0
                return_String+="\n"
        return return_String
     # Return a string representation of data suitable for printing.
     #    Long lists (more than 10 elements long) should be neatly
     #    printed with 10 elements to a line, two spaces between
     #    elements
  
    def addFirst (self, item):
        temp=Node(item)
        temp.setNext(self.root)
        self.root=temp
     # Add an item to the beginning of the list
     
    def addLast (self, item):
        temp=Node(item)
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

    def addInOrder (self, item):
        temp=Node(item)
        index=self.root
        previous=None
        if(index==None):    #if list is empty add to first element
            temp.setNext(self.root)
            self.root=temp
            return
        check=index
        if(check.getNext()==None): #check if there is only 1 node in linked list
            if(index.getData()>temp.getData()):
                index.setNext(None)
                temp.setNext(index)
            else:
                temp.setNext(None)
                index.setNext(temp)
        while(index!=None):  #if it goes to end of list then put at end of list
            if(temp.getData()<index.getData() and previous!=None):
                temp.setNext(index)
                previous.setNext(temp)
                return
            if(temp.getData()<index.getData() and previous==None):
                temp.setNext(index)
                self.root=temp
                return
            previous=index
            index=index.getNext()
        previous.setNext(temp)
        return
     # Insert an item into the proper place of an ordered list.
     # This assumes that the original list is already properly
     #    ordered.

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
            if(item==index.getData()):
                return True
            index=index.getNext()
        return False
     # Search in an unordered list
     #    Return True if the item is in the list, False
     #    otherwise.
     
    def findOrdered (self, item):
        index=self.root
        while(index!=None): #iterate through list to find element
            if(item==index.getData()):
                return True
            if(item<index.getData()):   #if element is before the data in current node then it does not exist in linked list
                return False
            index=index.getNext()
        return False
     # Search in an ordered list
     #    Return True if the item is in the list, False
     #    otherwise.
     # This method MUST take advantage of the fact that the
     #    list is ordered to return quicker if the item is not
     #    in the list.

    def delete (self, item):
        index=self.root
        previous=None
        found=False
        while(found==False and index!=None):    #iterate until the value is found or not found then remove
            if index.getData()==item:
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

    def copyList (self):    #not sure if correct
        index=self.root
        values=[]
        while(index!=None): #iterate through list copying each value and adding it to new copy
            values.append(index.getData())
            index=index.getNext()
        copy=LinkedList()
        for i in range(0,len(values)):
            copy.addLast(values[i])
        return copy
     # Return a new linked list that's a copy of the original,
     #    made up of copies of the original elements

    def reverseList (self):
        index=self.root
        values=[]
        while(index!=None): #reverses values in list
            values.append(index.getData())
            index=index.getNext()
        copy=LinkedList()
        for i in range(0,len(values)):
            copy.addFirst(values[i])
        return copy
     # Return a new linked list that contains the elements of the
     #    original list in the reverse order.

    def orderList (self):
        copy=LinkedList()
        values=[]
        index=self.root
        while(index!=None): #add items into copy linked list using the add in ordere method
            values.append(index.getData())
            index=index.getNext()
        for i in range(0,len(values)):
            copy.addInOrder(values[i])
        return copy
            
     # Return a new linked list that contains the elements of the
     #    original list arranged in ascending (alphabetical) order.
     #    Do NOT use a sort function:  do this by iteratively
     #    traversing the first list and then inserting copies of
     #    each item into the correct place in the new list.

    def isOrdered (self):
        index=self.root
        check=self.root
        while(index!=None):     #iterate through linked list and checks if all nodes in order
            if(check.getData()>index.getData()):
                return False
            check=index
            index=index.getNext()
        return True
     # Return True if a list is ordered in ascending (alphabetical)
     #    order, or False otherwise

    def isEmpty (self):
        if(self.root==None):    #if linked list is empty then root should be pointing to a null
            return True
        else:
            return False
     # Return True if a list is empty, or False otherwise

    def mergeList (self, b):
        copy=LinkedList()
        index=self.root
        index2=b.root
        while(index!=None and index2!=None):    #iterate through two list adding elements in order
            if(index.getData()<index2.getData()):
                copy.addLast(index.getData())
                index=index.getNext()
                continue
            else:
                copy.addLast(index2.getData())
                index2=index2.getNext()
        if(index==None):    #if either linked list has reached the end then add all nodes from other list
            while(index2!=None):
                copy.addLast(index2.getData())
                index2=index2.getNext()
        else:
            while(index!=None):
                copy.addLast(index.getData())
                index=index.getNext()
        return copy
     # Return an ordered list whose elements consist of the 
     #    elements of two ordered lists combined.

    def isEqual (self, b):
        index=self.root
        index2=b.root
        while(index!=None): #iterates through both lists to see if all nodes are the same
            if((index==None and index2!=None) or (index!=None and index2==None)):
                return False
            if(index.getData()!=index2.getData()):
                return False
            index=index.getNext()
            index2=index2.getNext()
        return index==index2
     # Test if two lists are equal, item by item, and return True.

    def removeDuplicates (self):
        copy=LinkedList()
        index=self.root
        values=[]
        while(index!=None): #removes all duplicates in linked list
            if(index.getData() not in values):
                copy.addLast(index.getData())
                values.append(index.getData())
            index=index.getNext()
        return copy
     # Remove all duplicates from a list, returning a new list.
     #    Do not change the order of the remaining elements.

def main():

   print ("\n\n***************************************************************")
   print ("Test of addFirst:  should see 'node34...node0'")
   print ("***************************************************************")
   myList1 = LinkedList()
   for i in range(35):
      myList1.addFirst("node"+str(i))

   print (myList1)

   print ("\n\n***************************************************************")
   print ("Test of addLast:  should see 'node0...node34'")
   print ("***************************************************************")
   myList2 = LinkedList()
   for i in range(35):
      myList2.addLast("node"+str(i))

   print (myList2)

   print ("\n\n***************************************************************")
   print ("Test of addInOrder:  should see 'alpha delta epsilon gamma omega'")
   print ("***************************************************************")
   greekList = LinkedList()
   greekList.addInOrder("gamma")
   greekList.addInOrder("delta")
   greekList.addInOrder("alpha")
   greekList.addInOrder("epsilon")
   greekList.addInOrder("omega")
   print (greekList)

   print ("\n\n***************************************************************")
   print ("Test of getLength:  should see 35, 5, 0")
   print ("***************************************************************")
   emptyList = LinkedList()
   print ("   Length of myList1:  ", myList1.getLength())
   print ("   Length of greekList:  ", greekList.getLength())
   print ("   Length of emptyList:  ", emptyList.getLength())

   print ("\n\n***************************************************************")
   print ("Test of findUnordered:  should see True, False")
   print ("***************************************************************")
   print ("   Searching for 'node25' in myList2: ",myList2.findUnordered("node25"))
   print ("   Searching for 'node35' in myList2: ",myList2.findUnordered("node35"))

   print ("\n\n***************************************************************")
   print ("Test of findOrdered:  should see True, False")
   print ("***************************************************************")
   print ("   Searching for 'epsilon' in greekList: ",greekList.findOrdered("epsilon"))
   print ("   Searching for 'omicron' in greekList: ",greekList.findOrdered("omicron"))

   print ("\n\n***************************************************************")
   print ("Test of delete:  should see 'node25 found', 'node34 found',")
   print ("   'node0 found', 'node40 not found'")
   print ("***************************************************************")
   print ("   Deleting 'node25' (random node) from myList1: ")
   if myList1.delete("node25"):
      print ("      node25 found")
   else:
      print ("      node25 not found")
   print ("   myList1:  ")
   print (myList1)

   print ("   Deleting 'node34' (first node) from myList1: ")
   if myList1.delete("node34"):
      print ("      node34 found")
   else:
      print ("      node34 not found")
   print ("   myList1:  ")
   print (myList1)

   print ("   Deleting 'node0'  (last node) from myList1: ")
   if myList1.delete("node0"):
      print ("      node0 found")
   else:
      print ("      node0 not found")
   print ("   myList1:  ")
   print (myList1)

   print ("   Deleting 'node40' (node not in list) from myList1: ")
   if myList1.delete("node40"):
      print ("      node40 found")
   else:
      print ("   node40 not found")
   print ("   myList1:  ")
   print (myList1)

   print ("\n\n***************************************************************")
   print ("Test of copyList:")
   print ("***************************************************************")
   greekList2 = greekList.copyList()
   print ("   These should look the same:")
   print ("      greekList before delete:")
   print (greekList)
   print ("      greekList2 before delete:")
   print (greekList2)
   greekList2.delete("alpha")
   print ("   This should only change greekList2:")
   print ("      greekList after deleting 'alpha' from second list:")
   print (greekList)
   print ("      greekList2 after deleting 'alpha' from second list:")
   print (greekList2)
   greekList.delete("omega")
   print ("   This should only change greekList1:")
   print ("      greekList after deleting 'omega' from first list:")
   print (greekList)
   print ("      greekList2 after deleting 'omega' from first list:")
   print (greekList2)

   print ("\n\n***************************************************************")
   print ("Test of reverseList:  the second one should be the reverse")
   print ("***************************************************************")
   print ("   Original list:")
   print (myList1)
   print ("   Reversed list:")
   myList1Rev = myList1.reverseList()
   print (myList1Rev) 

   print ("\n\n***************************************************************")
   print ("Test of orderList:  the second list should be the first one sorted")
   print ("***************************************************************")
   planets = LinkedList()
   planets.addFirst("Mercury")
   planets.addFirst("Venus")
   planets.addFirst("Earth")
   planets.addFirst("Mars")
   planets.addFirst("Jupiter")
   planets.addFirst("Saturn")
   planets.addFirst("Uranus")
   planets.addFirst("Neptune")
   planets.addFirst("Pluto?")
   
   print ("   Original list:")
   print (planets)
   print ("   Ordered list:")
   orderedPlanets = planets.orderList()
   print (orderedPlanets)

   print ("\n\n***************************************************************")
   print ("Test of isOrdered:  should see False, True")
   print ("***************************************************************")
   print ("   Original list:")
   print (planets)
   print ("   Ordered? ", planets.isOrdered())
   orderedPlanets = planets.orderList()
   print ("   After ordering:")
   print (orderedPlanets)
   print ("   ordered? ", orderedPlanets.isOrdered())

   print ("\n\n***************************************************************")
   print ("Test of isEmpty:  should see True, False")
   print ("***************************************************************")
   newList = LinkedList()
   print ("New list (currently empty):", newList.isEmpty())
   newList.addFirst("hello")
   print ("After adding one element:",newList.isEmpty())

   print ("\n\n***************************************************************")
   print ("Test of mergeList")
   print ("***************************************************************")
   list1 = LinkedList()
   list1.addLast("aardvark")
   list1.addLast("cat")
   list1.addLast("elephant")
   list1.addLast("fox")
   list1.addLast("lynx")
   print ("   first list:")
   print (list1)
   list2 = LinkedList()
   list2.addLast("bacon")
   list2.addLast("dog")
   list2.addLast("giraffe")
   list2.addLast("hippo")
   list2.addLast("wolf")
   print ("   second list:")
   print (list2)
   print ("   merged list:")
   list3 = list1.mergeList(list2)
   print (list3)

   print ("\n\n***************************************************************")
   print ("Test of isEqual:  should see True, False, True")
   print ("***************************************************************")
   print ("   First list:")
   print (planets)
   planets2 = planets.copyList()
   print ("   Second list:")
   print (planets2)
   print ("      Equal:  ",planets.isEqual(planets2))
   print (planets)
   planets2.delete("Mercury")
   print ("   Second list:")
   print (planets2)
   print ("      Equal:  ",planets.isEqual(planets2))
   print ("   Compare two empty lists:")
   emptyList1 = LinkedList()
   emptyList2 = LinkedList()
   print ("      Equal:  ",emptyList1.isEqual(emptyList2))

   print ("\n\n***************************************************************")
   print ("Test of removeDuplicates:  original list has 14 elements, new list has 10")
   print ("***************************************************************")
   dupList = LinkedList()
   print ("   removeDuplicates from an empty list shouldn't fail")
   newList = dupList.removeDuplicates()
   print ("   printing what should still be an empty list:")
   print (newList)
   dupList.addLast("giraffe")
   dupList.addLast("wolf")
   dupList.addLast("cat")
   dupList.addLast("elephant")
   dupList.addLast("bacon")
   dupList.addLast("fox")
   dupList.addLast("elephant")
   dupList.addLast("wolf")
   dupList.addLast("lynx")
   dupList.addLast("elephant")
   dupList.addLast("dog")
   dupList.addLast("hippo")
   dupList.addLast("aardvark")
   dupList.addLast("bacon")
   print ("   original list:")
   print (dupList)
   print ("   without duplicates:")
   newList = dupList.removeDuplicates()
   print (newList)

main()
