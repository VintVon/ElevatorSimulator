import tkinter as tk
from collections import deque

#Class that represents an elevator and its current state
class Elevator:
    
    #Constructor
    def __init__ (self):
        self.doorsOpened = False
        self.floor = 0
        self.numFloors = 5
        self.isMoving = False 
        self.queue = deque()
        self.direction = "None"
    
    #Getters
    def getDoorsOpened(self):
        return self.doorsOpened
    
    def getFloor(self):
        return self.floor
    
    def getMoving(self):
        return self.isMoving
    
    def getQueue(self):
        return self.queue
    
    def getDirection(self):
        return self.direction
    
    #Setters
    def setDoorsOpened(self, opened):
        self.doorsOpened = opened
    
    def setFloor(self, floor):
        self.floor = floor 
    
    def setMoving(self, value):
        self.isMoving = value
        
    def setDirection(self, direction):
        self.direction = direction
        
    #Methods
    
    #Add to queue
    def addToQueue(self, floor):
        self.queue.append(floor)
        
    #Remove from queue
    def popFromQueue(self):
        return self.queue.popleft()
        
    #Check if the queue is empty
    def queueIsEmpty(self):
        
        if len(self.queue) == 0:
            returnVal = True
        else: 
            returnVal = False
        
        return returnVal
    
    #Peek at the next floor without removing it from the queue
    def peekQueue(self):
        return self.queue[0]
    
    #Check if the elevator is moving down
    def isGoingDown(self):
        
        
        if self.direction == "Down":
            return True 
        else: 
            return False
        
    #Check if the elevator is moving up
    def isGoingUp(self):
        
        
        if self.direction == "Up":
            return True 
        else: 
            return False
    
    #Sort the queue from lowest to highest
    #For when the elevator is going up
    def sortQueueLowHigh(self):
        self.queue = deque(sorted(self.queue))
        
    #Sort the queue from highest to lowest
    #For when the elevator is going down
    def sortQueueHighLow(self):
        self.queue = deque(sorted(self.queue, reverse=True))
        
    #Function to move the elevator to a specific floor and perform state tracking
    #Only moving the elevator if the state permits
    #Function utilizes various helper functions to smoothen out the elevator's animations
    def move(self, floorNumber):
        
        
        #Calculate the distance between this floor and the floor the elevator needs to move to 
        floorDifference = Elevator.getFloor() - floorNumber
        numSteps = 200
        floorDistance =  150 * floorDifference
        stepDistance = floorDistance/numSteps
        
        #Get the direction that the elevator is moving in, and update the elevator's internal status
        self.getElevatorDirection(floorNumber)
        
        #Check if the elevator needs to change floors
        #If the elevator needs to change floors, check if the doors are opened
        if(floorDifference != 0):
            
            #If the elevator doors are opened, close them because the elevator needs to move
            if(Elevator.getDoorsOpened() == True):
                self.closeElevatorDoor()
                
                #Update the text on the tkinter canvas to showcase accurate elevator information
                canvas.itemconfig(elevatorStatus,text="Moving: Yes" if Elevator.getMoving() else "Moving: No")
                root.update()
                
        #For each step, move the elevator by an amount of totalDistance/numberOfSteps
        for i in range(numSteps):
            moveDistance(stepDistance)
            root.update()
            root.after(10)
            
        #Update the floor number that the elevator is on
        Elevator.setFloor(floorNumber)
        
        #Now that we are on a new floor, check if the doors are opened (they should not be), then open the door
        if(Elevator.getDoorsOpened() == False):
           self.openElevatorDoor()
           
           #Update the text on the tkinter canvas to showcase accurate elevator information
           canvas.itemconfig(elevatorStatus,text="Moving: Yes" if Elevator.getMoving() else "Moving: No")
           canvas.itemconfig(elevatorFloor,text=(f"Elevator Floor: {Elevator.getFloor()}"))
           root.update()

    #Function that optimizes the elevators next stops, meant to run after each Tkinter tick
    #Looks at direction elevator is moving to make a decision on how to sort floors
    def elevatorOptimizer(self, floorNumber):
        
        #Calculate the distance between this floor and the floor the elevator needs to move to 
        floorDifference = Elevator.getFloor() - floorNumber
        
        #Check if the elevator is moving up or down
        #IF the elevator is moving down, then sort the queue so that it can stop at the higher floors as it goes down
        #If the elevator is going up, then sort the queue so that it can stop at the lower levels as it goes up
        if(floorDifference < 0):
            
            Elevator.sortQueueLowHigh()
            
        elif(floorDifference > 0):
            
            Elevator.sortQueueHighLow()
            
        else:
            Elevator.setDirection("None")
            
            
        canvas.itemconfig(elevatorQueue,text=(f"Elevator Queue: {list(Elevator.getQueue())}"))
    
    #Function to get the elevators direction 
    def getElevatorDirection(self, floorNumber):
        
        #Calculate the distance between this floor and the floor the elevator needs to move to 
        floorDifference = Elevator.getFloor() - floorNumber
        
        #Check if the elevator is moving up or down
        #IF the elevator is moving down, set the state of the elevator as moving down
        #If the elevator is going up, set the state of the elevator as moving up
            
            Elevator.setDirection("Up")
         
            #Update the text on the tkinter canvas to showcase accurate elevator information
            canvas.itemconfig(elevatorDirection,text="Direction: Up" if Elevator.isGoingUp() else "Direction: Down" if Elevator.isGoingDown() else "Direction: None")
            
        elif(floorDifference > 0):
            
            Elevator.setDirection("Down")
            
            #Update the text on the tkinter canvas to showcase accurate elevator information
            canvas.itemconfig(elevatorDirection,text="Direction: Up" if Elevator.isGoingUp() else "Direction: Down" if Elevator.isGoingDown() else "Direction: None")
            
        else:
            Elevator.setDirection("None")
            
            #Update the text on the tkinter canvas to showcase accurate elevator information
            canvas.itemconfig(elevatorDirection,text="Direction: Up" if Elevator.isGoingUp() else "Direction: Down" if Elevator.isGoingDown() else "Direction: None")

    #Function to simulate opening the elevator door
    def openElevatorDoor(self):
        
        #The number of pixels the elevator should open to either side
        difference = 30
        
        #The number of increments the elevator door should take to reach the final pixel width
        numsteps = 20
        distanceStep = difference/numsteps
        
        #For each step, open the elevator doors by the step increment amount
        for i in range(numsteps):
            openElevatorDoorHelper(distanceStep)
            root.update()
            root.after(30)
            
        #Update the elevator flags to reflect a stopped elevator with open doors
        Elevator.setDoorsOpened(True)
        Elevator.setMoving(False)
        
        #Update the text on the tkinter canvas to showcase accurate elevator information
        canvas.itemconfig(elevatorDoors,text="Doors: Open" if Elevator.getDoorsOpened() else "Doors: Closed")
        
    #Function to simulate closing the elevator door
    def closeElevatorDoor(self):
        
        #The number of pixels the elevator should close from either side
        difference = 30
        
         #The number of increments the elevator door should take to reach the final pixel width
        numsteps = 20
        distanceStep = difference/numsteps
        
         #For each step, close the elevator doors by the step increment amount
        for i in range(numsteps):
            closeElevatorDoorHelper(distanceStep)
            root.update()
            root.after(30)
            
        #Update the elevator flags to reflect a stopped elevator with open doors
        Elevator.setDoorsOpened(False)
        Elevator.setMoving(True)
        
        #Update the text on the tkinter canvas to showcase accurate elevator information
        canvas.itemconfig(elevatorDoors,text="Doors: Open" if Elevator.getDoorsOpened() else "Doors: Closed")
        
                
#Helper function to move the elevator a certain distance (to make the animation look smoother)
def moveDistance(distance):
    canvas.move(elevator,0, distance)
    canvas.move(elevatorDoor, 0, distance)
    

#Function to extract the floor level from the button press
def buttonPress(event):
    
    #Looks at the button object that was pressed and extracts the number from the title of the button object
    buttonObj = event.widget
    floorValue = int(buttonObj["text"].split(":")[1].strip())
    print(floorValue)
    
    #Adds the floor that was pressed to the Elevator's internal floor queue
    Elevator.addToQueue(floorValue)
    
    #Update the text on the tkinter canvas to showcase accurate elevator information
    canvas.itemconfig(elevatorQueue,text=(f"Elevator Queue: {list(Elevator.getQueue())}"))
    
  

#Helper function to make the opening of the elevator door smoother
def openElevatorDoorHelper(openStepDistance):

    #Take the coordinates of the elevator and open by a small increment amount
    x1, y1, x2, y2 = canvas.coords(elevatorDoor)
    canvas.coords( elevatorDoor,  x1 - openStepDistance, y1, x2 + openStepDistance, y2)
    
    
#Helper function to make the closing of the elevator door smoother
def closeElevatorDoorHelper(openStepDistance):
    
    #Take the coordinates of the elevator and close by a small increment amount
    x1, y1, x2, y2 = canvas.coords(elevatorDoor)
    canvas.coords(elevatorDoor, x1 + openStepDistance, y1, x2 - openStepDistance, y2)

#Checks if the elevator queue is empty or not
def elevatorTick():
    
    #If the elevator is not moving and the floor queue has floors the elevator needs to go to
    if (Elevator.getMoving() == False and Elevator.queueIsEmpty() == False):
        
        #Optimize the elevator based on the direction that its moving before the elevator moves
        Elevator.elevatorOptimizer(Elevator.peekQueue())
        
        #Remove the floor from the queue and start moving to that floor
        Elevator.move(Elevator.popFromQueue())
        
    # Schedule this function to run again after 100 ms
    #Updaate the canvas to reflect the queue that has just been changed
    canvas.itemconfig(elevatorQueue,text=(f"Elevator Queue: {list(Elevator.getQueue())}"))
    root.after(1000, elevatorTick)
    

#Function to create the building around the elevator
def createBuilding(canvas):
    
    # Parameters
    floor_height = 150
    total_floors = 6
    elevator_x1 = 700
    elevator_x2 = 800
    floor0_bottom_y = 900  # bottom of floor 0 (aligns with your elevator base)
    floor0_top_y = floor0_bottom_y - floor_height  # top of floor 0
    building_left = 650
    building_right = 850
    
    # Calculate top of building (top of floor 5)
    building_top = floor0_bottom_y - floor_height * total_floors
    
    # Shaft background
    canvas.create_rectangle(elevator_x1, floor0_bottom_y, elevator_x2, building_top, fill="lightgray", outline="")
    
    # Building outer frame
    canvas.create_rectangle(building_left, floor0_bottom_y, building_right, building_top, outline="black", width=4)
    
    # Draw floor lines and labels
    for i in range(total_floors):
        y = floor0_bottom_y - i * floor_height
        canvas.create_line(building_left, y, building_right, y, fill="gray", dash=(4, 2))
        canvas.create_text(620, y, text=str(i), font=("Arial", 14))
        

#Create the tkinter interface

#Create the canvas
root = tk.Tk()
root.title("Elevator interface")
root.geometry("1000x1000")
canvas = tk.Canvas(root, width=900, height=900, bg="Grey")
canvas.pack(pady=10)


#Create building
createBuilding(canvas)

#Create the elevator 
elevator = canvas.create_rectangle(800,900, 700, 750, fill="Green")
elevatorDoor = canvas.create_rectangle(750,900, 750, 750, fill="Black")
Elevator = Elevator()

#Create the elevator information panel
infoBox = canvas.create_rectangle(0,0,400,400, fill="Dark Grey")
elevatorStatus = canvas.create_text(60,10, text="Moving: Yes" if Elevator.getMoving() else "Moving: No", font=("Arial", 14), fill="black")
elevatorDoors = canvas.create_text(10, 40, text="Doors: Open" if Elevator.getDoorsOpened() else "Doors: Closed", font=("Arial", 14), fill="black", anchor="w")
elevatorDirection = canvas.create_text(10, 70, text="Direction: Up" if Elevator.isGoingUp() else "Direction: Down" if Elevator.isGoingDown() else "Direction: None", font=("Arial", 14), fill="black", anchor="w")
elevatorFloor = canvas.create_text(80,100, text=(f"Elevator Floor: {Elevator.getFloor()}"), font=("Arial", 14), fill="black")
elevatorQueue = canvas.create_text(10,130, text=(f"Elevator Queue: {list(Elevator.getQueue())}"), font=("Arial", 14), fill="black",anchor="w")


#Main Elevator environment 
#Open the elevator door to start
Elevator.openElevatorDoor()
elevatorTick()

#Create the control buttons
controls = tk.Frame(root)
controls.pack()

#Button for floor 0
floor0 = tk.Button(controls, text="Floor: 0")
floor0.grid(row=0, column=0,padx=10, pady=5)
floor0.bind("<Button-1>", buttonPress)


#Button for floor 1
floor1 = tk.Button(controls, text="Floor: 1")
floor1.grid(row=0, column=10,padx=10, pady=5)
floor1.bind("<Button-1>", buttonPress)


#Button for floor 2
floor2 = tk.Button(controls, text="Floor: 2")
floor2.grid(row=0, column=20,padx=10, pady=5)
floor2.bind("<Button-1>", buttonPress)


#Button for floor 3
floor3 = tk.Button(controls, text="Floor: 3")
floor3.grid(row=0, column=30,padx=10, pady=5)
floor3.bind("<Button-1>", buttonPress)


#Button for floor 4
floor4 = tk.Button(controls, text="Floor: 4")
floor4.grid(row=0, column=40,padx=10, pady=5)
floor4.bind("<Button-1>", buttonPress)


#Button for floor 5
floor5 = tk.Button(controls, text="Floor: 5")
floor5.grid(row=0, column=50,padx=10, pady=5)
floor5.bind("<Button-1>", buttonPress)

    
root.mainloop()