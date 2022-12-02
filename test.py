"""
Name: Ethan Matthews
Project: Inverted Pendulum ODE simulation
Description: Project for Differentials Equations class
in which we need to model an inverted pendulum
"""

from matplotlib import pyplot as plt
from scipy.integrate import odeint
import numpy as np

# Constants given by the project
g = 9.8
L = 2
c = 0.25

# Function that holds the basic ODE
def u(u, t):
    return (u[1],-c*u[1]-(g/L)*np.sin(u[0]))

# Setting up the graphing for the ODE
y0 = [0.01,0]
ts = np.linspace(1,40,1000)
us = odeint(u, y0, ts)
ys = us[:,0]
plt.plot(ts,ys,'-')

plt.xlabel('t values')
plt.ylabel('u values')
plt.title('Solution')

plt.show()