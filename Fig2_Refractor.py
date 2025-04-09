# Refractor of Fig2.m into python
# April 9 2024
# Alexander Evans

#
# Started Refractor
# To run call in main.py
#
# Ploting Data list done
# Line 46 Refractor possible
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

    # this part in fig2 matlab is replaced by the parameter

    # Normalize sa into array a
    a = sa/10 + 0.5

    print (a)

    #initialize ki and aa
    ki = []
    # aa is for plotting
    aa = []

    # I think there are numpy functions for this if someone wants to refractor
    # creates nested array
    for l in range(n):
        aa.append([])

    # plotting 
    for x in range(j):
        ki.append(x)
        for l in range(n):
            aa[l].append(sa[l])

    
    return