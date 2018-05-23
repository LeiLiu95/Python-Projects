#  File: numberPath.py
#  Description: Depth first search in number grid
#  Student's Name: Lei Liu
#  Student's UT EID: LL28379
#  Course Name: CS 313E 
#  Unique Number: 51915
#
#  Date Created: 4/9/17
#  Date Last Modified:  4/14/17

class State():
    def __init__(self, grid, path, start_row, start_col, total, targetValue, grid_row, grid_col, end_row, end_col):
        # initialize variables for State class
        self.grid = grid
        self.path = path
        self.start_row = start_row
        self.start_col = start_col
        self.sum = total
        self.grid_row = grid_row
        self.grid_col = grid_col
        self.end_row = end_row
        self.end_col = end_col
        self.targetValue=targetValue
        
    def makeGrid(self, data):
        print(data)
        self.grid.append(data)

    def init(self): #initializes the maze for starting values
        self.sum += int(self.grid[self.start_row][self.start_col])  #initial sum of maze is the starting point
        self.path.append(self.grid[self.start_row][self.start_col]) #starting spot will be accounted for in path history
        self.grid[self.start_row][self.start_col] = None    #set starting point to none
        return

    def printMaze(self):
        temp_Grid = ""
        for row in range(self.grid_row+1):  #returns a string for the grid
            temp_Grid += "      "
            for col in range(self.grid_col+1):
                if(len(str(self.grid[row][col]))==1):   #if cases for spacing and format
                    temp_Grid += str(self.grid[row][col]) + "    "
                elif(len(str(self.grid[row][col]))==2):
                    temp_Grid += str(self.grid[row][col]) + "   "
                elif(len(str(self.grid[row][col]))==3):
                    temp_Grid += str(self.grid[row][col]) + "  "
                else:
                     temp_Grid += str(self.grid[row][col]) + " "
            temp_Grid+="\n"
        return temp_Grid

    def moveFunc(self, step):   #function to move in a specific direction
        newGrid = [r[:] for r in self.grid]
        step.grid = newGrid
        newPath = []
        for i in range(len(self.path)): #iterates through previous steps
            newPath.append(self.path[i])
        newPath.append(int(step.grid[step.start_row][step.start_col]))  #add new step
        step.path = newPath
        step.sum = self.sum + int(step.grid[step.start_row][step.start_col])
        step.grid[step.start_row][step.start_col] = None
        print ("Problem is now: ")  #prints the current problem
        print (step)            #prints the grid and returns it
        return step
        #returns the next step for the maze
    
    def __str__(self):
        return str("   Grid:\n" + str(self.printMaze()) + "   history: " + str(self.path) + "\n" + "   start point: (" + str(self.start_row) + "," + str(self.start_col) + ")\n" + "   sum so far: " + str(self.sum) + "\n")

def solve(grid):    #recursive function to solve the given maze problem
    print("Is this a goal state?")
    #base case, if current location is at the end location and sum is equal to target then return true
    if(grid.start_row == grid.end_row and grid.start_col == grid.end_col and grid.sum == grid.sum):
        print("Solution found!")
        print(str(grid.path))
        return (str(grid.path))
    else:
        if grid.sum > grid.targetValue: #if sum is past of value then return false
            print("No. Target exceeded:  abandoning path")
            return None
        #move right
        print("No.  Can I move right?")
        if(isValid(grid.grid, grid.start_row, grid.start_col + 1, grid.grid_row, grid.grid_col)):
            newMaze = State(grid.grid, grid.path, grid.start_row, grid.start_col + 1, grid.sum, grid.targetValue, grid.grid_row, grid.grid_col, grid.end_row, grid.end_col)
            newMaze = grid.moveFunc(newMaze)
            #creates a new state and calls the moveFunc and then tracks the history of moving
            result = solve(newMaze)
            if result != None:
                return newMaze.path
            else:
                pass
        #repeat the same moves for the rest of the directions
        #move up
        print ("No.  Can I move up?")
        if(isValid(grid.grid, grid.start_row - 1, grid.start_col, grid.grid_row, grid.grid_col)):
            newMaze = State(grid.grid, grid.path, grid.start_row - 1, grid.start_col, grid.sum, grid.targetValue, grid.grid_row, grid.grid_col, grid.end_row, grid.end_col)
            newMaze = grid.moveFunc(newMaze)
            result = solve(newMaze)
            if result != None:
                return newMaze.path
            else:
                pass
        #move down
        print ("No.  Can I move down?")
        if(isValid(grid.grid, grid.start_row + 1, grid.start_col, grid.grid_row, grid.grid_col)):
            newMaze = State(grid.grid, grid.path, grid.start_row + 1, grid.start_col, grid.sum, grid.targetValue, grid.grid_row, grid.grid_col, grid.end_row, grid.end_col)
            newMaze = grid.moveFunc(newMaze)
            result = solve(newMaze)
            if result != None:
                return newMaze.path
            else:
                pass
        #move Left
        print ("No.  Can I Move left?")
        if(isValid(grid.grid, grid.start_row, grid.start_col - 1, grid.grid_row, grid.grid_col)):
            newMaze = State(grid.grid, grid.path, grid.start_row, grid.start_col - 1, grid.sum, grid.targetValue, grid.grid_row, grid.grid_col, grid.end_row, grid.end_col)
            newMaze = grid.moveFunc(newMaze)
            result = solve(newMaze)
            if result != None:
                return newMaze.path
            else:
                pass
        print ("Couldn't move in any direction. Backtracking.")
        return None

def isValid(grid, check_row, check_col, grid_row, grid_col): #checks if the location is valid or not
    if(check_row>=0 and check_row<=grid_row) and (check_col>=0 and check_col<=grid_col):
        if(grid[check_row][check_col] == None): #if the location is None then return False
            return False
        print("Yes!")   #otherwise the location is valid and return True
        print()
        return True
    return False

def getDigits(param):   #function that parses the .txt files and returns them in a list
    items=[]
    word=""
    for i in param:
        if(i!=" "):
            word+=i
        else:
           items.append(int(word))
           word=""
    items.append(int(word))
    return items

def main():
    grid_Input = open("pathdata.txt", "r")  #opens the file to be read
    check=False
    grid = []
    for i in grid_Input:    #the initial values from .txt file will be grabbed
        i = i.strip()       #and added to a list to be analyzed
        if(check==False):
            data = getDigits(i)
            check=True
        else:
            grid_Data = getDigits(i)
            grid.append(grid_Data)
    targetValue = data[0]   #sets all the given values into the respective variable names
    grid_rows = data[1]-1 #reduce size by 1 for 0 index
    grid_cols = data[2]-1 #reduce size by 1 for 0 index
    start_row = data[3]
    start_col = data[4]
    end_row = data[5]
    end_col = data[6]
    problem = State(grid, [], start_row, start_col, 0, targetValue, grid_rows, grid_cols, end_row, end_col)
    #create the initial state of the maze using the State class
    problem.init()
    print(problem) #print the start of the the initial maze
    solve(problem)    
    
    grid_Input.close()
main()
