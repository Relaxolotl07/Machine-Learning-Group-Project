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




def fig2_refractor () :
    import numpy as np
    import matplotlib.pyplot as plt
    import time

    # Paramter Initialization
    # Trajectories
    n=9
    # Iterations
    j=10

    # dmin: tracks smallest value of k in d array
    # dmax: largest k values in d array
    # tmax: max time to execute the inner simulation loop for k
    dmin, dmax, tmax = 0, 0, 0

    # Random Data Generation
    # Generate array of random numbers
    a = np.random.rand(n)
    # scale to [-1, 1]
    sa = (a - 0.5) * 2
    
    return