import traceback

#linear_probe: takes in a Hashtag object with key k and an integer i
#returns (k + i) mod 13
def linear_probe(hashtag,i):
    return (hashtag.key + i) % 13

#double_hash: takes in a Hashtag object with key k and an integer i
#returns (k + i*(1 + (k mod 12))) mod 13
def double_hash(hashtag,i):
    return (hashtag.key + i*(1 + (hashtag.key % 12))) % 13


#hash_insert: takes inputs:
#   table: the hash table, a list of 13 elements.
#       each element is either a Hashtag object, None, or the special object DELETED
#   hashtag: a Hashtag type object to insert into the hash table
#   hash_function: a function, either linear_probe or double_hash
#Inserts the Hashtag object at the proper place in the table, and returns the
#   index at which it was inserted.
def hash_insert(table,hashtag,hash_function):
    offset = 0
    while(offset != 13):
        slot = hash_function(hashtag, offset)
        curr = table[slot]
        if (curr == None or curr == DELETED):
            table[slot] = hashtag
            return slot
        offset += 1
    raise "hash table overflow"

#hash_delete: takes inputs:
#   table: the hash table, a list of 13 elements.
#       each element is either a Hashtag object, None, or the special object DELETED
#   hashtag: a Hashtag type object to search for in the hash table
#   hash_function: a function, either linear_probe or double_hash
#Deletes the requested Hashtag object in the table, replacing it with DELETED.
#   returns either the index at which the object was found, or None it wasn't.
def hash_delete(table,hashtag,hash_function):
    index = hash_search(table,hashtag,hash_function)
    if (index != None):
        table[index] = DELETED
        return index
    return None

#hash_search: takes inputs:
#   table: the hash table, a list of 13 elements.
#       each element is either a Hashtag object, None, or the special object DELETED
#   hashtag: a Hashtag type object to search for in the hash table
#   hash_function: a function, either linear_probe or double_hash
#Searches for the requested Hashtag object in the table.
#   returns either the index at which the object was found, or None it wasn't.
def hash_search(table,hashtag,hash_function):
    offset = 0
    slot = hash_function(hashtag, offset)
    curr = table[slot]
    if (curr == hashtag):
        return slot
    offset = 1
    while(offset != 13 and curr != None):
        slot = hash_function(hashtag, offset)
        curr = table[slot]
        if (curr == hashtag):
            return slot
        offset += 1
    return None


#DO NOT EDIT BELOW THIS LINE

class Hashtag:
    def __init__(self,hashtag):
        self.hashtag = hashtag
        if hashtag == "DELETED":
            self.key = ""
        else:
            self.key = -16
            for i in hashtag:
                self.key += (ord(i)-97) % 26
    def __repr__(self):
        return str(self.key)+":"+str(self.hashtag)
    def __eq__(self,other):
        return type(self) == type(other) and \
               self.hashtag == other.hashtag

#Special DELETED object.  Treated as None for purposes of insertion,
#but as an occupied spot for purposes of searching/deletion
DELETED = Hashtag("DELETED")
DELETED.key = ""

#Test cases

hashtag_list1 = ["#holistic","#synergies","#ltd"]
hashtag_list2 = ["#help","#i","#uploaded","#myself","#to","#the",
             "#cloud","#and","#cant","#get","#out"]
hashtag_list3 = ["#time__","#travel__________","#cannot___________",
                 "#save__","#you___","#feel____________","#the__","#wrath",
                 "#of___","#ted","#from___________","#accounting___"]

correct_1 = [None,None,None,None,None,None,None,"#ltd","#synergies",
             "#holistic",None,None,None]
del_1 = Hashtag("#synergies")
correct_1d = [None,None,None,None,None,None,None,"#ltd","DELETED",
             "#holistic",None,None,None]
ins_1 = Hashtag("#synergies")
correct_1i = [None,None,None,None,None,None,None,"#ltd","#synergies",
             "#holistic",None,None,None]
ser_1 = Hashtag("#synergies")
correct_1s = 8

correct_2 = [None,"#out",None,"#and","#the","#uploaded","#get","#to",
             "#i","#myself","#cant","#help","#cloud"]
del_2 = Hashtag("#help")
correct_2d = [None,"#out",None,"#and","#the","#uploaded","#get","#to",
             "#i","#myself","#cant","DELETED","#cloud"]
ins_2 = Hashtag("#chaos")
correct_2i = [None,"#out","#chaos","#and","#the","#uploaded","#get","#to",
             "#i","#myself","#cant","DELETED","#cloud"]
ser_2 = Hashtag("#cloud")
correct_2s = 12

correct_3 = ["#out","#cloud","#get","#and","#the","#uploaded","#cant","#to",
             "#i","#myself",None,"#help",None]
del_3 = Hashtag("#help")
correct_3d = ["#out","#cloud","#get","#and","#the","#uploaded","#cant","#to",
             "#i","#myself",None,"DELETED",None]
ins_3 = Hashtag("#chaos")
correct_3i = ["#out","#cloud","#get","#and","#the","#uploaded","#cant","#to",
             "#i","#myself",None,"DELETED","#chaos"]
ser_3 = Hashtag("#cloud")
correct_3s = 1

correct_4 = ["#time__","#travel__________","#cannot___________",
                 "#save__","#you___","#feel____________","#the__","#wrath",
                 "#of___","#ted","#from___________","#accounting___",None]
del_4 = Hashtag("#save__")
correct_4d = ["#time__","#travel__________","#cannot___________",
                 "DELETED","#you___","#feel____________","#the__","#wrath",
                 "#of___","#ted","#from___________","#accounting___",None]
ins_4 = Hashtag("#fools")
correct_4i = ["#time__","#travel__________","#cannot___________",
                 "DELETED","#you___","#feel____________","#the__","#wrath",
                 "#of___","#ted","#from___________","#accounting___","#fools"]
ser_4 = Hashtag("#save__")
correct_4s = None

correct_5 = ["#time__","#travel__________","#cannot___________",
             "#feel____________","#from___________",None,"#wrath","#the__",
             "#save__","#of___","#accounting___","#you___","#ted"]
del_5 = Hashtag("#save__")
correct_5d = ["#time__","#travel__________","#cannot___________",
             "#feel____________","#from___________",None,"#wrath","#the__",
             "DELETED","#of___","#accounting___","#you___","#ted"]
ins_5 = Hashtag("#fools")
correct_5i = ["#time__","#travel__________","#cannot___________",
             "#feel____________","#from___________","#fools","#wrath","#the__",
             "DELETED","#of___","#accounting___","#you___","#ted"]
ser_5 = Hashtag("#save__")
correct_5s = None

testlists = [hashtag_list1,hashtag_list2,hashtag_list2,hashtag_list3,hashtag_list3]
correct = [correct_1,correct_2,correct_3,correct_4,correct_5]
correct_d = [correct_1d,correct_2d,correct_3d,correct_4d,correct_5d]
del_list = [del_1,del_2,del_3,del_4,del_5]
correct_i = [correct_1i,correct_2i,correct_3i,correct_4i,correct_5i]
ins_list = [ins_1,ins_2,ins_3,ins_4,ins_5]
correct_s = [correct_1s,correct_2s,correct_3s,correct_4s,correct_5s]
search_list = [ser_1,ser_2,ser_3,ser_4,ser_5]
probe_type = [linear_probe,linear_probe,double_hash,linear_probe,double_hash]
probe_string = ["Linear Probe","Linear Probe","Double Hash","Linear Probe","Double Hash"]
for i in range(len(testlists)):
    testlists[i] = list(map(lambda x: Hashtag(x),testlists[i]))
    correct[i] = list(map(lambda x: None if x == None else Hashtag(x),correct[i]))
    correct_d[i] = list(map(lambda x: None if x == None else Hashtag(x),correct_d[i]))
    correct_i[i] = list(map(lambda x: None if x == None else Hashtag(x),correct_i[i]))


probe_tests = [Hashtag("#never"),Hashtag("#gonna"),Hashtag("#give"),
               Hashtag("#you"),Hashtag("#up")]
probe_tests2 = [Hashtag("#never"),Hashtag("#gonna"),Hashtag("#let"),
               Hashtag("#you"),Hashtag("#down")]
linear_probe_vals = [7,8,2,9,0]
double_hash_vals = [7,5,4,0,7]

count = 0

try:
    print("TEST #",1,":","Checking Probing Functions")
    for i in range(len(probe_tests)):
        print("Testing linear_probe("+str(probe_tests[i])+","+str(i)+")")
        out = linear_probe(probe_tests[i],i)
        assert out == linear_probe_vals[i],"Linear Probing Function Incorrect"+\
               "- \nExpected: " + str(linear_probe_vals[i])+"\nGot:      " + str(out)
    for i in range(len(probe_tests)):
        print("Testing double_hash("+str(probe_tests2[i])+","+str(i)+")")
        out = double_hash(probe_tests2[i],i)
        assert out == double_hash_vals[i],"Double Hashing Function Incorrect"+\
               "- \nExpected: " + str(double_hash_vals[i])+"\nGot:      " + str(out)
    count = count + 1

    for i in range(len(testlists)):
        print("\n---------------------------------------\n")
        print("TEST #",i+2,":",probe_string[i])
        testlist = list(testlists[i])
        table = [None]*13
        for hashtag in testlist:
            print("Inserting:",hashtag)
            hash_insert(table,hashtag,probe_type[i])
        assert table == correct[i], "Table incorrect- \nExpected: " + \
               str(correct[i]) + "\nGot:      " + str(table)

        print("Deleting",del_list[i])
        hash_delete(table,del_list[i],probe_type[i])
        assert table == correct_d[i], "Table incorrect- \nExpected: " + \
               str(correct_d[i]) + "\nGot:      " + str(table)

        print("Inserting",ins_list[i])
        hash_insert(table,ins_list[i],probe_type[i])
        assert table == correct_i[i], "Table incorrect- \nExpected: " + \
               str(correct_i[i]) + "\nGot:      " + str(table)

        print("Searching",search_list[i])
        index = hash_search(table,search_list[i],probe_type[i])
        assert index == correct_s[i], "Search index incorrect- \nTable is: "+ \
               str(table) + "\nExpected: " + str(correct_s[i]) + "\nGot:      " + \
               str(index)
        print("Final Table",table)
        count += 1
except AssertionError as e:
    print("\nFAIL: ",e)
except Exception:
    print("\nFAIL: ",traceback.format_exc())

print("\n---------------------------------------\n")
print(count,"out of",6,"tests passed.")
