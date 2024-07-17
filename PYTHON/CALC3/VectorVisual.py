#!/usr/bin/env python3

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

points = np.array([[1,2],[0,0],[2,1]])
vectors = np.array([[-10,-8],[0,0],[-8,10]])

plt.figure()
plt.quiver(points[:,0], points[:,1], vectors[:,0], vectors[:,1], angles='xy', scale_units='xy', scale=1, color['blue','red','yellow'])

plt.xlim(-10,10)
plt.ylim(-10,10)

for i, (x,y) in enumerate(points):
	plt.text(x,y, f'f{x},{y}', fontsize = 12)

plt.xlabel('x')
plt.xlabel('y')
plt.title('VectorField')
plt.grid()
plt.show()
