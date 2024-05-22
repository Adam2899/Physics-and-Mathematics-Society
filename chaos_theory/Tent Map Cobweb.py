import matplotlib.pyplot as plt
from matplotlib.widgets import Slider
import numpy as np

fig, (ax1, ax2) = plt.subplots(1,2)
plt.subplots_adjust(bottom=0.25)

axr = plt.axes([0.15, 0.1, 0.65, 0.03])
rSlide=Slider(axr, "r", 0, 2)

r=0.5
numSteps=50

def tentCob(xy, r1):
    x,y=xy
    xDot=x
    if (y<0.5):
        yDot=r1*x
    else:
        yDot= r1*(1-x)
    return (xDot,yDot)

def linear(xy):
    x, y=xy
    return (y,y)
    
def updateVal(val):
    r=rSlide.val
    ax1.cla()
    ax2.cla()
    plotter(r)

rSlide.on_changed(updateVal)

def plotter(r1):
    xys1=np.empty((2*numSteps+1,2))
    xys1[0]=(0.4,0)
    xys2=np.empty((2*numSteps+1,2))
    xys2[0]=(0.405,0)

    xys3=np.empty((numSteps+1,2))
    xys3[0]=(0,0.4)
    xys4=np.empty((numSteps+1,2))
    xys4[0]=(0,0.405)
    
    for i in range(0,2*numSteps,2):
        xys1[i+1]=tentCob(xys1[i],r1)
        xys1[i+2]=linear(xys1[i+1])
        xys2[i+1]=tentCob(xys2[i],r1)
        xys2[i+2]=linear(xys2[i+1])
        xys3[int(i/2+1)]=(i+1,xys1[i+1][1])
        xys4[int(i/2+1)]=(i+1,xys2[i+1][1])
        
    ax1.plot([0,0.5,1],[0,r1/2,0])
    ax1.plot([0,1],[0,1])
    ax1.plot(*xys1.T,lw=0.4)
    ax1.plot(*xys2.T,lw=0.4)
    ax1.set_ylim(0,1)
    ax1.set_xlim(0,1)
    ax1.set_xlabel("x")
    ax1.set_ylabel("y")
    ax1.set_title("Tent Map")

    ax2.plot(*xys3.T,"g",lw=0.5)
    ax2.plot(*xys4.T,"r",lw=0.5)
    ax2.set_ylim(0,1)
    ax2.set_xlabel("Iterations")
    ax2.set_ylabel("x")
    
plotter(r)

plt.show()