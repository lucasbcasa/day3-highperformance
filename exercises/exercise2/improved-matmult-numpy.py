# Program to multiply two matrices using nested loops
import numpy as np
from numpy.random import randint

N = 250

# NxN matrix
X = randint(0,high=100,size=(N,N))

# Nx(N+1) matrix
Y = randint(0,high=100,size=(N,N+1))

# result is Nx(N+1)
result = np.zeros((N,N+1),dtype=int)

# iterate through rows of X
# for i in range(len(X)):
#     # iterate through columns of Y
#     for j in range(len(Y[0])):
#         # iterate through rows of Y
#         for k in range(len(Y)):
#             result[i,j] += X[i,k] * Y[k,j] # Improved performance by accessing the arrays properly

# The performance can be improved without using nested loops:
result = X@Y

for r in result:
    print(r)
