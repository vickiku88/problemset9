# 6.00 Problem Set 9
#
# Name:
# Collaborators:
# Time:

from string import *

class Shape(object):
    def area(self):
        raise AttributeException("Subclasses should override this method.")

class Square(Shape):
    def __init__(self, h):
        """
        h: length of side of the square
        """
        self.side = float(h)
    def area(self):
        """
        Returns area of the square
        """
        return self.side**2
    def __str__(self):
        return 'Square with side ' + str(self.side)
    def __eq__(self, other):
        """
        Two squares are equal if they have the same dimension.
        other: object to check for equality
        """
        return type(other) == Square and self.side == other.side
    
    def search(self):
        return "Square"

class Circle(Shape):
    def __init__(self, radius):
        """
        radius: radius of the circle
        """
        self.radius = float(radius)
    def area(self):
        """
        Returns approximate area of the circle
        """
        return 3.14159*(self.radius**2)
    def __str__(self):
        return 'Circle with radius ' + str(self.radius)
    def __eq__(self, other):
        """
        Two circles are equal if they have the same radius.
        other: object to check for equality
        """
        return type(other) == Circle and self.radius == other.radius
   
    def search(self):
        return "Circle"

#
# Problem 1: Create the Triangle class
#
## TO DO: Implement the `Triangle` class, which also extends `Shape`.
class Triangle(Shape):
    def __init__(self,b,h):
        self.base = float(b)
        self.height = float(h)

    def area(self):
        return (self.base * self.height)*0.5

    def __str__(self):
        return 'Triangle with base of ' + str(self.base)+ ' and height of '+ str(self.height)

    def __eq__(self, other):
        #maybe needs some work
        return type(other) == Triangle and self.base == other.base and self.height == other.height

    def increaseHeight(self, h_to_inc_by):
        self.height += h_to_inc_by
    
    def search(self):
        return "Triangle"



#
# Problem 2: Create the ShapeSet class
#
## TO DO: Fill in the following code skeleton according to the
##    specifications.

class ShapeSet:

    def __init__(self):
        """
        Initialize any needed variables
        """
        ## TO DO
        self.setOfShapes = set()


    def addShape(self, sh):
        """
        Add shape sh to the set; no two shapes in the set may be
        identical
        sh: shape to be added
        """
        ## TO DO
        if sh in self.setOfShapes:
            print "we already have this"
        else:
            self.setOfShapes.add(sh)
            #print "added shape " + sh.__str__()


    def __iter__(self):
        """
        Return an iterator that allows you to iterate over the set of
        shapes, one shape at a time
        """
        ## TO DO
        for shape in self.setOfShapes:
            print shape.__str__()

    def __str__(self):
        """
        Return the string representation for a set, which consists of
        the string representation of each shape, categorized by type
        (circles, then squares, then triangles)
        """
        ## TO DO
        return sorted(setOfShapes)






        
#
# Problem 3: Find the largest shapes in a ShapeSet
#
def findLargest(shapes):
    """
    Returns a tuple containing the elements of ShapeSet with the
       largest area.
    shapes: ShapeSet
    """
    ## TO DO
    largestTuple = ()
    largest = ()
    print shapes.setOfShapes
    for shape in shapes.setOfShapes:
        if not largestTuple or shape.area() > largest.area():
            largestTuple = (shape,)
            largest = shape
        elif shape.area() == largest.area():
            largestTuple = largestTuple + (shape,)
        else:
            largestTuple





        """if shape.search() == "Triangle":
            print "Triangle"


        if shape.search() == "Circle":
            print "Circle"


        if shape.search() == "Square":
            print "Square"
        """
    return largestTuple






#
# Problem 4: Read shapes from a file into a ShapeSet
#
def readShapesFromFile(filename):
    """
    Retrieves shape information from the given file.
    Creates and returns a ShapeSet with the shapes found.
    filename: string
    """
    ## TO DO
    currentShapeSet = ShapeSet()
    useShape = ""

    with open(filename,"r") as f:
        file_contents = f.read()
        shapes_list = file_contents.split()
        print shapes_list

    for shapes in shapes_list:
        useShape = shapes.split(',')[0]
        #attribute1 = shapes.split(',')[1]

        if useShape == "circle":
            attribute1 = shapes.split(',')[1]
            #currentShapeSet.addShape(Circle(shapes.split[1]))
            x = Circle(attribute1)
            print x
        elif useShape == "triangle":
            attribute1 = shapes.split(',')[1]
            attribute2 = shapes.split(',')[2]
            print Triangle(attribute1,attribute2)

            #currentShapeSet.addShape(Triangle(shapes.split[1], shapes.split[2]))
        elif useShape == "square":
            attribute1 = shapes.split(',')[1]

            #currentShapeSet.addShape(Square(shapes.split[1]))
            print Square(attribute1)
        else:
            return nil
        
    return currentShapeSet







"""vicki = Triangle(3,4)
carson = Circle(5)
winston = Square(3)
darvin = Square(4)
vickiSet = ShapeSet()
vickiSet.addShape(vicki)
vickiSet.addShape(carson)
vickiSet.addShape(winston)
vickiSet.addShape(darvin)

print findLargest(vickiSet)


ss = ShapeSet()
ss.addShape(Triangle(3,8))
ss.addShape(Circle(1))
ss.addShape(Triangle(4,6))

largest = findLargest(ss)

for e in largest: print e
"""
y =  readShapesFromFile("shapes.txt")

