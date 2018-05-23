#  File: MultiwayTree.py
#  Description: Program to check if two given trees are isomorphic
#  Student's Name: Lei Liu
#  Student's UT EID: LL28379
#  Course Name: CS 313E 
#  Unique Number: 51915
#
#  Date Created: 4/22/17
#  Date Last Modified: 4/27/17

class Node:
    def __init__(self,initdata):    #node that holds data and an array
        self.data = initdata
        self.tree = []
        
    def getData (self):
        return self.data            # returns a POINTER

    def getTree (self):
        return self.tree            # returns a POINTER

    def setData (self, newData):
        self.data = newData         # changes a POINTER

    def setTree (self,newTree):
        self.tree = newTree

def treeHelper(treeList, pyTree):   #treeList is the current List, pyTree is remaining elements
    if(pyTree[0]=="]"): #recursive function to append all following nodes to tree
        temp=Node(None)
        treeList.append(temp)
        if(len(pyTree)!=1):
            return pyTree[1:]
        else:
            return pyTree
    elif(pyTree[0]=="["):   #other base case, recurse call if another tree
        pyTree=treeHelper(treeList, pyTree[1:])
        return pyTree
    else:
        temp=Node(pyTree[0])    #add a new node of the current element into arraylist
        pyTree=pyTree[1:]
        pyTree=treeHelper(temp.getTree(), pyTree)
        treeList.append(temp)
        return pyTree
    
def preOrderHelper(node):   #helper recursive function to print out the elements in the tree
    temp=""
    if(node.getData()!=None):
        temp+=str(node.getData()) + " "
    for i in node.getTree():
        temp+=preOrderHelper(i)
    return temp

def isIsomorphicToHelper(selfN,otherN): #helper function to check if two trees are iso or not
    check=True
    if(selfN.getData()!=None and otherN.getData()!=None):
        return False
    else:
        for i in len(selfN.getTree()):
            check=isIsomorphicToHelper(selfN.tree[i],otherN.tree[i])
            return check

class MultiwayTree:
    def __init__(self,pyTree):  #given "pyTree", a Python representation of a tree, create a node-and-pointer representation of that tree.
        self.root = Node(pyTree[1])     #the root is a node that has a data and a list of all following nodes
        self.iso=pyTree
        pyTree=pyTree[2:]
        while(len(pyTree)!=1):
            pyTree=treeHelper(self.root.getTree(), pyTree) #a recursive call begins with the root's list and the rest of pyTree
    def preOrder(self, num):  #print out the node-and-pointer representation of a tree using preorder.
        print("Tree " + str(num) + " preorder:   ", end="")
        temp=""
        temp+=str(self.root.getData()) + " "
        for i in self.root.getTree():
            temp+=preOrderHelper(i)
        print(temp)
        print()
    def isIsomorphicTo(self,other):  #return True if the tree "self" has the same structure as the tree "other", "False" otherwise.
        stackS=[]
        stackO=[]
        if(len(self.iso)!=len(other.iso)):
            return False
        for i in range(0,len(self.iso)):
            stackS.append(self.iso[i])
            stackO.append(other.iso[i])
        while(len(stackS)!=0):
            checkS=stackS.pop()
            checkO=stackO.pop()
            if((checkS=="[" and checkO=="]") or (checkS=="]" and checkO=="[")):
                return False
        return True

def getInformation(param): #a function to parse a string of words and return it in a list
    items=[]
    word=""
    for i in param:  #loop to iterate through to get each word and append to list
        if(i=='"' or i==" " or i==","):
            continue
        elif(i=="[" or i=="]"):
            if(len(word)!=0):
                items.append(word)
                word=""
            items.append(i)
        else:
            word+=i
    return items

def stringInformation(param):
    items=[]
    word=""
    for i in param:  #loop to iterate through to get each word and append to list
        word+=i
    items.append(word)
    return items

def main():
    tree = open("MultiwayTreeInput.txt", "r")
    trees=[]
    for i in tree:
        i=i.strip()
        data = stringInformation(i)    #parses data into readable information
        print("Tree " + str(len(trees)+1) + ":  " + data[0])
        
        data = getInformation(i)
        multiTree=MultiwayTree(data)
        trees.append(multiTree)
        multiTree.preOrder(len(trees))
        if(len(trees)%2==0):
            if(multiTree.isIsomorphicTo(trees[len(trees)-2])):
                print("Tree " + str(len(trees)-1) + " is isomorphic to Tree " + str(len(trees)))
            else:
                print("Tree " + str(len(trees)-1) + " is not isomorphic to Tree " + str(len(trees)))
            print()
            print()
    tree.close()
main()
