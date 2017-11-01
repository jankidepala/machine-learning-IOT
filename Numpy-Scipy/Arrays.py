import numpy as np

a = np.array([[1, 2, 3, 4], [1, 5,5,5], [8,9]])   # Create a rank 1 array
print(type(a))            # Prints "<class 'numpy.ndarray'>"
print("SHAPE ",a.shape)            # Prints "(3,)"

b = np.array([[1,2,3],[4,5,6], [7, 4, 5]])    # Create a rank 2 array
print(b.shape)                     # Prints "(2, 3)"
print(b[0, 0], b[0, 1], b[1, 0])   # Prints "1 2 4"

#Indexing
c = b[:3]
d = b[1:2]
print("INDEXING :", d)
