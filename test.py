from matplotlib import pyplot as plt
from scipy.integrate import odeint
import numpy as np

g = 9.8
L = 2
c = 0.25

def u(u, t):
    return (u[1],-c*u[1]-(g/L)*np.sin(u[0]))

y0 = [0.01,0]
ts = np.linspace(1,40,1000)
us = odeint(u, y0, ts)
ys = us[:,0]
plt.plot(ts,ys,'-')
#plt.plot(ts,ys,'r*')
plt.xlabel('t values')
plt.ylabel('u values')
plt.title('Solution')

plt.show()