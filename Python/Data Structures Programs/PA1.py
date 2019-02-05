import turtle


#Insertion_Sort: takes one parameter, a list of Rectangle objects
#Uses insertion sort to sort the list in place from highest z value
# to lowest.
#Doesn't return anything.
def Insertion_Sort(shapels):
    for j in range(1, len(shapels)):
        key = shapels[j]
        i = j - 1
        while i >= 0 and shapels[i].d < key.d:
            shapels[i + 1] = shapels[i]
            i = i - 1
        shapels[i + 1] = key

#Rectangle class, turtle graphics, and test case setup
#You shouldn't change any of the code below, but do read it.

#Rectangle class.  Represents a single rectangle on the turtle canvas
class Rectangle:
    #self.x: x coord of the Rectangle's lower left corner
    #self.y: y coord of the Rectangle's lower left corner.
    #self.d: depth of the Rectangle: higher values represent Rectangles
    #   further in the background
    #self.w: extent of the Rectangle in the x direction
    #self.l: extent of the Rectangle in the y direction
    #self.c: String representing the color of the Rectangle
    #self.id: Unique string identifier for object
    def __init__(self,xpos,ypos,depth,width,length,color,name):
        self.x = xpos
        self.y = ypos
        self.d = depth
        self.w = width
        self.l = length
        self.c = color
        self.id = name
    #Draw method: takes in a Turtle object and draws the Rectangle
    def draw(self,turt):
        turt.penup()
        turt.setpos(self.x,self.y)
        turt.color(self.c)
        turt.begin_fill()
        turt.pendown()
        for i in range(2):
            turt.forward(self.w)
            turt.left(90)
            turt.forward(self.l)
            turt.left(90)
        turt.end_fill()
    #String representation of Rectangle object: depth:identifier
    def __repr__(self):
        return str(self.d)+":"+self.id

#Set up turtle graphics
turtle.hideturtle()
t = turtle.Turtle()
t.speed(10)
s = turtle.getscreen()
s.tracer(1,1)

#Create Rectangles in scene
background = Rectangle(-400,-300,60,800,600,"lime green","background")
building = Rectangle(-150,-50,41,300,150,"ivory4","building")
door = Rectangle(50,-50,40,35,70,"burlywood4","door")
line1 = Rectangle(-200,-145,20,50,5,"yellow","line1")
line2 = Rectangle(150,-145,20,50,5,"yellow","line2")
leaves1 = Rectangle(-200,10,30,110,80,"dark green","leaves1")
leaves2 = Rectangle(90,-70,10,220,150,"dark green","leaves2")
river = Rectangle(-400,70,50,800,100,"blue","river")
road = Rectangle(-400,-200,21,800,100,"black","road")
trunk1 = Rectangle(-160,-70,31,30,110,"brown","trunk1")
trunk2 = Rectangle(170,-230,11,60,220,"brown","trunk2")
window = Rectangle(-110,-10,40,80,60,"grey20","window")


#Create test case lists
scene1 = []
scene2 = [river]
scene3 = [trunk2,road]
scene4 = [leaves2,trunk2,line2,line1,road,leaves1,trunk1,window,
          door,building,river,background]
scene5 = [background,river,building,door,window,trunk1,leaves1,
          road,line1,line2,trunk2,leaves2]
scene6 = [building,background,door,line1,line2,leaves1,leaves2,
             river,road,trunk1,trunk2,window]

#List of test cases and their correct sorted versions
tests = [scene1,scene2,scene3,scene4,scene5,scene6]
correct = [[],
           [river],
           [road,trunk2],
           [background,river,building,window,door,trunk1,leaves1,
          road,line2,line1,trunk2,leaves2],
           [background,river,building,door,window,trunk1,leaves1,
          road,line1,line2,trunk2,leaves2],
           [background,river,building,door,window,trunk1,leaves1,
          road,line1,line2,trunk2,leaves2]]


#Run test cases, check whether sorted list correct
count = 0

for i in range(len(tests)):
    try:
        print("Running: Insertion_Sort(",tests[i],")\n")
        Insertion_Sort(tests[i])
        print("Expected:",correct[i],"\n\nGot:",tests[i])
        if (correct[i] == tests[i]):
            count=count+1
        else:
            print("FAIL: Incorrect output")
    except Exception as e:
        print("FAIL: Error ", e)
    print()

print(count,"out of",len(tests),"tests passed.")

#Draw Rectangles in list in sequence.
for element in scene6:
    element.draw(t)
t.hideturtle()