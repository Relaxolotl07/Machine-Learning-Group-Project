# Refractor of Fig2.m into python
# April 9 2024
# Alexander Evans

#
# Started Refractor
# To run call in main.py
#
# Random data initialization done
#
#
#
import numpy as np
import matplotlib.pyplot as plt
import time

# takes an array and simulates a k-WTA networks with different ks
# if you want a random array test then input it in the parameter when calling
# sa is the array to test, is normalized within function
def fig2_refractor (sa) :


    # Paramter Initialization
    # Trajectories
    n=9
    # Iterations
    j=10

    # dmin: tracks smallest value of k in d array
    # dmax: largest k values in d array
    # tmax: max time to execute the inner simulation loop for k
    dmin, dmax, tmax = 0, 0, 0

    # 

    return