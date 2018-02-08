import numpy as np
import matplotlib.pyplot as plt
from math import pi

n = 6
x = np.linspace(-1, n*pi+1, 1000)
y1 = np.sin(x)
y2 = np.cos(x)
y3 = y1*y2
y4 = y1+y2

plt.xkcd()
plt.plot(x, y1, '-b', label='sine')
plt.plot(x, y2, '-r', label='cosine')
plt.plot(x, y3, '-g', label='sine * cosine')
plt.plot(x, y4, '-y', label='sine + cosine')
plt.xticks([i*pi for i in range(n+1)],
           ["%d*PI"%i if i else "0" for i in range(n+1)],
           #fontsize = 18,
           )
           # ["$%d\pi$"%i for i in range(n)])
plt.xlim(-1, n*pi+1)
plt.grid(color='k', linestyle=':', linewidth=1)
plt.legend(loc='upper right')
plt.ylim(-1.5, 2.0)
plt.show()

