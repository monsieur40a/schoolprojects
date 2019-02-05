import traceback

#Takes as input two parameters:

# priceList is a list of integers that represents today's cost for a single order of
#  chicken nuggets for every quantity between 0 and the length of the priceList - 1.
#  So the element at index 0 should always be 0, the element at index 1 is the cost of
#  ordering a single chicken nugget, the element at index 2 is the cost of an order of
#  two chicken nuggets, and so on.

# numNuggets is an integer, representing the total number of chicken nuggets you need to
#  order today to send the intended message to your shadow organization

# Returns a list of integers, where each integer is the number of chicken nuggets in an order,
#  and the whole list represents the lowest cost set of orders which total to numNuggets.
def optimizeNuggets(priceList,numNuggets):
    revenue = [0]*(numNuggets + 1)
    split = [0]*(numNuggets + 1)
    for j in range(1, numNuggets + 1):
        lowest = float("inf")
        for i in range(1, j + 1):
            if (lowest > (priceList[i] + revenue[j - i])):
                lowest = priceList[i] + revenue[j - i]
                split[j] = i
        revenue[j] = lowest
    outputSplit = []
    while (numNuggets > 0):
        outputSplit.append(split[numNuggets])
        numNuggets -= split[numNuggets]
    return outputSplit


#  DO NOT EDIT BELOW THIS LINE
pL1 = [0, 4]
pL2 = [0, 1, 5, 8, 9, 12, 17, 19, 20]
pL3 = [0, 2, 3, 3, 6, 10, 11, 13, 14, 19]
pL4 = [0, 4, 7, 7, 7, 7, 7, 8, 9, 10, 11,
       15, 16, 19, 20, 21, 23, 24, 24, 24, 24,
       24, 24, 24, 24, 31, 32, 32, 34, 34, 34,
       35, 35, 36, 36, 39, 39, 39, 40, 41, 41,
       41, 44, 45, 45, 46, 47, 48, 49, 51, 53]

priceLists = [ list(pL1),list(pL2),list(pL2),list(pL3),list(pL3),list(pL4) ]
nuggetNums = [ 1, 3, 6, 4, 8, 35]
correct = [[1],[1, 1, 1],[1, 1, 1, 1, 1, 1],[1, 3],[2, 3, 3],[5, 6, 24]]

# Takes as input a list of prices for orders of any number of chicken nuggets between 0 and the length,
# along with a list of orders, which is an list of integers representing the number of chicken nuggets
# in each order, and computes the total cost of the list of orders.
def ComputeCost(priceList,splits):
    total = 0
    for ele in splits:
        total += priceList[ele]
    return total

#Run test cases
count = 0

try:
    for i in range(len(priceLists)):
        ("\n---------------------------------------\n")
        print("TEST #",i+1)
        print("Running optimizeNuggets("+str(priceLists[i])+", "+str(nuggetNums[i])+")")
        outSplit = optimizeNuggets(priceLists[i],nuggetNums[i])
        corrSplit = correct[i]
        outCost = ComputeCost(priceLists[i],outSplit)
        corrCost = ComputeCost(priceLists[i],corrSplit)
        print("Optimal Split:",corrSplit," Cost $"+str(corrCost))
        print("Output Split:",outSplit," Cost $"+str(outCost))
        assert sum(outSplit) == nuggetNums[i], "Wrong number of total nuggets ordered!"
        assert corrCost == outCost, "Nuggets order not cheapest possible!"
        print("Test Passed!\n")
        count += 1
except AssertionError as e:
    print("\nFAIL: ",e)

except Exception:
    print("\nFAIL: ",traceback.format_exc())


print(count,"out of",len(priceLists),"tests passed.")
