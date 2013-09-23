"""
my_module.py

This module contains various functions useful in the analysis of experimental data

Author: Brad Reisfeld
Last update: 20130908

Relevant equations were taken from the following references (these are not real):

Smith, J.A.  _Methods in Data Analysis_, 3rd edition, Springer, 1986, pp 45-47.
Jones et al. "Advanced comnputational techniques for discrete data", J. Appl. Comp., 12(3), 2011.

"""

import matplotlib.pyplot as plt
import numpy as np
import scipy as sp
import scipy.integrate as spi

def add_vals(x, y):
    """Sum of two values or two sets of values.
    
    x: a scalar or numpy array conytaining the first value(s)
    y: a scalar or numpy array conytaining the second value(s)
    
    If x and y are numpy arrays, they must have the same shape or be broadcast-able.
    
    """
    
    z = x + y
    return z
  
  
def plot_sin(m=1):
    """Scatter plot of the sin function.""" 
   
    m: a scalar number used to establish the length of the plotting interval,
       interval = [0, 2*pi*m]
    
    """
    
    x = np.linspace(0, 2*m*np.pi, 100)
    y = np.sin(x)
    plt.plot(x, y)
    plt.show()
 
 
def integrate_values(x, y):
    """Numerical integration of data using the trapezoidal method.
    
    x: list or numpy array of independent variable values
    y: list or numpy array of dependent variable values
    
    """
    
    z = spi.trapz(y, x)
    return z
