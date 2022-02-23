# Exercises for Day 3
# Numpy and inheritance

## 1. Numpy exercises
import numpy as np

#### a. Create a null vector of size 10 but the fifth value which is 1
null_with_1_at_5th = np.zeros(10)
null_with_1_at_5th[4] = 1
print(null_with_1_at_5th)

#### b. Create a vector with values ranging from 10 to 49
from_10_to_49 = np.arange(10,49,1)
print(from_10_to_49)

#### c. Reverse a vector (first element becomes last) 
to_be_reversed = np.arange(10)
reversed_vector = np.reverse(to_be_reversed)
print(to_be_reversed)
print(reversed_vector)

#### d. Create a 3x3 matrix with values ranging from 0 to 8
crescent_matrix =  np.arange(8).reshape((3,3))
print(crescent_matrix)

#### e. Find indices of non-zero elements from [1,2,0,0,4,0]
my_list = [1,2,0,0,4,0]
non_zero_indices = [i for i, val in enumerate(my_list) if val!=0] # With lists
my_array = np.array(my_list)
non_zero_indices_np = np.nonzero(my_array) # With arrays
print(non_zero_indices)
print(non_zero_indices_np)
print(my_array[non_zero_indices_np])

#### f. Create a random vector of size 30 and find the mean value
random_vector = np.random.rand(30)
mean = np.mean(random_vector)
print(mean)

#### g. Create a 2d array with 1 on the border and 0 inside
N = 5 # Array sizes
array = np.ones((N,N)) # Create array of ones
array[1:-1, 1:-1] = 0 # Empty the values not on border
print(array)

#### h. Create a 8x8 matrix and fill it with a checkerboard pattern
checkerboard = np.array([[1 if i%2==j%2 else 0 for i in range(8)] for j in range(8)])
print(checkerboard)

#### i. Create a checkerboard 8x8 matrix using the tile function
tile = [[1,0],[0,1]]
checkerboard_from_tile = np.tile(tile, (4,4))
print(checkerboard_from_tile)

#### j. Given a 1D array, negate all elements which are between 3 and 8, in place
Z = np.arange(11)
Z[3:8] *= -1 # Negating elements between 3rd and 8th indices
print(Z)

Z = np.arange(11)
Z[(Z >= 3) & (Z < 8)] *= -1 # Negating elements based on their values (between 3 and 8)
print(Z)

#### k. Create a random vector of size 10 and sort it
Z = np.random.random(10)
Z = np.sort(Z)
print(Z)

#### l. Consider two random array A anb B, check if they are equal
A = np.random.randint(0,2,5)
B = np.random.randint(0,2,5)
equal = (A==B).all()
print(equal)

#### m. How to convert an integer (32 bits) array into a float (32 bits) in place?
Z = np.arange(10, dtype=np.int32)
print(Z.dtype)
Z = Z.view('float32')
print(Z.dtype)

#### n. How to get the diagonal of a dot product?
A = np.arange(9).reshape(3,3)
B = A + 1
C = np.dot(A,B)
D = np.diag(C)
print(C) # Show the matrix to check we are indeed getting the diagonal
print(D)