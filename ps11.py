# Problem Set 11: Simulating robots
# Name:
# Collaborators:
# Time:

import math
import random
import matplotlib.pyplot as plt


# === Provided classes

class Position(object):
    """
    A Position represents a location in a two-dimensional room.
    """
    def __init__(self, x, y):
        """
        Initializes a position with coordinates (x, y).

        x: a real number indicating the x-coordinate
        y: a real number indicating the y-coordinate
        """
        self.x = x
        self.y = y
        #print x,y
    def getX(self):
        return self.x
    def getY(self):
        return self.y
    def getNewPosition(self, angle, speed):
        """
        Computes and returns the new Position after a single clock-tick has
        passed, with this object as the current position, and with the
        specified angle and speed.

        Does NOT test whether the returned position fits inside the room.

        angle: integer representing angle in degrees, 0 <= angle < 360
        speed: positive float representing speed

        Returns: a Position object representing the new position.
        """
        old_x, old_y = self.getX(), self.getY()
        # Compute the change in position
        delta_y = speed * math.cos(math.radians(angle))
        delta_x = speed * math.sin(math.radians(angle))

        # Add that to the existing position
        new_x = old_x + delta_x
        new_y = old_y + delta_y

        return Position(new_x, new_y)



# === Problems 1 and 2

class RectangularRoom(object):
    """
    A RectangularRoom represents a rectangular region containing clean or dirty
    tiles.

    A room has a width and a height and contains (width * height) tiles. At any
    particular time, each of these tiles is either clean or dirty.
    """
    def __init__(self, width, height):
        """
        Initializes a rectangular room with the specified width and height.
        Initially, no tiles in the room have been cleaned.

        width: an integer > 0
        height: an integer > 0
        """
        # TODO: Your code goes here
        self.width = width
        self.height = height
        self.tilesDict = {}

        for w in range(self.width):
            for h in range(self.height):
                self.tilesDict[(w,h)] = 0




    def cleanTileAtPosition(self, pos):
        """
        Mark the tile under the position POS as cleaned.
        Assumes that POS represents a valid position inside this room.

        pos: a Position
        """
        # TODO: Your code goes here
        posX = pos.getX()
        posY = pos.getY()
        self.tilesDict[(posX,posY)] = 1



    def isTileCleaned(self, m, n):
        """
        Return True if the tile (m, n) has been cleaned.

        Assumes that (m, n) represents a valid tile inside the room.

        m: an integer
        n: an integer
        returns: True if (m, n) is cleaned, False otherwise
        """
        # TODO: Your code goes here
        return self.tilesDict[(m,n)] == 1
    def getNumTiles(self):
        """
        Return the total number of tiles in the room.

        returns: an integer
        """
        # TODO: Your code goes here
        return len(self.tilesDict.items())
    def getNumCleanedTiles(self):
        """
        Return the total number of clean tiles in the room.

        returns: an integer
        """
        # TODO: Your code goes here
        return sum(x == 1 for x in self.tilesDict.values())
    def getRandomPosition(self):
        """
        Return a random position inside the room.

        returns: a Position object.
        """
        # TODO: Your code goes here
        listitem = random.choice(list(self.tilesDict))
        return Position(listitem[0],listitem[1])
    def isPositionInRoom(self, pos):
        """
        Return True if POS is inside the room.

        pos: a Position object.
        returns: True if POS is in the room, False otherwise.
        """
        # TODO: Your code goes here
        posX = pos.getX()
        posY = pos.getY()

        if self.width > posX and self.height > posY:
            return True 
        else: 
            return False 
        




class BaseRobot(object):
    """
    Represents a robot cleaning a particular room.

    At all times the robot has a particular position and direction in
    the room.  The robot also has a fixed speed.

    Subclasses of BaseRobot should provide movement strategies by
    implementing updatePositionAndClean(), which simulates a single
    time-step.
    """
    def __init__(self, room, speed):
        """
        Initializes a Robot with the given speed in the specified
        room. The robot initially has a random direction d and a
        random position p in the room.

        The direction d is an integer satisfying 0 <= d < 360; it
        specifies an angle in degrees.

        p is a Position object giving the robot's position.

        room:  a RectangularRoom object.
        speed: a float (speed > 0)
        """
        # TODO: Your code goes here
        self.roomObj = room
        self.speed = speed

        self.dirAngle = 0
        self.p = self.roomObj.getRandomPosition()


    def getRobotPosition(self):
        """
        Return the position of the robot.

        returns: a Position object giving the robot's position.
        """
        # TODO: Your code goes here
        pos = self.p
        return pos

    def getRobotDirection(self):
        """
        Return the direction of the robot.

        returns: an integer d giving the direction of the robot as an angle in
        degrees, 0 <= d < 360.
        """
        # TODO: Your code goes here
        self.dirAngle = random.randint(0,360)

        return self.dirAngle
    def setRobotPosition(self, position):
        """
        Set the position of the robot to POSITION.

        position: a Position object.
        """
        # TODO: Your code goes here
        posX = position.getX()
        posY = position.getY()
        self.p.x = posX
        self.p.y = posY  
    def setRobotDirection(self, direction):
        """
        Set the direction of the robot to DIRECTION.

        direction: integer representing an angle in degrees
        """
        # TODO: Your code goes here
        self.dirAngle = direction



class Robot(BaseRobot):
    """
    A Robot is a BaseRobot with the standard movement strategy.

    At each time-step, a Robot attempts to move in its current
    direction; when it hits a wall, it chooses a new direction
    randomly.
    """
    def updatePositionAndClean(self):
        """
        Simulate the passage of a single time-step.

        Move the robot to a new position and mark the tile it is on as having
        been cleaned.
        """
        # TODO: Your code goes here
        roomObj = self.roomObj

        speed = self.speed
        position = self.getRobotPosition()
        angle = self.getRobotDirection()

        newPosition = position.getNewPosition(angle, speed)

        
        while roomObj.isPositionInRoom(newPosition) == False:
            newAngle = self.getRobotDirection()
            print ">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>",newAngle
            newPosition = position.getNewPosition(newAngle, speed)
        

        self.setRobotPosition(newPosition)
        roomObj.cleanTileAtPosition(newPosition)


        

# === Problem 3

def runSimulation(num_robots, speed, width, height, min_coverage, num_trials,
                  robot_type, visualize):
    """
    Runs NUM_TRIALS trials of the simulation and returns a list of
    lists, one per trial. The list for a trial has an element for each
    timestep of that trial, the value of which is the percentage of
    the room that is clean after that timestep. Each trial stops when
    MIN_COVERAGE of the room is clean.

    The simulation is run with NUM_ROBOTS robots of type ROBOT_TYPE,
    each with speed SPEED, in a room of dimensions WIDTH x HEIGHT.

    Visualization is turned on when boolean VISUALIZE is set to True.

    num_robots: an int (num_robots > 0)
    speed: a float (speed > 0)
    width: an int (width > 0)
    height: an int (height > 0)
    min_coverage: a float (0 <= min_coverage <= 1.0)
    num_trials: an int (num_trials > 0)
    robot_type: class of robot to be instantiated (e.g. Robot or
                RandomWalkRobot)
    visualize: a boolean (True to turn on visualization)
    """
    # TODO: Your code goes here
    list_of_lists = []
    room = RectangularRoom(width,height)
    coverage = 0
    robot = Robot(room,speed)

    for num in range(num_trials):
        justList = []
        min_coverage = min_coverage / num_robots

        while coverage < min_coverage:

            robot.updatePositionAndClean()
            total = float(room.getNumTiles())
            clean = float(room.getNumCleanedTiles())
            coverage = clean / total
            justList.append(coverage)
        list_of_lists.append(justList)
        return list_of_lists





# === Provided function
    




def computeMeans(list_of_lists):
    """
    Returns a list as long as the longest list in LIST_OF_LISTS, where
    the value at index i is the average of the values at index i in
    all of LIST_OF_LISTS' lists.

    Lists shorter than the longest list are padded with their final
    value to be the same length.
    """
    # Find length of longest list
    longest = 0
    for lst in list_of_lists:
        if len(lst) > longest:
           longest = len(lst)
    # Get totals
    tots = [0]*(longest)
    for lst in list_of_lists:
        for i in range(longest):
            if i < len(lst):
                tots[i] += lst[i]
            else:
                tots[i] += lst[-1]
    # Convert tots to an array to make averaging across each index easier
    tots = pylab.array(tots)
    # Compute means
    means = tots/float(len(list_of_lists))
    return means


# === Problem 4
def showPlot1():
    """
    Produces a plot showing dependence of cleaning time on room size.
    """
    # TODO: Your code goes here

def showPlot2():
    """
    Produces a plot showing dependence of cleaning time on number of robots.
    """
    # TODO: Your code goes here

def showPlot3():
    """
    Produces a plot showing dependence of cleaning time on room shape.
    """
    # TODO: Your code goes here

def showPlot4():
    """
    Produces a plot showing cleaning time vs. percentage cleaned, for
    each of 1-5 robots.
    """
    # TODO: Your code goes here


# === Problem 5

class RandomWalkRobot(BaseRobot):
    """
    A RandomWalkRobot is a robot with the "random walk" movement
    strategy: it chooses a new direction at random after each
    time-step.
    """
    # TODO: Your code goes here


# === Problem 6

def showPlot5():
    """
    Produces a plot comparing the two robot strategies.
    """
    # TODO: Your code goes here




def runAvg(width,height, num_robots):
    avg = runSimulation(num_robots, 1.0, width, height, 0.75, 30, Robot, False) 
    return len(avg[0])

listAvg = []
for num in range(1,10):
    avg = runAvg(25,25,num)
    listAvg.append(avg)

plt.plot(listAvg, 'ro')
plt.xlabel('robots')
plt.ylabel('average time')
plt.show()


"""
print runAvg(5,5,1)
print runAvg(10,10,1)
print runAvg(20,20,1)
print runAvg(25,25,1)

plt.plot([5^2, 10^2, 20^2, 25^2],[ runAvg(5,5,1),
 runAvg(10,10,1),
 runAvg(20,20,1),
 runAvg(25,25,1)], 'ro')
plt.xlabel('room area')
plt.ylabel('average time')
plt.show()
"""