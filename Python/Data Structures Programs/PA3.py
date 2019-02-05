import traceback

#Takes as input the index of a heap node i
#Returns index of parent node
def parent(i):
    return int((i-1)/2)

#Takes as input the index of a heap node i
#Returns index of left child node
def left(i):
    return 2*i+1

#Takes as input the index of a heap node i
#Returns index of right child node
def right(i):
    return 2*i+2

#Takes as input a Heap object A consisting of Task objects
#  and an index i
#Assuming that all descendents of the node at index i have
#  the property that they have a priority greater than or equal
#  to their children, this function enforces that same condition
#  on the node at index i.
#WARNING: be sure you check whether the node's left and right
#children exist based on A.heap_size, not len(A), since not all
#elements of the array will be part of the heap.
def max_heapify(A,i):
    left_ = left(i)
    right_ = right(i)
    if left_ <= A.heap_size - 1 and A[left_].priority > A[i].priority:
        largest = left_
    else:
        largest = i
    if right_ <= A.heap_size - 1 and A[right_].priority > A[largest].priority:
        largest = right_
    if largest != i:
        temp = A[i]
        A[i] = A[largest]
        A[largest] = temp
        max_heapify(A, largest)


#Takes as input a Heap object A consisting of Task objects
#Increases A.heap_size to encompass all elements in the
#  inherited list, and enforces the property that all
#  nodes have a priority value greater than or equal to
#  the priority of their children.
def build_max_heap(A):
    A.heap_size = len(A)
    for i in range(int(len(A)/2)-1,-1,-1):
        max_heapify(A,i)

#Takes as input a Heap object consisting of Task objects
#Returns the Task with the highest priority
def heap_maximum(A):
    if A.heap_size > 0:
        return A[0]
    return None

#Takes as input a Heap object consisting of Task objects
#Removes the Task of highest priority from the Heap, and
#  returns it.
#Returns None (without throwing an error) if the Heap contains no Tasks
def heap_extract_max(A):
    if A.heap_size < 1:
        return None
    maximum = A[0]
    A[0] = A[A.heap_size - 1]
    A.heap_size = A.heap_size - 1
    max_heapify(A,0)
    return maximum


#Takes as input a Heap of Task objects A, an index of that
#  Heap i, and a number new_priority.
#Increases the priority of the Task at index i within Heap A
#  to new_priority, and adjusts the Heap accordingly to
#  maintain the max-heap property.
#Immediately returns None if new_priority is less than the
#  target Task's current priority, without throwing an error.
def heap_increase_key(A,i,new_priority):
    if new_priority < A[i].priority:
        return None
    A[i].priority = new_priority
    while i > 0 and A[parent(i)].priority < A[i].priority:
        temp = A[i]
        A[i] = A[parent(i)]
        A[parent(i)] = temp
        i = parent(i)


#NOTE: max_heap_insert is a bit different than the textbook implementation
#Rather than taking as an argument a key, it takes as an argument the
#Task object you want to input.  Since heap_increase_key still works
#on a numerical key, you'll need to be careful that you're actually
#putting a new Task into the heap and not just overwriting an existing
#Task's priority number.

#Takes as input a Heap of Task objects A, and a Task object task.
#Inserts task into the Heap A, while maintaining the
#  max-heap property.
def max_heap_insert(A,task):
    A.heap_size = A.heap_size + 1
    A[A.heap_size - 1] = task
    heap_increase_key(A, A.heap_size - 1, task.priority)



#  DO NOT EDIT BELOW THIS LINE

#Heap class: inherits from list.
#Essentially this is a normal Python list, except with an extra
#instance variable heap_size.  This is implemented similarly to the
#textbook, where the "array" componenet can have more than heap_size
#elements, but only the first heap_size elements are considered to
#be part of the heap and are required to have the max-heap property.
class Heap(list):
    #Initialize a Heap.  Takes two inputs: array is the the list of
    #  Task objects, not necessarily all in max-heap format, and
    #  heap_size is the number of elements that are actually within
    #  the "heap" part of the array (usually 0 to start)
    def __init__(self,array,heap_size):
        self.heap_size = heap_size
        super().__init__(array)
    #Overloading the [] operator.  There is a point in the
    #  max_heap_insert code in the textbook where the psuedocode increases
    #  the heap_size by 1 and inserts an element there without checking
    #  whether the underlying array has room.  We avoid that problem
    #  by allowing indexing one past the end of the array to be interpreted
    #  as simply appending.
    def __setitem__(self,key,value):
        if key == len(self):
            self.append(value)
        else:
            super().__setitem__(key,value)
    #String representation of Heap objects.  We display the actual heap
    #  part of the array as surrounded by angle brackets; anything in
    #  the array but not in the heap is added after the ~~~End of Heap~~~
    #  marker.
    def __repr__(self):
        return "[<"+str(self[:self.heap_size])[1:-1]+\
               ">\n~~~End of Heap~~~"+str(self[self.heap_size:])[1:]
    #Heap equality: we only care that the elements that are in the heap
    #  section of the array match: those outside don't count.
    def __eq__(self,other):
        return (self[:self.heap_size] == other[:other.heap_size])




#Task class
#Each task has two instance variables:
#   self.description is a string describing what the task is
#   self.priority is a number representing the importance of the
#      task (higher values are more important)
class Task:
    def __init__(self,description,priority):
        self.description = description
        self.priority = priority
    def __repr__(self):
        return "\n"+str(self.priority) + ": " + self.description
    def __eq__(self,other):
        return type(self) == type(other) and \
               self.description == other.description and \
               self.priority == self.priority



#Test cases:

t1 = Task("'Accidentally' run into love interest",76)
t2 = Task("Brood over inner darkness",61)
t3 = Task("Lunch with Powerdude and Megagal",61)
t4 = Task("Pick up Laundry",89)
t5 = Task("Go to boring normal job as alter-ego",65)
t6 = Task("Comic relief with useless sidekick",1)
t7 = Task("Help clean up collateral damage",84)
t8 = Task("Receive key to city",33)
t9 = Task("Prevent bank robbery",96)
t10 = Task("Training montage",46)

t11 = Task("Take a nap",20)
t12 = Task("Defeat King Explosion Murder", 20)
t13 = Task("Walk Ultradog the Annhilator", 20)
t14 = Task("Escape elaborate deathtrap", 97)
t15 = Task("Respond to fanmail",16)

#Duplicate objects, in case originals corrupted by student code
d1 = Task("'Accidentally' run into love interest",76)
d2 = Task("Brood over inner darkness",61)
d3 = Task("Lunch with Powerdude and Megagal",61)
d4 = Task("Pick up Laundry",89)
d5 = Task("Go to boring normal job as alter-ego",65)
d6 = Task("Comic relief with useless sidekick",1)
d7 = Task("Help clean up collateral damage",84)
d8 = Task("Receive key to city",33)
d9 = Task("Prevent bank robbery",96)
d10 = Task("Training montage",46)

d11 = Task("Take a nap",20)
d12 = Task("Defeat King Explosion Murder", 20)
d13 = Task("Walk Ultradog the Annhilator", 20)
d14 = Task("Escape elaborate deathtrap", 97)
d15 = Task("Respond to fanmail",16)

count = 0


try:
    print("Day 1: 6 Initial Tasks.  Building Priority Queue")

    # TEST 1: build_max_heap
    todo = Heap([t8,t6,t2,t10,t5,t3],0)
    print("TEST #1: build_max_heap/max_heapify")
    print("Running: build_max_heap(",todo,")\n")
    build_max_heap(todo)
    correct = Heap([d5,d10,d2,d8,d6,d3],6)
    print("Expected Heap:",correct,"\n\nGot:",todo)
    assert todo == correct, "Heap incorrect after build_max_heap"
    count = count+1

    print("\n---------------------\n")


    # TEST 2: heap_maximum
    print("TEST #2: heap_maximum")
    print("Running: heap_maximum(",todo,")\n")
    topPriority = heap_maximum(todo)
    correctOut = d5
    print("Expected Output:",correctOut,"\n\nGot:",topPriority)
    assert topPriority == correctOut,"heap_maximum output incorrect"
    count = count+1

    print("\n---------------------\n")


    # TEST 3 and 4: heap_extract_max
    print("TEST #3: heap_extract_max output")
    correct = Heap([d3,d10,d2,d8,d6,d3],5)

    print("Running: heap_extract_max(",todo,")\n")
    topPriority = heap_extract_max(todo)
    correctOut = d5
    print("Expected Output:",correctOut,"\n\nGot:",topPriority)
    assert topPriority == correctOut,"heap_extract_max output incorrect"
    count = count+1

    print("\nTEST #4: heap_extract_max resulting heap")
    print("\nExpected Heap:",correct,"\n\nGot:",todo)
    assert todo == correct, "Heap incorrect after heap_extract_max"
    count = count+1
    print("\n---------------------\n")


    # TEST 5: heap_increase_key
    print("TEST #5: heap_increase_key")
    d2 = Task("Brood over inner darkness",90)
    correct = Heap([d2,d10,d3,d8,d6,d3],5)

    print("Running: heap_increase_key(",todo,"2, 90)\n")
    heap_increase_key(todo,2,90)


    print("Expected Heap:",correct,"\n\nGot:",todo)
    assert todo == correct, "heap_increase_key output incorrect"
    count = count+1

    print("\n---------------------\n")


    #TEST 6: max_heap_insert
    print("TEST #6: max_heap_insert")
    correct = Heap([d9,d10,d2,d8,d6,d3],6)

    print("Running: max_heap_insert(",todo,",",t9,")\n")
    max_heap_insert(todo,t9)

    print("Expected Heap:",correct,"\n\nGot:",todo)
    assert todo == correct, "max_heap_insert resulting heap incorrect"
    count = count+1

    print("\n---------------------\n")


    #TEST 7
    print("\nTEST #7")
    correct = Heap([d7,d10,d3,d8,d6,d3,d4],5)

    print("Inserting Task:",t4,"\n")
    max_heap_insert(todo,t4)
    print("Epicperson seeks a task to complete!")
    topPriority = heap_extract_max(todo)
    print("Expected Output:",d9,"\n\nGot:",topPriority)
    assert topPriority == d9, "heap_extract_max output incorrect"
    count = count+1


    #TEST 8
    print("\nTEST #8")
    print("\nEpicperson seeks a task to complete!")
    topPriority = heap_extract_max(todo)
    print("Expected Output:",d2,"\n\nGot:",topPriority)
    assert topPriority == d2, "heap_extract_max output incorrect"
    count = count+1


    #TEST 9
    print("\nTEST #9")
    print("\nInserting Task:",t7,"\n")
    max_heap_insert(todo,t7)
    print("Epicperson seeks a task to complete!")
    topPriority = heap_extract_max(todo)

    print("Expected Output:",d4,"\n\nGot:",topPriority)
    assert topPriority == t4, "heap_extract_max output incorrect"
    count = count+1


    #TEST 10
    print("\nTEST #10")
    print("\nExpected Heap:",correct,"\n\nGot:",todo)
    assert todo == correct, "Final heap structure incorrect"
    count = count+1
    print("\n---------------------\n")


    #TEST 11 and 12
    correct = Heap([d15,d15,d15],1)
    print("Day 2: No initial Tasks")
    print("Building empty Priority Queue")
    todo = Heap([],0)
    print("Running build_max_heap on empty heap")
    build_max_heap(todo)
    print("Epicperson seeks a task to complete! (underflow, should return None)")
    topPriority = heap_extract_max(todo)
    print("Got:",topPriority)
    print("Inserting Task",t11)
    max_heap_insert(todo,t11)
    print("Epicperson seeks a task to complete!")
    topPriority = heap_extract_max(todo)
    print("Got:",topPriority)
    print("Epicperson seeks a task to complete! (underflow, should return None)")
    topPriority = heap_extract_max(todo)
    print("Got:",topPriority)
    print("Inserting Task",t12)
    max_heap_insert(todo,t12)
    print("Inserting Task",t13)
    max_heap_insert(todo,t13)
    print("Increasing Priority of ",t13,
          "to 10 (new priority smaller, should do nothing)")
    heap_increase_key(todo,1,10)
    print("Increasing Priority of ",t13,"to 30")
    heap_increase_key(todo,1,30)
    print("Epicperson seeks a task to complete!")
    topPriority = heap_extract_max(todo)
    print("Got:",topPriority)
    print("Inserting Task",t14)
    max_heap_insert(todo,t14)
    print("Inserting Task",t15)
    max_heap_insert(todo,t15)
    print("Epicperson seeks a task to complete!")
    topPriority = heap_extract_max(todo)
    print("Got:",topPriority)
    print("\nTEST #11: Day 2 final task extraction")
    print("\nEpicperson seeks a task to complete!")
    topPriority = heap_extract_max(todo)
    print("Expected Output:",t12,"\n\nGot:",topPriority)
    assert topPriority == t12,"heap_extract_max incorrect output"
    count = count+1
    print("\nTEST #12: Day 2 final heap correctness")
    print("\nExpected Heap:",correct,"\n\nGot:",todo)
    assert todo == correct, "Final result heap incorrect"
    count = count+1
except AssertionError as e:
    print("\nFAIL: ", e)
except Exception:
    print("\nFAIL: ", traceback.format_exc())



print(count,"out of 12 tests passed.")
