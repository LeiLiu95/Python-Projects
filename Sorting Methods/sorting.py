#  File: sorting.py
#  Description: Averages times of different sorting algorithms
#  Student's Name: Lei Liu
#  Student's UT EID: LL28379
#  Course Name: CS 313E 
#  Unique Number: 51915
#
#  Date Created: 4/18/17
#  Date Last Modified: 4/21/17

import random
import time
import sys
sys.setrecursionlimit(10000)

def bubbleSort(alist):
    for passnum in range(len(alist)-1,0,-1):
        for i in range(passnum):
            if alist[i] > alist[i+1]:
                temp = alist[i]
                alist[i] = alist[i+1]
                alist[i+1] = temp

def selectionSort(alist):
    for fillslot in range(len(alist)-1,0,-1):
        positionOfMax = 0
        for location in range(1,fillslot+1):
            if alist[location] > alist[positionOfMax]:
                positionOfMax = location
        temp = alist[fillslot]
        alist[fillslot] = alist[positionOfMax]
        alist[positionOfMax] = temp

def insertionSort(alist):
    for index in range(1,len(alist)):
        currentvalue = alist[index]
        position = index

        while position>0 and alist[position-1]>currentvalue:
            alist[position] = alist[position-1]
            position = position-1

        alist[position] = currentvalue

def mergeSort(alist):
    if len(alist) > 1:
        mid = len(alist) // 2
        lefthalf = alist[:mid]
        righthalf = alist[mid:]

        mergeSort(lefthalf)
        mergeSort(righthalf)

        i = 0
        j = 0
        k = 0

        while i<len(lefthalf) and j<len(righthalf):
            if lefthalf[i] < righthalf[j]:
                alist[k] = lefthalf[i]
                i += 1
            else:
                alist[k] = righthalf[j]
                j += 1
            k += 1

        while i < len(lefthalf):
            alist[k] = lefthalf[i]
            i += 1
            k += 1

        while j < len(righthalf):
            alist[k] = righthalf[j]
            j += 1
            k += 1

def quickSort(alist):
    quickSortHelper(alist,0,len(alist)-1)

def quickSortHelper(alist,first,last):
    if first < last:
        splitpoint = partition(alist,first,last)
        quickSortHelper(alist,first,splitpoint-1)
        quickSortHelper(alist,splitpoint+1,last)

def partition(alist,first,last):
    pivotvalue = alist[first]
    leftmark = first + 1
    rightmark = last
    done = False

    while not done:

        while leftmark <= rightmark and alist[leftmark] <= pivotvalue:
            leftmark += 1

        while alist[rightmark] >= pivotvalue and rightmark >= leftmark:
            rightmark -= 1

        if rightmark < leftmark:
            done = True
        else:
            temp = alist[leftmark]
            alist[leftmark] = alist[rightmark]
            alist[rightmark] = temp

    temp = alist[first]
    alist[first] = alist[rightmark]
    alist[rightmark] = temp

    return rightmark

def generateArray(sortType,n):  #function to generate array depending on what kind of array needs to be made
    arr=[]
    if(sortType=="Random"):
        arr=[i for i in range(n)]
        random.shuffle(arr)
    elif(sortType=="Sorted"):
        arr=[i for i in range(n)]
    elif(sortType=="Reverse"):
        arr=[i for i in range(n)]
        arr.reverse()
    elif(sortType=="Almost sorted"):
        arr=[i for i in range(n)]
        for i in range(0,n//10):
            index=random.randint(0,len(arr)-1)
            index2=random.randint(0,len(arr)-1)
            temp=arr[index2]
            arr[index2]=arr[index]
            arr[index]=temp
    return arr

def avg(arr):   #function that calculates the avg time for a passed list
    total=0
    for i in range(0,5):
        total+=arr[i]
    return format((total/5), '.6f')

def sortingList(sortType):
    arr=[]
    n=10
    bTime=[]    #lists to hold the time of each type of sort
    sTime=[]
    iTime=[]
    mTime=[]
    qTime=[]
    for i in range(0,3):
        for j in range(0,5):    #for loop to do each sort and account for the time taken for each sort
            arr=generateArray(sortType,n)
            startTime = time.perf_counter()
            bubbleSort(arr)
            endTime = time.perf_counter()
            elapsedTime = endTime - startTime
            bTime.append(elapsedTime)

            arr=generateArray(sortType,n)
            startTime = time.perf_counter()
            selectionSort(arr)
            endTime = time.perf_counter()
            elapsedTime = endTime - startTime
            sTime.append(elapsedTime)

            arr=generateArray(sortType,n)
            startTime = time.perf_counter()
            insertionSort(arr)
            endTime = time.perf_counter()
            elapsedTime = endTime - startTime
            iTime.append(elapsedTime)

            arr=generateArray(sortType,n)
            startTime = time.perf_counter()
            mergeSort(arr)
            endTime = time.perf_counter()
            elapsedTime = endTime - startTime
            mTime.append(elapsedTime)

            arr=generateArray(sortType,n)
            startTime = time.perf_counter()
            quickSort(arr)
            endTime = time.perf_counter()
            elapsedTime = endTime - startTime
            qTime.append(elapsedTime)
        n=n*10#after finishing a loop, increment n by *10
    index=0
    if(sortType=="Random"): #print function with proper format to display 
        print("Input type = Random")
    elif(sortType=="Sorted"):
        print("Input type = Sorted")
    elif(sortType=="Reverse"):
        print("Input type = Reverse")
    elif(sortType=="Almost sorted"):
        print("Input type = Almost sorted")
    print("                    avg time   avg time   avg time")
    print("   Sort function     (n=10)    (n=100)    (n=1000)")
    print("-----------------------------------------------------")
    avg10=avg(bTime[0:5])
    avg100=avg(bTime[5:10])
    avg1000=avg(bTime[10:])
    print("      bubbleSort    " + str(avg10) + "   " + str(avg100) + "   " + str(avg1000))
    avg10=avg(sTime[0:5])
    avg100=avg(sTime[5:10])
    avg1000=avg(sTime[10:])
    print("   selectionSort    " + str(avg10) + "   " + str(avg100) + "   " + str(avg1000))
    avg10=avg(iTime[0:5])
    avg100=avg(iTime[5:10])
    avg1000=avg(iTime[10:])
    print("   insertionSort    " + str(avg10) + "   " + str(avg100) + "   " + str(avg1000))
    avg10=avg(mTime[0:5])
    avg100=avg(mTime[5:10])
    avg1000=avg(mTime[10:])
    print("       mergeSort    " + str(avg10) + "   " + str(avg100) + "   " + str(avg1000))
    avg10=avg(qTime[0:5])
    avg100=avg(qTime[5:10])
    avg1000=avg(qTime[10:])
    print("       quickSort    " + str(avg10) + "   " + str(avg100) + "   " + str(avg1000))
    print()
    print()
    
def main():
    sortingList("Random")   #function calls of each type of array to sort
    sortingList("Sorted")
    sortingList("Reverse")
    sortingList("Almost sorted")
main()
