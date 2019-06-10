# array such that arr[i] = i. 
def arrayFind(A, len):
	for  i in range(0, len):
		if(A[i] != -1 and A[i] != i):
			x = A[i]
	print('--------')
			

def fix( A, len): 
	
	for i in range(0, len): 
		
		if (A[i] != -1 and A[i] != i): 
			x = A[i]; 
			while (A[x] != -1 and A[x] != x): 
				#store the value from 
				# desired place 
				y = A[x] 

				# place the x to its correct 
				# position 
				A[x] = x 

				# now y will become x, now 
				# search the place for x 
				x = y 
			
			# place the x to its correct 
			# position 
			A[x] = x; 

			# check if while loop hasn't 
			# set the correct value at A[i] 
			if (A[i] != i) : 
				
				# if not then put -1 at 
				# the vacated place 
				A[i] = 0; 

# Driver function. 
A = [ 0, 1, 2, 1, 9, 5, 2, -1, 4, -1 ] 
print(arrayFind(A, len(A)))
fix(A, len(A)) 

for i in range(0, len(A)): 
	print (A[i],end = ' ') 

	