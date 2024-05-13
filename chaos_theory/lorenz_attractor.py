import matplotlib.pyplot as plt
from matplotlib.widgets import Slider
import numpy as np

s=10
r=28
p=2.5

def lorenz(xyz, s1, r1, p1):
    x, y, z = xyz
    x_dot = s1*(y - x)
    y_dot = r1*x - y - x*z
    z_dot = x*y - p1*z
    return np.array([x_dot, y_dot, z_dot])

dt = 0.01
num_steps = 10000

xyzs = np.empty((num_steps + 1, 3))
xyzs[0] = (0., 1., 1.05)
for i in range(num_steps):
    xyzs[i + 1] = xyzs[i] + lorenz(xyzs[i], s, r, p) * dt

# Plot
ax = plt.figure().add_subplot(projection='3d')
plt.subplots_adjust(bottom=0.35)

axs = plt.axes([0.25, 0.2, 0.65, 0.03])
axr = plt.axes([0.25, 0.15, 0.65, 0.03])
axp = plt.axes([0.25, 0.1, 0.65, 0.03])

sSlide=Slider(axs,"s",0,50,10)
rSlide=Slider(axr,"r",0,50,28)
pSlide=Slider(axp,"p",0,50,2.5)

ax.plot(*xyzs.T, lw=0.6)
ax.set_xlabel("X Axis")
ax.set_ylabel("Y Axis")
ax.set_zlabel("Z Axis")
ax.set_title("Lorenz Attractor")

def updateVal(val):
    r=rSlide.val
    s=sSlide.val
    p=pSlide.val
    
    xyzs[0] = (0., 1., 1.05)
    for i in range(num_steps):
        xyzs[i + 1] = xyzs[i] + lorenz(xyzs[i], s, r, p) * dt
    ax.clear()
    ax.plot(*xyzs.T, lw=0.6)

sSlide.on_changed(updateVal)
pSlide.on_changed(updateVal)
rSlide.on_changed(updateVal)

plt.show()
