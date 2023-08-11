"""
 Author: Sumeyye Acar
 Id: 22103640
 Course: CS-115
 Semester: Summer 2023
 Assignment: Lab10 - Q2
"""

import numpy as np
import matplotlib.pyplot as plt

# read data, skip first 2 rows
arr_pop = np.loadtxt('pop_data.txt', skiprows=2)

# create an array with data only if the first colum is 2
arr_amer = arr_pop[arr_pop[:,0] == 2] 


## FIGURE 1
# name it a unique name
plt.figure(1)
# clear if not clean
plt.clf()

# sub-plot1: 1 row, 2 columns, position index: 1
plt.subplot(1,2,1)

# 100 - second column (-.-.- line, asterisk marker, red)
plt.plot((100 - arr_amer[:,1]),'-.*r')

# 100 - third column (dotted line, pentagon marker, black)
plt.plot((100 - arr_amer[:,2]), ':pk')

# Labels & Legends
plt.xlabel('Country Indexes')
plt.ylabel('Literacy Rate')
plt.legend(['Men', 'Women'])

# subplot 2: 1 row, 2 columns, position index: 2
plt.subplot(1,2,2)

# bar width
bar_width = 0.5

# bars: starting position, data, width, alignment
plt.bar( 2, arr_amer[:,3], bar_width, align = 'edge' )
plt.bar( 2, arr_amer[:,4], -bar_width, align = 'edge' )

# Title & Legends & Labels
plt.xlabel('Gender')
plt.ylabel('Education Rates')
plt.title('Education Rates for the Americas by Gender')
plt.legend(['Men', 'Women'])




## FIGURE 2
# name a unique plt
plt.figure(2)
# Clear if not clean
plt.clf()

# sub-plot 1: 2 rows, 1 column, position index: 1
plt.subplot(2,1,1)

# data form row 27 column 4 and 5
t_data = [arr_pop[27,3], arr_pop[27,4]]

# Title & Labels
plt.title( 'Education Rates by Gender in Turkey' )
labels = ( 'Male', 'Female' )

# Pia chart = data, labels, autopct (%1.2f = 2 decimals after '.', %% = one % sign)
plt.pie( t_data, labels = labels, autopct='%1.2f%%' )


# sub-plot 2: 2 row, 1 column, position index: 2
plt.subplot( 2, 1, 2 )

# Title
plt.title( 'Frequency of Infant Mortality in the Americas' )

# histogram = data, number of bins
plt.hist( arr_amer[:,5], 4 )
