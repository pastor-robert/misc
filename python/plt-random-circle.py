import matplotlib.pyplot as plt
from math import pi, cos, sin
from random import random

def point(h, k, r):
    theta = random() * 2 * pi
    return h + cos(theta) * r, k + sin(theta) * r

xy = [point(1,2,1) for _ in range(30)]

plt.xkcd()
plt.scatter(*zip(*xy), marker='x')
plt.grid(color='k', linestyle=':', linewidth=1)
plt.axes().set_aspect('equal', 'datalim')
plt.show()
