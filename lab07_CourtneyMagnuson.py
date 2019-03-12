# -*- coding: utf-8 -*-
"""
Created on Wed Feb 27 11:08:56 2019

@author: Courtney Magnuson
"""
import numpy as np
import matplotlib.pyplot as plt

def freq_and_modes(matrix, k_over_m):
    """
    Determine the frequencies and normalized 
    eigenvectors of a matrix
    
    Parameters
    ----------
    matrix : array
        n x n array
        
    k_over_m : float 
        value of pring constant (k) divided by
        mass of spring (m)
    
    Returns
    -------
    freq : array
        frequencies of matrix
        
    modes : array
        normalized eigenvectors (modes)
    
    """
    val, vect = np.linalg.eigh(matrix)
    
        #for different masses, use eig with no h
    
    freq = np.sqrt(val)
    return freq, vect

mat = np.array([[2, -1],
                [-1, 2]])

#mat = np.array([[2, -.1],
          #      [-1, .2]])      #matrix for m2 = 10m1

F, M = freq_and_modes(mat, 1)
print(F,M)

def comp_from_ics(x_init, modes):
    """
    Determine the coefficients a and b for the 
    normalized eigenvectors
    
    Parameters
    ----------
    x_init : array
        1 x n array. initial x positions
        
    modes : array 
        n x n array. normalized eigenvector 
    
    Returns
    -------
    floats
        coefficients a and b. a associated with
        eigenvector 1, b with 2.
    
    """
    a = x_init @ modes[:,0]
    b = x_init @ modes[:,1]
    return a,b



#x = np.array([1,-1]) #normal mode same mass
#x = np.array([1,1])  #normal mode same mass
#x = np.array([1,0])  #test position
x = np.array([0,1])  #test position
    #(1 0) does not oscillate "nicely"; there is no regular 
    #pattern for each mass's movement
    #initial x of (1 0) and (0 1) are the same but opposite
    
#x = np.array([0.88012902, 0.05386091]) #normal mode 10m and m
    # move the smaller mass to the right .880... units, the larger to the right .053... units
#x = np.array([-0.47473457,  0.99854845])
    #move the smaller mass to the left .4747.. units, the larger to the right .998... units
    
    #eigenvectors cause the masses to move harmonically
    
#(1 0) and (0 1) are different because the masses are different.  moving the larger mass will 
    #affect the smaller mass more than if vice versa

A, B = comp_from_ics(x,M)



def position_of_masses(f_and_m, coef, matrix, x_init, t):
    freq, modes = f_and_m(matrix, 1)
    a, b = coef(x_init, modes)
    x_pos = (a * np.cos(freq[0]*t)*modes[:,0] 
            + b * np.cos(freq[1]*t)*modes[:,1])
    return x_pos



t_init = 0
t_end = 50
N_times = 1000

time = np.linspace(t_init, t_end, num=N_times)

# So that we can multiply the array of times by two dimensinoal vectors
# later.

time = time.reshape(N_times, 1)

#print(position_of_masses(freq_and_modes, comp_from_ics, mat, x, time))




def plot_motion_of_masses(x, time, title='bad title'):
    """
    Function to make a plot of motion of masses as a function of time. The time
    should be on the vertical axis and the position on the horizontal axis.
    
    Parameters
    ----------
    x : array of position, N_times by 2 elements
        The array of positions, set up so that x[:, 0] is the position of mass
        1 relative to equilibrium and x[:, 1] is the position of mass 2.
    time : array of times
        Times at which the positions have been calculated.
    title : str
        A descriptive title for the plot to make grading easier.
    """
    # Nothing special about these, but they look nice
    x1_equilibrium_pos = 3
    x2_equilibrium_pos = 6

    x1 = x[:, 0] + x1_equilibrium_pos
    x2 = x[:, 1] + x2_equilibrium_pos

    plt.plot(x1, time, label='Mass 1')
    plt.plot(x2, time, label='Mass 2')
    plt.xlabel("Position")
    plt.ylabel("Time")
    plt.xlim(0, 9)
    plt.legend()
    plt.title(title)
    
x_pos = position_of_masses(freq_and_modes, comp_from_ics, mat, x, time)
plot_motion_of_masses(x_pos, time, title='Position of Springs Over Time')


