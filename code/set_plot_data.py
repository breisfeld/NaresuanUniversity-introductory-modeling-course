"""
create some variables that can be used in various types of plots
"""

import numpy as np
import matplotlib.cm as cm
import matplotlib.mlab as mlab

#------------------------------------------------------------------------------
# variables for line plots
#------------------------------------------------------------------------------
def scatter(base, npts, magnitude=3.0):
    return base*(1 + magnitude*(0.5-np.random.rand(npts)))

xmin, xmax= 0., 5.
full_pts = 100
range_full_pts = range(full_pts)
np.random.shuffle(range_full_pts)
sparse_frac = 0.1
sparse_pts = int(np.ceil(sparse_frac*full_pts))
sparse_ind = sorted(range_full_pts[:sparse_pts])

x_simp = np.linspace(xmin, xmax, full_pts)
y_simp = (x_simp-2.)**3
x_simp_sparse = x_simp[sparse_ind]
y_simp_sparse = scatter(y_simp[sparse_ind], len(x_simp_sparse))
y_simp_std = scatter(0.1*np.max(y_simp_sparse), len(x_simp_sparse))

#------------------------------------------------------------------------------
# variables for multi-subplot plots
#------------------------------------------------------------------------------
y_mult_1 = np.sin(np.pi*x_simp)
y_mult_2 = np.cos(np.pi*x_simp/2) - np.sin(np.pi*x_simp)

#------------------------------------------------------------------------------
# variables for bar charts
#------------------------------------------------------------------------------
men_means = (20, 35, 30, 35, 27)
men_std = (2, 3, 4, 1, 2)
women_means = (25, 32, 34, 20, 25)
women_std = (3, 5, 2, 3, 3)

#------------------------------------------------------------------------------
# variables for histograms
#------------------------------------------------------------------------------
mu, sigma = 100, 15
x_hist = mu + sigma*np.random.randn(10000)

#------------------------------------------------------------------------------
# variables for contour plots
#------------------------------------------------------------------------------
delta = 0.025
x_cont = np.arange(-3.0, 3.0, delta)
y_cont = np.arange(-2.0, 2.0, delta)
x_mesh, y_mesh = np.meshgrid(x_cont, y_cont)
z1 = 100*mlab.bivariate_normal(x_mesh, y_mesh, 1.0, 1.0, 0.0, 0.0)
z2 = 200*mlab.bivariate_normal(x_mesh, y_mesh, 1.5, 0.5, 1, 1)
# difference of Gaussians
z_mesh = (z2 - z1)
