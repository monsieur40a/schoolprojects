import traceback, turtle, math

#optimize_hyperspace_routes: takes in two arguments:
#   star_list is a list of Star objects (nodes), in order of index.
#   jump_times is a matrix of edge weights for the graph.
#This function must use the Floyd-Warshall or Johnson's algorithm to compute
#   the shortest path from each star to every other star.  You may use whatever
#   method you want to detect negative cycles.
#If there is a negative cycle in the graph, this function must return a list of
#   Star objects that compose the cycle in an order that forms the cycle.  The
#   first object in this list should be the same as the last.
#If there is not a negative cycle in the graph, this function must reutrn a matrix
#   (that is, a list of lists) of integers, containing the total weights for the
#   shortest path from every vertex to every other vertex.  You do not actually have
#   to return the paths themselves, just the final total path weight for each pairing.
def optimize_hyperspace_routes(star_list,jump_times):
    #TODO: Implement this function
    for i in range(len(star_list) - 1):
        for row in jump_times:
            for col in row:
                relax(row, col, star_list, jump_times)
    found = False
    for row in jump_times:
        for col in row:
            if star_list[row].get_dist() > star_list[col].get_dist() + jump_times[row][col]:
                found = True
                break
    if (not found):
        return jump_times
    prev = star_list[row].prev
    A = [star_list[row].prev]
    duplicate = False
    while(not duplicate):
        prev = star_list[row].prev
        if (prev not in A):
            prev = star_list[row].prev
        else:
            duplicate = True
    B = [prev]
    original = prev
    next = prev.prev
    while (next != original):
        B.append(next)
        next = prev.prev
    B.append(next)
    return B

def relax(row, col, star_list, jump_times):
    if (star_list[col].get_dist() > star_list[row].get_dist() + jump_times[row][col]):
        star_list[col].set_dist(star_list[row].get_dist() + jump_times[row][col])
        star_list[col].prev = star_list[row]


#  DO NOT EDIT BELOW THIS LINE

rainbow = ["red","orange","yellow","green","blue","brown","purple"]
#Star class
#This class represents a single vertex within the Star Map.
#Instance variables:
#   self.num: number between 0 and # of total Stars - 1.
#       Represents the index of this Star within the list/matrix
#   self.color: what color this star will be represented as on
#       the graph.
#   self.adj: a list of other Star objects to which
#       this object is adjacent (the weight of their edge is not infinity)
#   self.jump_times: a list of integers representing the edge weights
#       between this and every other Star, in order of index number.
#   self.__dist: the .d instance variable from the textbook algorithm, representing
#       the total distance from the start node to this node.  Private, so can only be
#       accessed through getter and setter method below.
#   self.prev: previous Star in shortest path from start to here.
#   self.x, self.y: where this star will be drawn on the star map.

class Star:
    def __init__(self,num,color,x,y,dist):
        self.num = num
        self.color = color
        self.adj = []
        self.jump_times = []
        self.__dist = dist
        self.x = x
        self.y = y
        self.prev = None

    #Getter and setter for the private variable __dist, which represents the
    #distance this node is from the start node.  Not needed for Floyd-Warshall,
    #may be useful for debugging Johnson's.
    def set_dist(self,dist):
        self.__dist = dist
        self.draw(self.t)

    def get_dist(self):
        return self.__dist

    #Draw this node on the Star Map
    def draw(self,t):
        self.t = t
        t.hideturtle()
        t.speed(0)
        t.color(self.color)
        t.penup()
        t.setpos(self.x,self.y-15)
        t.pendown()
        t.begin_fill()
        t.circle(15)
        t.end_fill()
        if(self.color not in ["yellow","orange"]):
            t.color("white")
        else:
            t.color("black")
        if self.__dist != float("inf"):
            t.write(self.__dist,align="center",font=("Arial",20,"normal"))



    #Draw an edge from this node to other on the Star Map.
    #   with weight d.  path is a boolean: if False the edge is
    #   drawn normally (white), if True it's drawn cyan
    #   directed indicates whether the path is one direction only.
    def draw_edge(self,t,other,d,path,directed):
        if d == float("inf") or self == other:
            return
        t.hideturtle()
        t.fillcolor(self.color)
        t.color("white")
        t.penup()
        t.speed(5)
        dx = other.x - self.x
        dy = other.y - self.y
        dist = (dx*dx+dy*dy)**(0.5)
        sx = dx*(15/dist)
        sy = dy*(15/dist)
        startx = self.x+sx
        starty = self.y+sy
        endx = other.x-sx
        endy = other.y-sy
        halfx = (startx+endx)/2
        halfy = (starty+endy)/2
        t.pensize(2)
        if directed:
            t.color("magenta")
            t.pensize(3)
        if path:
            t.color("cyan")
            t.pensize(4)

        t.setpos(startx,starty)
        t.pendown()
        t.setpos(endx,endy)
        if directed:
            angle = math.atan2(dy,dx)*180/math.pi
            t.seth(angle)
            t.right(135)
            t.forward(20)
            t.back(20)
            t.left(270)
            t.forward(20)
            t.back(20)
            t.seth(0)

        t.penup()
        t.setpos(halfx,halfy-10)
        t.fillcolor("black")
        t.color("black")
        t.begin_fill()
        t.circle(10)
        t.end_fill()
        t.color("white")
        if path:
            t.color("cyan")
        t.write(d,align="center",font=("Arial",15,"normal"))

    #String representation of a Star object: color
    def __repr__(self):
        return self.color

    #Check equality between two Star objects.
    def __eq__(self,other):
        return type(self) == type(other) and \
               self.color == other.color

#StarMap class
#Instance variables:
#   star_list: a list of Star objects, ordered by
#       index number
#   jump_times: a matrix of integers representing the weight of each
#       edge in the graph.  Infinity for edges that don't exist
#
class StarMap:
    def __init__(self,star_list,jump_times):
        self.star_list = star_list
        n = len(self.star_list)
        self.jump_times = jump_times
        for c1 in self.star_list:
            c1.jump_times = jump_times[c1.num]
            for i in range(n):
                if jump_times[c1.num][i] != float("inf"):
                    c1.adj.append(self.star_list[i])
    def draw_everything(self,t):
        for c1 in self.star_list:
            c1.draw(t)
        for c1 in self.star_list:
            for c2 in self.star_list:
                if c1.jump_times[c2.num] != c2.jump_times[c1.num]:
                    c1.draw_edge(t,c2,c1.jump_times[c2.num],False,True)
                else:
                    c1.draw_edge(t,c2,c1.jump_times[c2.num],False,False)

#Test case
i = float("inf")

def make_star_list(n):
    red = Star(0,"red",-256, 13,float("inf"))
    orange = Star(1,"orange",265, -70,float("inf"))
    yellow = Star(2,"yellow",12,215,float("inf"))
    green = Star(3,"green",68,12,float("inf"))
    blue = Star(4,"blue",-180,189,float("inf"))
    brown = Star(5,"brown",141,-96,float("inf"))
    violet = Star(6,"purple",-73,-183,float("inf"))
    full_list = [red,orange,yellow,green,blue,brown,violet]
    return full_list[:n]


star_list1 = make_star_list(2)
jump_times = [[0,2],
             [2,0]]
star_map1 = StarMap(star_list1,jump_times)

star_list2 = make_star_list(3)
jump_times = [[0,i,2],
             [-4,0,1],
             [2,1,0]]
star_map2 = StarMap(star_list2,jump_times)

star_list3 = make_star_list(4)
jump_times = [[0,1,3,4],
             [1,0,i,i],
             [3,-1,0,i],
             [4,i,-3,0]]
star_map3 = StarMap(star_list3,jump_times)

star_list4 = make_star_list(5)
jump_times = [[0,-7,-2,3,i],
             [i,0,6,12,4],
             [i,6,0,i,3],
             [3,12,i,0,i],
             [i,4,3,-1,0]]
star_map4 = StarMap(star_list4,jump_times)

star_list5 = make_star_list(6)
jump_times = [[0,i,i,6,2,16],
             [i,0,13,4,i,i],
             [i,13,0,-5,i,12],
             [6,4,i,0,7,2],
             [2,i,-2,7,0,i],
             [16,-1,12,2,i,0]]
star_map5 = StarMap(star_list5,jump_times)

star_list6 = make_star_list(7)
jump_times = [[0,26,-2,i,i,i,2],
             [26,0,i,i,i,8,i],
             [i,i,0,9,4,-6,i],
             [i,i,9,0,i,i,1],
             [i,i,4,i,0,i,i],
             [i,8,i,i,i,0,7],
             [2,i,-11,1,-6,7,0]]
star_map6 = StarMap(star_list6,jump_times)


star_lists = [star_list1,star_list2,star_list3,
       star_list4,star_list5,star_list6]
star_maps = [star_map1,star_map2,star_map3,star_map4,star_map5,star_map6]
time_limit = [2,4,4,7,12,21]
correct = [[[0,2],
             [2,0]],
           [Star(2,"yellow",12,215,3),
            Star(1,"orange",265, -70,12),
            Star(0,"red",-256, 13,0),
            Star(2,"yellow",12,215,3)],
           [[0,0,1,4],
            [1,0,2,5],
            [0,-1,0,4],
            [-3,-4,-3,0]],
           [Star(4,"blue",-180,189,2),
            Star(3,"green",68,12,9),
            Star(0,"red",-256, 23,0),
            Star(1,"orange",265, -70,12),
            Star(4,"blue",-180,189,2)],
           [[0, -4, 0, -5, 2, -3],
            [10, 0, 9, 4, 11, 6],
            [1, -4, 0, -5, 2, -3],
            [6, 1, 5, 0, 7, 2],
            [-1, -6, -2, -7, 0, -5],
            [8, -1, 7, 2, 9, 0]],
           [Star(6,"purple",-73,-183,2),
            Star(2,"yellow",12,215,3),
            Star(3,"green",68,12,9),
            Star(6,"purple",-73,-183,2)]]

#Run test cases, check whether final MST correct
count = 0

def draw_counter(t,i,color):
    t.penup()
    t.setpos(-100+i*10,-225)
    t.color(color)
    t.pendown()
    t.begin_fill()
    t.circle(5)
    t.end_fill()

time_counter = turtle.Turtle()
cyan_turtle = turtle.Turtle()
draw_turtle = turtle.Turtle()

try:
    for i in range(len(correct)):
        print("\n---------------------------------------\n")
        print("TEST #",i+1)
        turtle.delay(0)

        turtle.tracer(1)
        turtle.resetscreen()

        turtle.bgcolor("black")
        turtle.tracer(0)
        star_maps[i].draw_everything(draw_turtle)

        turtle.delay(0)
        copy_jump_times = [list(ls) for ls in star_maps[i].jump_times]
        routes = optimize_hyperspace_routes(list(star_lists[i]),copy_jump_times)

        print("Expected:",correct[i],"\nGot     :",routes)
        #Change this to turtle.tracer(0) if you want to speed up tests considerably
        turtle.tracer(1)
        assert routes != [], "Time matrix empty"
        assert type(routes[0]) in [list,Star], "Invalid return type"

        if type(routes[0]) == Star:
            total_time = 0
            draw_turtle.penup()
            draw_turtle.setpos(0,-250)
            draw_turtle.color("cyan")
            draw_turtle.write("NEGATIVE TIME LOOP FOUND!",align='center',font=('Arial',20,'normal'))
            for j in range(-1,len(routes)-1):
                from_v = routes[j]
                to_v = routes[j+1]
                time = star_maps[i].jump_times[from_v.num][to_v.num]
                if j != -1 or routes[-1] != routes[0]:
                    total_time += time
                from_v.draw_edge(draw_turtle,to_v,time,True,True)
            assert total_time < 0, "Negative time loop not actually negative, total time = "\
                   +str(total_time)
        elif type(routes[0]) == list:
            assert type(correct[i][0]) == list, "Negative time loop missed!"
            assert correct[i] == routes, "Final time matrix incorrect"


        print("Test Passed!\n")
        count += 1
except AssertionError as e:
    print("\nFAIL: ",e)

except Exception:
    print("\nFAIL: ",traceback.format_exc())


print(count,"out of",len(correct),"tests passed.")
