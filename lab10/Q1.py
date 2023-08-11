"""
 Author: Sumeyye Acar
 Id: 22103640
 Course: CS-115
 Semester: Summer 2023
 Assignment: Lab10 - Q1
"""

import matplotlib.pyplot as plt
import numpy as np

# X-axis
temp = np.array( [-10, -5, 0, 5, 10, 15, 20, 25, 30] )

# Dens values
dens = np.array( [1.341, 1.316, 1.293, 1.269, 1.247, 1.225, 1.204, 1.184, 1.164] )

# data points as blue circles  
plt.plot(temp, dens, 'bo') 

# calculates the coefficient 
coef = np.polyfit(temp, dens, 1)

# evaluates y-axis using coef and X-axis values
y1= np.polyval(coef, temp) 

# plot a red linear graph using x and y axises
plt.plot(temp, y1, 'r-')

# Title and Labels
plt.title('Density of Water')
plt.xlabel('Temperature')
plt.ylabel('Density')

# show
plt.show()
