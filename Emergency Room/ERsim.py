#  File: ERsim.py
#  Description: Emergency room simulation
#  Student's Name: Lei Liu
#  Student's UT EID: LL28379
#  Course Name: CS 313E 
#  Unique Number: 51915
#
#  Date Created: 3/6/17
#  Date Last Modified: 3/10/17

class Queue (object):   #Queue class defined with constructor and methods
   def __init__(self):
      self.items = [ ]

   def isEmpty (self):
      return self.items == [ ]

   def enqueue (self, item):
      self.items.insert(0,item)

   def dequeue (self):
      return self.items.pop ()

   def size (self):
      return len(self.items)

   def peek (self):
      return self.items [len(self.items)-1]

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
   
def getString(param):   #a function to return the paramater into a printable string for display
   return_String=[]
   temp=""
   while(param.isEmpty()==False):   #gets all the values from queue and adds to list
      temp=param.dequeue()
      return_String.insert(0, temp)
   index=len(return_String)-1
   while(index>=0):  #add back all the elements back onto the queue
      param.enqueue(return_String[index])
      index-=1
   return return_String

def printQueues(Critical, Serious, Fair): #function to display all queues
   print("   Queues are:")
   critical_List=getString(Critical)
   serious_List=getString(Serious)
   fair_List=getString(Fair)
   print("   Critical " + str(critical_List))
   print("   Serious  " + str(serious_List))
   print("   Fair     " + str(fair_List))
   print()
   
def main():
   patients=open("ERsim.txt", "r")  #opens txt file
   Critical = Queue()   #create all 3 queues
   Serious = Queue()
   Fair = Queue()

   for i in patients:   #iterate through all commands from the text file
      i=i.strip()
      data = getInformation(i)   #parses data into usable information
      if(data[0]=="add"):     #if case to add a patient
         if(data[2]=="Critical"):   #check patient condition then add to proper queue
            Critical.enqueue(data[1])
            print(">>> Add patient " + data[1] + " to Critical queue")
         if(data[2]=="Serious"):
            Serious.enqueue(data[1])
            print(">>> Add patient " + data[1] + " to Serious queue")
         if(data[2]=="Fair"):
            Fair.enqueue(data[1])
            print(">>> Add patient " + data[1] + " to Fair queue")
         print()
         printQueues(Critical,Serious,Fair)  #print out status of queues
         
      elif(data[0]=="treat"): #another case to treat patients
         if(data[1]=="next"): #determine next patient to treat
            print(">>> Treat next patient")
            print()
            if(Critical.isEmpty()==False):   #check all queues until there is a patient to treat
               patient = Critical.dequeue()
               print("   Treating '" + patient + "' from Critical queue")
            elif(Serious.isEmpty()==False):
               patient = Serious.dequeue()
               print("   Treating '" + patient + "' from Serious queue")
            elif(Fair.isEmpty()==False):
               patient = Fair.dequeue()
               print("   Treating '" + patient + "' from Fair queue")
            else: #otherwise there is no patient to treat
               print("   No patients in queues")
               print()
               continue
            printQueues(Critical,Serious,Fair)
            
         elif(data[1]=="all"):   #if treat all, then iterate through all queues and treat all patients
            print(">>> Treat all patients")
            print()
            patient=""
            while(Critical.isEmpty()==False):
               patient=Critical.dequeue()
               print("   Treating '" + patient + "' from Critical queue")
               printQueues(Critical,Serious,Fair)
            while(Serious.isEmpty()==False):
               patient=Serious.dequeue()
               print("   Treating '" + patient + "' from Serious queue")
               printQueues(Critical,Serious,Fair)
            while(Fair.isEmpty()==False):
               patient=Fair.dequeue()
               print("   Treating '" + patient + "' from Fair queue")
               printQueues(Critical,Serious,Fair)
            print("   No patients in queues")   #once finished, there are no patients left in queues
            print()
         else: #else determine what condition to treat for a patient
            if(data[1]=="Critical"):   #treat depending on what condition was given
               if(Critical.isEmpty()): #check if the queue is empty
                  print("   No patients in queue") 
               else: #else treat the patient on the queue
                  print(">>> Treat next patient on Critical queue")
                  print()
                  patient=Critical.dequeue()
                  print("   Treating '" + patient + "' from Critical queue")
            elif(data[1]=="Serious"):
               if(Serious.isEmpty()):
                  print("   No patients in queue")
               else:
                  print(">>> Treat next patient on Serious queue")
                  print()
                  patient=Serious.dequeue()
                  print("   Treating '" + patient + "' from Serious queue")
            elif(data[1]=="Fair"):
               if(Fair.isEmpty()):
                  print("   No patients in queue")
               else:
                  print(">>> Treat next patient on Fair queue")
                  print()
                  patient=Fair.dequeue()
                  print("   Treating '" + patient + "' from Fair queue")
            printQueues(Critical,Serious,Fair)  #print status of queues
      elif(data[0]=="exit"):  #if input is exit, then exit from algorithm
         print(">>> Exit")
         break
   patients.close()  #close txt file
main()
