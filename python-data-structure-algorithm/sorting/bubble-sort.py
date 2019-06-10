#Worst and Average Case Time Complexity: O(n*n). Worst case occurs when array is reverse sorted.

#Swap 2 adjacent element till they r in right order

A = [99, 2, 14, 64, 25, 12, 22, 11]

for i in range(0, len(A)-1):
    
    for j in range(0, len(A)-1-i):
            while A[j+1] <  A[j]:
                A[j], A[j+1] = A[j+1] , A[j]
                print(len(A)-1-i)
             
# Driver code to test above
print ("B Sorted array")
for i in range(len(A)):
    print("%d" %A[i]), 
