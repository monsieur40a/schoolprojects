import traceback, turtle

#Takes as input a Square object node in a graph of Square nodes.
# This will always be the Square node representing (0,0), the start position
#Performs BFS until the goal Square is found (the Square with val == 2).
#Returns a list containing each Square node in the path from the start
# (0,0) to the goal node, inclusive, in order from start to goal.
def find_path(start_node):
    start_node.set_color("gray")
    start_node.depth = 0
    start_node.prev = None
    # Finish the BFS and return the path from start_node to the goal
    queue = [start_node]
    result = []
    while (queue != []):
        u = queue.pop(len(queue) - 1)
        for vertex in u.adj:
            if (vertex.get_color() == "white"):
                vertex.set_color("gray")
                vertex.depth = u.depth + 1
                vertex.prev = u
                queue = [vertex] + queue
                if (vertex.val == 2):
                    result = [vertex]
                    while (vertex != start_node):
                        vertex = vertex.prev
                        result = [vertex] + result
                    break
        u.set_color("black")
    return result



#  DO NOT EDIT BELOW THIS LINE

#Square class
#A single square on the grid, which is a single node in the graph.
#Has several instance variables:
# self.t: The turtle object used to draw this square
# self.x: The integer x coordinate of this square
# self.y: The integer y coordinate of this square
# self.val: An integer, which is 0 if this square is blocked, 1
#   if it's a normal, passable square, and 2 if it's the goal.
# self.adj: A list representing all non-blocked squares adjacent
#   to this one. (This is the node's adjacency list)
# self.__color: A private string representing the color of the square
#   Must be accessed using set_color and get_color because it's private
#   The color of the square is purple if it's a blocked square.
#   Otherwise, it starts as white, and then progresses to grey and then
#   black according to the BFS algorithm.
# self.depth: An integer representing the depth of the node within BFS
# self.prev: A Square object pointing to the node from which this node
#   was discovered from within BFS: the pi variable in the textbook
class Square:
    def __init__(self,x,y,val,t):
        self.t = t
        self.x = x
        self.y = y
        self.val = val
        self.adj = []
        if self.val:
            self.__color = "white"
        else:
            self.__color = "purple"
        self.depth = float("inf")
        self.prev = None

    #Getters and setters for color variable.  You MUST use these rather
    #  than trying to change color directly: it causes the squares to
    #  actually update color within the graphics window.
    def set_color(self,color):
        if color != self.__color:
            self.__color = color
            self.draw()
    def get_color(self):
        return self.__color

    #Draws the square
    def draw(self):
        t = self.t
        t.hideturtle()
        t.speed(0)
        t.pencolor("blue")
        if self.__color == "purple":
            t.pencolor("purple")

        if self.val != 2:
            t.fillcolor(self.__color)
        else:
            t.fillcolor("blue")
        t.penup()
        t.setpos(self.x-.5,self.y-.5)
        t.pendown()
        t.begin_fill()
        for i in range(4):
            t.forward(1)
            t.left(90)
        t.end_fill()

    #String representation of a Square object: (x,y)
    def __repr__(self):
        return "("+str(self.x)+","+str(self.y)+")"

    #Check equality between two Square objects.
    def __eq__(self,other):
        return type(self) == type(other) and \
               self.x == other.x and self.y == other.y

#Takes as input a 2D list of numbers and a turtle object
#Outputs a 2D list of Square objects, which have their adjacency
#  lists initialized to all adjacent Square objects that aren't
#  blocked (so their val isn't 0).
def grid_to_squares(grid,t):
    square_grid = []
    for j in range(len(grid)):
        square_row = []
        for i in range(len(grid[j])):
            square_row.append(Square(i,j,grid[j][i],t))
        square_grid.append(square_row)
    for j in range(len(grid)):
        for i in range(len(grid[j])):
            adj = []
            if j+1 < len(grid) and grid[j+1][i]:
                adj.append(square_grid[j+1][i])
            if i+1 < len(grid[j]) and grid[j][i+1]:
                adj.append(square_grid[j][i+1])
            if j-1 >= 0 and grid[j-1][i]:
                adj.append(square_grid[j-1][i])
            if i-1 >= 0 and grid[j][i-1]:
                adj.append(square_grid[j][i-1])
            square_grid[j][i].adj = adj
    return square_grid

#Draws the entire grid of Square objects.
def draw_grid(square_grid):
    for j in range(len(square_grid)):
        for i in range(len(square_grid[j])):
            square_grid[j][i].draw()

#Test cases
square_turtle = turtle.Turtle()
square_turtle.hideturtle()
square_turtle.speed(0)
square_turtle.pencolor("blue")
map0 = grid_to_squares(
    [[1,2],
     [0,0]],square_turtle)
map1 = grid_to_squares(
    [[1, 0, 2],
        [1, 0, 1],
        [1, 1, 1]],square_turtle)
map2 = grid_to_squares(
    [[1,1,1,1,1,1,1],
     [1,1,1,1,1,1,1],
     [1,1,1,0,0,0,0],
     [1,1,1,0,2,1,1],
     [1,1,1,0,1,1,1],
     [1,1,1,1,1,1,1],
     [1,1,1,1,1,1,1]],square_turtle)
map3 = grid_to_squares(
    [[1,1,0,0,0,0,0,0,0,0],
    	[1,1,1,0,1,1,1,1,1,0],
    	[0,1,1,0,1,0,1,1,1,0],
    	[0,1,1,1,1,0,1,1,1,0],
    	[0,1,0,0,0,0,0,0,1,0],
    	[0,1,1,0,1,2,1,1,1,0],
    	[0,0,1,0,1,0,1,0,1,0],
    	[0,0,1,0,1,0,1,1,1,0],
    	[0,1,1,1,1,1,1,1,1,0],
    	[0,0,0,0,0,0,0,0,0,0]],square_turtle)

path0 = [map0[0][0],
         map0[0][1]]
path1 = [map1[0][0],
         map1[1][0],
         map1[2][0],
         map1[2][1],
         map1[2][2],
         map1[1][2],
         map1[0][2]]
path2 = [map2[0][0],
         map2[1][0],
         map2[2][0],
         map2[3][0],
         map2[4][0],
         map2[5][0],
         map2[5][1],
         map2[5][2],
         map2[5][3],
         map2[5][4],
         map2[4][4],
         map2[3][4]]
path3 = [map3[0][0],
         map3[1][0],
         map3[1][1],
         map3[2][1],
         map3[3][1],
         map3[4][1],
         map3[5][1],
         map3[5][2],
         map3[6][2],
         map3[7][2],
         map3[8][2],
         map3[8][3],
         map3[8][4],
         map3[7][4],
         map3[6][4],
         map3[5][4],
         map3[5][5]]
tests = [map0,map1,map2,map3]
correct = [path0,path1,path2,path3]


#Run test cases, check whether output path correct
count = 0

import random
try:
    for i in range(len(tests)):
        print("\n---------------------------------------\n")
        print("TEST #",i+1)
        turtle.resetscreen()
        turtle.setworldcoordinates(-1,-1,len(tests[i][0]),len(tests[i]))
        turtle.delay(0)
        square_grid = tests[i]

        turtle.tracer(0)
        draw_grid(square_grid)

        turtle.tracer(1)
        pathlst = find_path(square_grid[0][0])
        if i == 0:
            turtle.delay(1)
        else:
            turtle.speed(i)

        tom = turtle.Turtle()
        tom.speed(1)
        tom.color("green")
        tom.shape("turtle")
        tom.left(90)
        for square in pathlst:
            tom.goto(square.x,square.y)
        if i < 3:
            print("Expected:",correct[i],"\nGot     :",pathlst)
        assert pathlst == correct[i], "Path incorrect"
        print("Test Passed!\n")
        count += 1
except AssertionError as e:
    print("\nFAIL: ",e)

except Exception:
    print("\nFAIL: ",traceback.format_exc())


print(count,"out of",len(tests),"tests passed.")
