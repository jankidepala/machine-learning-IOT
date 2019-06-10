#Insertion sort is a simple sorting algorithm that works the way we sort playing cards in our hands.
#Uses: number of elements is small. input array is almost sorted, only few elements are misplaced in complete big array.
#O(n2) algorithm

def insertionSort(a):
    for i in range(1, len(a)):
        print("i", i)
        key = a[i]
        for j in range(i-1, -1, -1):
            if a[j] > key:
                a[j+1] = a[j]
            else:
                a[j+1] - key
                break

def insertionSort2(b):
    for i in range(1, len(b)):
        key = b[i]
        j = i-1
        print("Data key", j, key,"<", b[i-1])
        while j >= 0 and key < b[j]:
                b[j+1] = b[j]
                j -= 1
                print("Data", j, key, b[i])
        b[j+1] = key


            
b =[3, 4, 1, 6, 0]
insertionSort(b)

# Driver code to test above
arr = [4, 8, 11, 13, 5, 6]
insertionSort2(arr)
print ("Sorted array is:")
for i in range(len(arr)):
    print ("%d" %arr[i])
