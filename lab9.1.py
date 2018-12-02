from numpy import*
from math import*
import matplotlib.pyplot as plt

x = linspace(0,5,50)
y =5*cos(10*x)*sin(3*x)/(x**(1/2))

plt.plot(x,y,'g--', label = '')
plt.savefig('y.png', dpi = 200)
plt.axis([0,5,-1,1])
plt.xlabel('x')
ply.ylabel('y')

plt.title('My first normal plot')
plt.legend()

plt.show()
