#Time Complexity: O(n2) as there are two nested loops.


def selectionSort(a):
    for i in range(0, len(a)):
        print("bble ", i, a)

t= [9, 0, 6, 3]
selectionSort(t)

A = [64, 25, 12, 22, 11]

# Traverse through all array elements
for i in range(len(A)):
     
    # Find the minimum element in remaining 
    # unsorted array
    minIndex = i
    for j in range(i+1, len(A)):
        if A[minIndex] > A[j]:
            minIndex = j
             
    # Swap the found minimum element with 
    # the first element        
    A[i], A[minIndex] = A[minIndex], A[i]
 
# Driver code to test above
print ("Sorted array")
for i in range(len(A)):
    print("%d" %A[i]), 
