import traceback, turtle, math

#Takes as input a list of ChromaticCrusader objects, representing the
#list of vertices in the graph, and a FriendshipMatrix object, representing
#the weight matrix.
#You must implement Prim's algorithm or Kruskal's algorithm to construct
# a minimum spanning tree.  Every time you want to add an edge to the tree,
# you must call friend_matrix.chromatic_call(c1,c2), where c1 and c2 are
# the Crusaders (vertices) that you want to be connected.  Once an edge has
# been added it cannot be removed, so be sure that you don't use
# chromatic_call until you are sure that there should be an edge between
# c1 and c2 in the final tree.
def gather_friends(crusader_list,friend_matrix):
    crusader_list[0].key = 0
    build_min_heap(crusader_list)
    while len(crusader_list) != 0:
        crusader = heap_extract_min(crusader_list)
        if crusader.prev != None:
            friend_matrix.chromatic_call(crusader.prev, crusader)
        for friend in crusader.friends:
            if friend in crusader_list:
                weight = crusader.distance[friend.num]
                if weight < friend.key:
                    friend.prev = crusader
                    i = crusader_list.index(friend)
                    heap_decrease_key(crusader_list, i, weight)

rainbow = ["red","orange","yellow","green","blue","indigo","purple"]
#ChromaticCrusader class
#This class represents a single vertex within the distance graph.
#Instance variables:
#   self.num: number between 0 and # of total Crusaders - 1.
#       Represents the index of this Crusader within the list/matrix
#   self.color: what color this crusader will be represented as on
#       the graph.
#   self.friends: a list of other ChromaticCrusader objects to which
#       this object is adjacent (the weight of their edge is not infinity)
#   self.distance: a list of integers representing the edge weights
#       between this and every other crusader, in order of index number.

#The next two instance variables are only relevant to Prim's algorithm
#   self.key: used for Prim's algorithm: shortest distance from any node
#       currently in the tree to this node.  Used for priority queue
#   self.prev: pi in the textbook, predecessor pointer for Prim's algorithm

#The next two instance variables are only relevant to Kruskal's algorithm
#   self.p: Parent pointer for set operations, as shown in section 21.3
#   self.rank: rank value for set operations, as shown in section 21.3
class ChromaticCrusader:
    def __init__(self,num,color):
        self.num = num
        self.color = color
        self.friends = []
        self.distance = []

        self.key = float("inf")
        self.prev = None

        self.p = self
        self.rank = 0

    #Set operations from section 21.3: used for Kruskal's algorithm
    #Feel free to edit these or ignore them entirely.
    def find_set(self):
        if self != self.p:
            self.p = (self.p).find_set()
        return self.p

    def link(self,other):
        if self.rank > other.rank:
            other.p = self
        else:
            self.p = other
            if self.rank == other.rank:
                other.rank += 1

    def union(self,other):
        (self.find_set()).link(other.find_set())

    #Draw this node in the distance graph
    def draw(self):
        t = turtle.Turtle()
        t.hideturtle()
        t.speed(0)
        t.fillcolor(self.color)
        t.penup()
        totCCs = len(self.distance)
        angle = (self.num/totCCs)*math.pi*2
        self.x = math.cos(angle)*250
        self.y = math.sin(angle)*250
        t.setpos(self.x,self.y-30)
        t.pendown()
        t.begin_fill()
        t.circle(30)
        t.end_fill()


    #Draw an edge from this node to other in the distance graph
    #   with weight d.  call is a boolean: if False the edge is
    #   drawn normally (black), if True it's drawn multicolored
    def draw_edge(self,other,d,call):
        if d == float("inf"):
            return
        t = turtle.Turtle()
        t.hideturtle()
        t.fillcolor(self.color)
        t.penup()
        t.speed(1)
        dx = other.x - self.x
        dy = other.y - self.y
        dist = (dx*dx+dy*dy)**(0.5)
        sx = dx*(30/dist)
        sy = dy*(30/dist)
        startx = self.x+sx
        starty = self.y+sy
        endx = other.x-sx
        endy = other.y-sy
        halfx = (startx+endx)/2
        halfy = (starty+endy)/2
        if call:
            turtle.tracer(0)
            t.pensize(4)
            t.setpos(self.x,self.y)
            t.pendown()
            dx = (other.x-self.x)/100
            dy = (other.y-self.y)/100
            for i in range(100):
                t.color(rainbow[i%7])
                t.setpos(self.x+dx*(i+1),self.y+dy*(i+1))
            t.color("black")
            turtle.tracer(1)
        else:
            t.pensize(2)
            t.setpos(startx,starty)
            t.pendown()
            t.setpos(endx,endy)
        t.penup()
        t.setpos(halfx,halfy-10)
        t.fillcolor("white")
        t.color("white")
        t.begin_fill()
        t.circle(10)
        t.end_fill()
        t.color("black")
        t.write(d,align="center",font=("Arial",12,"normal"))

    #String representation of a ChromaticCrusader object: index #:color
    def __repr__(self):
        return str(self.num)+":"+self.color

    #Check equality between two ChromaticCrusader objects.
    def __eq__(self,other):
        return type(self) == type(other) and \
               self.color == other.color


#Min-priority queue implementation: used for Prim's algorithm
#Feel free to edit these, or don't use them at all.
def parent(i):
    return int((i-1)/2)

def min_heapify(Q,i):
    l = 2*i+1
    r = 2*i+2
    smallest = i
    if l < len(Q) and Q[l].key < Q[smallest].key:
        smallest = l
    if r < len(Q) and Q[r].key < Q[smallest].key:
        smallest = r
    if i != smallest:
        Q[i],Q[smallest] = Q[smallest],Q[i]
        min_heapify(Q,smallest)

def build_min_heap(Q):
    for i in range(len(Q)//2-1,-1,-1):
        min_heapify(Q,i)

def heap_extract_min(Q):
    if len(Q) == 1:
        return Q.pop()
    minElement = Q[0]
    Q[0] = Q.pop()
    min_heapify(Q,0)
    return minElement

def heap_decrease_key(Q,i,key):
    Q[i].key = key
    while i > 0 and Q[parent(i)].key > Q[i].key:
        Q[i],Q[parent(i)] = Q[parent(i)],Q[i]
        i = parent(i)


#  DO NOT EDIT BELOW THIS LINE

#FriendshipMatrix class
#Instance variables:
#   crusader_list: a list of ChromaticCrusader objects, ordered by
#       index number
#   distance: a matrix of integers representing the weight of each
#       edge in the graph.  Infinity for edges that don't exist.
#   tree: the final output MST, an adjacency matrix of 0's and 1's.
#
class FriendshipMatrix:
    def __init__(self,crusader_list,distance):
        self.crusader_list = crusader_list
        n = len(self.crusader_list)
        self.tree = [[0 for i in range(n)] for i in range(n)]
        self.distance = distance
        for c1 in self.crusader_list:
            c1.distance = distance[c1.num]
            for i in range(n):
                if distance[c1.num][i] != float("inf"):
                    c1.friends.append(self.crusader_list[i])
    def draw_everything(self):
        for c1 in self.crusader_list:
            c1.draw()
        for c1 in self.crusader_list:
            for c2 in self.crusader_list:
                c1.draw_edge(c2,c1.distance[c2.num],False)

    #chromatic_call: used to add one edge to the final MST.
    #Takes as input two ChromaticCrusader objects, draws a colorful
    #edge between them, and adds the edge to the MST.
    def chromatic_call(self,crusader1,crusader2):
        #Just in case the user passes indexes instead of objects
        if type(crusader1) == int:
            crusader1 = self.crusader_list[crusader1]
        if type(crusader2) == int:
            crusader2 = self.crusader_list[crusader2]
        dist = crusader1.distance[crusader2.num]
        if self.tree[crusader1.num][crusader2.num] == 1:
            print("Edge already added")
            return
        crusader1.draw_edge(crusader2,dist,True)
        self.tree[crusader1.num][crusader2.num] = 1
        self.tree[crusader2.num][crusader1.num] = 1
    def __eq__(self,other):
        return self.tree == other.tree

#Test cases

i = float("inf")

def make_crusader_list(n):
    red = ChromaticCrusader(0,"red")
    yellow = ChromaticCrusader(1,"yellow")
    blue = ChromaticCrusader(2,"blue")
    orange = ChromaticCrusader(3,"orange")
    indigo = ChromaticCrusader(4,"indigo")
    green = ChromaticCrusader(5,"green")
    violet = ChromaticCrusader(6,"purple")
    full_list = [red,yellow,blue,orange,indigo,green,violet]
    return full_list[:n]


crusader_list1 = make_crusader_list(3)
distances = [[i,1,2],
             [1,i,i],
             [2,i,i]]
fm1 = FriendshipMatrix(crusader_list1,distances)

crusader_list2 = make_crusader_list(3)
distances = [[i,3,1],
             [3,i,2],
             [1,2,i]]
fm2 = FriendshipMatrix(crusader_list2,distances)

crusader_list3 = make_crusader_list(5)
distances = [[i,i,1,2,i],
             [i,i,i,3,4],
             [1,i,i,i,5],
             [2,3,i,i,i],
             [i,4,5,i,i]]
fm3 = FriendshipMatrix(crusader_list3,distances)

crusader_list4 = make_crusader_list(5)
distances = [[i,7,8,3,i],
             [7,i,i,12,4],
             [8,i,i,i,i],
             [3,12,i,i,1],
             [i,4,i,1,i]]
fm4 = FriendshipMatrix(crusader_list4,distances)

crusader_list5 = make_crusader_list(7)
distances = [[i,i,23,i,i,24,10],
             [i,i,1,i,11,16,i],
             [23,1,i,i,i,6,25],
             [i,i,i,i,21,i,3],
             [i,11,i,21,i,20,i],
             [24,16,6,i,20,i,i],
             [10,i,25,3,i,i,i]]
fm5 = FriendshipMatrix(crusader_list5,distances)

crusader_list6 = make_crusader_list(7)
distances = [[i,16,17,i,i,i,20],
             [16,i,i,i,4,8,11],
             [17,i,i,9,i,6,i],
             [i,i,9,i,1,7,i],
             [i,4,i,1,i,5,i],
             [i,8,6,7,5,i,17],
             [20,11,i,i,i,17,i]]
fm6 = FriendshipMatrix(crusader_list6,distances)


crusader_lists = [crusader_list1,crusader_list2,crusader_list3,
       crusader_list4,crusader_list5,crusader_list6]
friendship_matrices = [fm1,fm2,fm3,fm4,fm5,fm6]
tree1 = [[0,1,1],
         [1,0,0],
         [1,0,0]]
tree2 = [[0,0,1],
         [0,0,1],
         [1,1,0]]
tree3 = [[0,0,1,1,0],
         [0,0,0,1,1],
         [1,0,0,0,0],
         [1,1,0,0,0],
         [0,1,0,0,0]]
tree4 = [[0,0,1,1,0],
         [0,0,0,0,1],
         [1,0,0,0,0],
         [1,0,0,0,1],
         [0,1,0,1,0]]
tree5 = [[0,0,0,0,0,0,1],
         [0,0,1,0,1,0,0],
         [0,1,0,0,0,1,0],
         [0,0,0,0,1,0,1],
         [0,1,0,1,0,0,0],
         [0,0,1,0,0,0,0],
         [1,0,0,1,0,0,0]]
tree6 = [[0,1,0,0,0,0,0],
         [1,0,0,0,1,0,1],
         [0,0,0,0,0,1,0],
         [0,0,0,0,1,0,0],
         [0,1,0,1,0,1,0],
         [0,0,1,0,1,0,0],
         [0,1,0,0,0,0,0]]
correct = [tree1,tree2,tree3,tree4,tree5,tree6]


#Run test cases, check whether final MST correct
count = 0
tom = turtle.Turtle()
try:
    for i in range(len(correct)):
        print("\n---------------------------------------\n")
        print("TEST #",i+1)
        turtle.delay(0)

        turtle.tracer(0)
        turtle.resetscreen()

        friendship_matrices[i].draw_everything()
        turtle.tracer(1)
        turtle.delay(5)
        gather_friends(crusader_lists[i],friendship_matrices[i])

        print("Expected:",correct[i],"\nGot     :",friendship_matrices[i].tree)
        assert friendship_matrices[i].tree == correct[i], "Tree incorrect"
        print("Test Passed!\n")
        count += 1
except AssertionError as e:
    print("\nFAIL: ",e)

except Exception:
    print("\nFAIL: ",traceback.format_exc())


print(count,"out of",len(correct),"tests passed.")
