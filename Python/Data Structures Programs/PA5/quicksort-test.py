def partition(A,p,r):
    x = A[r]
    # print("                                    pivot is " + str(x))
    i = p - 1
    for j in range(p, r):
        if A[j] <= x:
            i = i + 1
            z = A[i]
            A[i] = A[j]
            A[j] = z
    z = A[i + 1]
    A[i + 1] = A[r]
    A[r] = z
    return i + 1

#Takes in list of Emails A, and indices p and r
#Sorts the sublist A[p...r], in order of the length of each Email's
#sender, from longest name to shortest, using Quicksort
#Returns nothing
def quicksort(A,p,r):
    if p < r:
        # print("before partition" + " p is " + str(p) + " r is " + str(r))
        # display(A)
        q = partition(A, p, r)
        # print("after partition " + "p is " + str(p) + " r is " + str(r) + " q is " + str(q))
        # display(A)
        # print("")
        quicksort(A, p, q-1)
        quicksort(A, q+1, r)

def display(A):
    sortresult = ""
    for i in range(0, len(A)):
        sortresult += str(A[i]) + ", "
    print(sortresult)

B = [10,9,8,7,6,5,4,3,2,1]
C = [1,1,1,1,1,6,2,10,11,12]

quicksort(B, 0, len(B)-1)

def TwoSumToX(A, x):
			quicksort(A,0, len(A)-1)
			p = 0
			r = len(A) - 1
			cont = True
			result = False
			while cont and p < r:
				if A[p] + A[r] == x:
					cont = False
					result = True
				elif A[p] + A[r] < x:
					p += 1
				elif A[p] + A[r] > x:
					r -= 1
			return result

print(TwoSumToX(C, 2))
print(TwoSumToX(C, 7))
print(TwoSumToX(C, 3))
print(TwoSumToX(C, 11))
print(TwoSumToX(C, 12))
print(TwoSumToX(C, 13))
print(TwoSumToX(C, 8))
print(TwoSumToX(C, 16))
print(TwoSumToX(C, 17))
print(TwoSumToX(C, 13))
print(TwoSumToX(C, 14))
print(TwoSumToX(C, 21))
print(TwoSumToX(C, 22))
print(TwoSumToX(C, 23))
print(TwoSumToX(C, 16))
print(TwoSumToX(C, 16))
