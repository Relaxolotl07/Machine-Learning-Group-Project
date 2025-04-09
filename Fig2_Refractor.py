# Refractor of Fig2.m into python
# April 9 2024
# Alexander Evans

#
# Started Refractor
# To run call in main.py
#
# Begun K-WTA simulation 
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

    #initialize ki and aa
    ki = []
    # aa is for plotting
    aa = []

    # I think there are numpy functions for this if someone wants to refractor
    # creates nested array
    for l in range(n):
        aa.append([])

    # plotting preparation
    for x in range(j):
        ki.append(x)
        for l in range(n):
            aa[l].append(sa[l])
    # convert aa into numpy array for slicing operation later
    aa = np.array(aa)

    # Subplot 1 trajectories
    # Define the subplots
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10,8))
    # define plot styles
    plot_styles = ['ko-', 'rh-', 'b<-', 'm^-', 'gv-', 'kp-', 'cd-', 'rx-', 'b*-']
    # set the label for the subplots
    labels = [f'a_{i+1}' for i in range(n)] # f is for shorthand formatting in python
    # Set each subplot with the plotstyle and label according to fig2
    for i in range(n):
        ax1.plot(ki, aa[i, :], plot_styles[i], label=labels[i])

    # x and y limit for ax1
    ax1.set_xlim(1,j)
    ax1.set_ylim(-5, 5)
    # x and y labels
    ax1.set_xlabel('Number of iteration l')
    ax1.set_ylabel('Trajectories a_1 to a_9')
    # activate the legend
    ax1.legend()
    # set to show the grid
    ax1.grid(True)
   
    # K-WTA Simulation

    # initial x
    x = [0.5]
    alfa = [0.6]

    # s arrays initialized with zero
    s1 = np.zeros((j,n))
    s2 = np.zeros((j,n))
    s3 = np.zeros((j,n))
    s4 = np.zeros((j,n))
    s5 = np.zeros((j,n))
    s6 = np.zeros((j,n))
    s7 = np.zeros((j,n))
    s8 = np.zeros((j,n))
    s9 = np.zeros((j,n))
    
    # loop over the range to run the simulation
    for k in range(n):
        # begin time assessment
        start_time = time.time()

        # initialize d array
        d=np.zeros(j)

        # Actual K-WTA Simulation
        for (i) in range(j):
            
            # set s values
            # binary decision (Pass - Fail)
            s = []
            # We set the values of Pass or Fail 
            # based on normalized list <a> 
            # compared to given/calculated x
            for l in range(n):
                # Pass
                if (a(l) - x(i)) > 0:
                    s(l) = 1
                # Fail
                else:
                    s(l) = 0
            
            # Case
            # Dot product
            # Could use a refractor into switch for efficiency
            # Places the dot product of <a> and <s> into d array 
            # k is the  of k-WTA
            # 
            if k==0:
                d[i] = np.dot(a,s)
                s1[i, :] = s
            elif k==1:
                d[i] = np.dot(a, s - s1[i,:])
                s2[i, :] = s
            elif k==2:
                d[i] = np.dot(a, s - s2[i,:])
                s3[i, :] = s
            elif k==3:
                d[i] = np.dot(a, s - s3[i,:])
                s4[i, :] = s
            elif k==4:
                d[i] = np.dot(a, s - s4[i,:])
                s5[i, :] = s
            elif k==5:
                d[i] = np.dot(a, s - s5[i,:])
                s6[i, :] = s
            elif k==6:
                d[i] = np.dot(a, s - s6[i,:])
                s7[i, :] = s
            elif k==7:
                d[i] = np.dot(a, s - s7[i,:])
                s8[i, :] = s
            elif k==8:
                d[i] = np.dot(a, s - s8[i,:])
                s9[i, :] = s

            # Add all s values and put it into ss
            ss = np.sum(s)
            e = ss - (k+1)
    return # fig2_refractor end