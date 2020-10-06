
import matplotlib.pyplot as plt
import numpy as np

x = np.arange(0,2*np.pi,0.1)   # start,stop,step
y = np.sin(x)
z = np.cos(x)
t = np.tan(x)
plt.plot(x,y,x,z)
plt.show()
# this is a good code. You can also add the main function!

# to improve the scalability and plot tangent function
plt.plot(x,t)
plt.ylim(-3,3)
plt.show()
