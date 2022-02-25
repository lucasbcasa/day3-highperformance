# Advanced Exercises: High-performance computing

#### a. Given a list of XYZ-coordinates, p,

p = [[1.0, 2.0, 10],
     [3.0, 4.0, 20],
     [5.0, 6.0, 30],
     [7.0, 8.0, 40]]
# Normalise each coordinate by dividing with its Z (3rd) element. For example, the first row becomes:
# `[1/10, 2/10, 10/10]`
# Hint: extract the last column into a variable z, and then change its dimensions so that p / z works.
import numpy as np
p = np.array(p) # Transform list of lists into ndarray
z = p[:,-1] # Extract last column
z = z[:, np.newaxis] # Create new dimension so that broadcast can happen
p = p/z # Divide matrix through broadcast (per element division)
print(p)

#### b. Create a 3x3 ndarray. Use fancy indexing to slice out the diagonal elements.
array = np.random.rand(3,3) # Create array
diagonal = array[range(3),range(3)] # access diagonal elements
print(array)
print(diagonal)

#### c. Generate a 10 x 3 array of random numbers (all between 0 and 1). From each row, pick the number closest to 0.75. Make use of np.abs and np.argmax to find the column j which contains the closest element in each row.
array = np.random.rand(10,3)
j = np.argmin(np.abs(array-0.75), axis=1)
closest_values = array[range(10), j]
print("Column indices: ", j)
print("Closest values: ", closest_values)

#### d. Predict and verify the shape of the following slicing operation.

x = np.empty((10, 8, 6))

idx0 = np.zeros((3, 8)).astype(int)
idx1 = np.zeros((3, 1)).astype(int)
idx2 = np.zeros((1, 1)).astype(int)

# x[idx0, idx1, idx2]

# Predictions: x has shape 10 x 8 x 6
# x[idx0,:,:] should have shape (3 x 8) x (8 x 6), since we set the first entry of x to 3 x 8 values, and for each value we get a 8 x 6 matrix back
print("Check prediction (3 x 8 x 8 x 6): ", x[idx0,:,:].shape)
# x[idx0,idx1,:] should have shape Broadcast((3 x 8), (3 x 1)) x (6), since we set the first entry of x to 3 x 8 values, the second to 3 x 1 values simultaneously, and for each value we get an array of length (6) back. The broadcast results in Broadcast((3 x 8), (3 x 1)) = 3 x 8, so the final shape is 3 x 8 x 6.
print("Check prediction (3 x 8 x 6): ", x[idx0,idx1,:].shape)
# x[idx0,idx1,idx2] should have shape Broadcast((3 x 8), (3 x 1), (1 x 1)) x (), since we set the first entry of x to 3 x 8 values, the second to 3 x 1 values and the third to 1 x 1 simultaneously, and for each value we get a number back. The broadcast results in Broadcast((3 x 8), (3 x 1), (1 x 1)) = 3 x 8, so the final shape is 3 x 8.
print("Check prediction (3 x 8): ", x[idx0,idx1,idx2].shape)



#### e. *Very Advanced* Construct an array:
'''
x = np.arange(12, dtype=np.int32).reshape((3, 4))
'''

#so that x is

'''
array([[ 0,  1,  2,  3],
       [ 4,  5,  6,  7],
       [ 8,  9, 10, 11]])
'''

#Now, provide to `np.lib.stride_tricks.as_strided` the strides necessary to view a sliding 2x2 window over this array. The output should be

'''
array([[[[ 0,  1],
         [ 4,  5]],

        [[ 1,  2],
         [ 5,  6]],

        [[ 2,  3],
         [ 6,  7]]],


       [[[ 4,  5],
         [ 8,  9]],

        [[ 5,  6],
         [ 9, 10]],

        [[ 6,  7],
         [10, 11]]]], dtype=int32)
'''

#The code is of the form

'''
z = as_strided(x, shape=(2, 3, 2, 2),
                  strides=(..., ..., ..., ...))
'''

#This sort of stride manipulation is handy for implementing techniques such as region based statistics, convolutions, etc.

# Solution:

x = np.arange(12, dtype=np.int32).reshape((3, 4))

# The np.int32 datatype takes 4 bytes per entry
# So the strides of x, in row-major ordering, should be 
# 4 x (ncols, 1) = (4 x 4, 4) = (16, 4)
xstrides = x.strides
print(xstrides)

# For a (2 x 3 x 2 x 2) array with np.int32 datatype
# The strides, in row-major ordering, should be
# 4 x (n1 x n2 x n3, n2 x n3, n3, 1) = 4 x (12, 4, 2, 1) = (48, 16, 8, 4)
print(np.empty((2,3,2,2), dtype=np.int32).strides)

# In order to view a gliding 2x2 window we need to add multiples of the stride entries
#strides = [(n * xstrides[0], m * xstrides[1]) for (m,n), _ in np.ndenumerate(x)]

strides = (48, 4, 16, 4)

z = np.lib.stride_tricks.as_strided(x, shape=(2, 3, 2, 2), strides=strides)
