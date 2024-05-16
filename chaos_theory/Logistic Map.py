import matplotlib.pyplot as plt
from matplotlib.widgets import Slider
import numpy as np

iterations=100
rVal=1

fig, ax=plt.subplots()
plt.subplots_adjust(bottom=0.32)

axr = plt.axes([0.15, 0.15, 0.65, 0.03])
axi = plt.axes([0.15, 0.1, 0.65, 0.03])
rSlide=Slider(axr, "r", 0, 4, 0.5)
iSlide=Slider(axi, "Iterations",50,500,100,valstep=1)

xys=np.empty((iterations+1,2))
xys[0]=(0,0.5)

def logistic(xy,r):
    x,y=xy
    xDot=x+1
    yDot=r*y*(1-y)
    return (xDot, yDot)

def updateVal(val):
    rVal=rSlide.val
    iterations=iSlide.val
    
    xys=np.empty((iterations+1,2))
    xys[0]=(0,0.5)
    for i in range(iterations):
        xys[i+1]=logistic(xys[i],rVal)
    ax.cla()
    ax.plot(*xys.T,lw=0.6)
    ax.set_ylim(0,1)
    ax.set_xlabel("Iterations")
    ax.set_ylabel("Population %")
    ax.set_title("Logistic Map")

for i in range(iterations):
    xys[i+1]=logistic(xys[i],rVal)

rSlide.on_changed(updateVal)
iSlide.on_changed(updateVal)

ax.plot(*xys.T,lw=0.6)
ax.set_ylim(0,1)
ax.set_xlabel("Iterations")
ax.set_ylabel("Population %")
ax.set_title("Logistic Map")
plt.show()