#Numpy Functions

L=list(range(10))
L2=[str(c) for c in L]
l3=[1,'One',1.00,True]
l3
print(list(type(x) for x in l3))
for x in l3:
    print(type(x))

import array

a=array.array('i',L)

import numpy as np

a=np.array([3,2,5,1])

np.array([range(i,i+4) for i in range(5)])

# Create a length-10 integer array filled with zeros
np.zeros(10,dtype=int)

# Create a 3x5 floating-point array filled with ones
np.ones([3,4],dtype=float)

# Create a 4x5 array filled with 200
np.full([4,5],200)

# Create an array filled with a linear sequence
# Starting at 10, ending at 20, stepping by 3
# (this is similar to the built-in range() function)
np.arange(10,20,3)


# Create an array of five values evenly spaced between 0 and 1
np.linspace(0,1,5)

# Create a 3x3 array of uniformly distributed
# random values between 0 and 1
np.random.random((3,3))

# Create a 3x3 array of random integers in the interval [0, 10]
np.random.randint(3,10,(3,3))


# Create a 3x3 array of normally distributed random values
# with mean 0 and standard deviation 1
np.random.normal(0,1,(3,3))

# Create a 3x3 identity matrix
np.eye(3)

# Create an uninitialized array of three integers
# The values will be whatever happens to already exist at that memory location

np.empty(5)


np.random.seed(0)  # seed for reproducibility

x1 = np.random.randint(10, size=6)  # One-dimensional array
x2 = np.random.randint(10, size=(3, 4))  # Two-dimensional array
x3 = np.random.randint(10, size=(3, 4, 5))  # Three-dimensional array
print(x1)
print(x2)
print(x3)

x1[1:5:2]
x2[1:,::3]
x2[2:,::2]
