import matplotlib.pyplot as plt
import numpy as np
x=np.arange(0,2*np.pi,0.2)#可用于多种类型
y=np.sin(x)
y1=np.cos(x)
plt.plot(x,y,ls='-',lw=4,c='b')
plt.plot(x,y1,ls='-.',lw=4,c='r')
#x = range(0,100,1)
plt.show()
