import numpy as np

# The paper provided describes a neural network architechture focused around efficient parallel sorting.

# This file inludes randomly generated sample data for our model to sort and a validation function to compare the sorted results.


# n = number of elements in the list
# low & high = range of random integers
def create_data(n, low=1, high=101):
    data = np.random.rand(n)
    data = data * high
    data = data + low
    return data


# simple linear confirmation for validating the sorted data
# ascending = True for ascending order, False for descending order
def validate_data(data, ascending=True):
    for i in range(len(data) - 1):
        if ascending:
            if data[i] > data[i + 1]:
                return False
        else:
            if data[i] < data[i + 1]:
                return False
    return True
