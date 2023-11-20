#!/usr/bin/env python
# coding: utf-8

# In[ ]:





# In[ ]:






# In[14]:


import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

# Create a figure and a 3D subplot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Create 3D data
x = [1,2,3,4,5,6,7,8]
y = [1,2,3,4,5,6,7,8]
z = [15]

# Add more data points with unique markers
x2 = np.random.rand(10) * 5  # Generate 10 random x values between 0 and 5
y2 = np.random.rand(10) * 5  # Generate 10 random y values between 0 and 5
z2 = np.random.rand(10) * 5  # Generate 10 random z values between 0 and 5

x3 = [2, 3, 4, 5, 6, 7, 8, 9]  # Sample x values
y3 = [3, 4, 5, 6, 7, 8, 9, 10]  # Sample y values
z3 = [6, 12, 10, 9, 8, 15, 14, 11]  # Sample z values

# Plot the original data with a red circle marker
ax.scatter(x, y, z, c='r', marker='o', label='Abstract')

# Plot the additional data with a blue triangle marker
ax.scatter(x2, y2, z2, c='b', marker='^', label='Nonabstract')

ax.scatter(x3, y3, z3, c='g', marker='s', label='Control')

# Customize the 3D plot
ax.set_xlabel('Amount')
ax.set_ylabel('Amount')
ax.set_zlabel('Z Label')
ax.view_init(elev=20, azim=45)  # Adjust the viewing angle

# Add a legend
ax.legend()

# Show the 3D plot
plt.show()








# In[5]:


import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Create a figure and a 3D subplot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Create 3D data
patterned_x = [1, 2]  # Patterned Abstract and Nonabstract Colors
unpatterned_x = [4, 5]  # Unpatterned Abstract and Nonabstract Colors

# Create labels for the bars
categories = ['Patterned', 'Unpatterned']
colors = ['Abstract Colors', 'Nonabstract Colors']

# Heights of the bars (data from your example)
patterned_data = [8, 22]
unpatterned_data = [10, 15]

# Bar width
width = 0.5

# Plot the bars for Patterned and Unpatterned
ax.bar(patterned_x, patterned_data, zs=1, zdir='y', width=width, label='Patterned')
ax.bar(unpatterned_x, unpatterned_data, zs=2, zdir='y', width=width, label='Unpatterned')

# Customize the 3D plot
ax.set_xlabel('Categories')
ax.set_ylabel('Colors')
ax.set_zlabel('Values')
ax.view_init(elev=20, azim=45)  # Adjust the viewing angle

# Add a legend
ax.legend()

# Set the ticks and labels for the y-axis
ax.set_yticks([1, 2])
ax.set_yticklabels(categories)

# Set the ticks and labels for the x-axis
ax.set_xticks([1.5, 4.5])
ax.set_xticklabels(colors)

# Show the 3D plot
plt.show()


# In[20]:


import matplotlib.pyplot as plt

# Sample data
categories = ['Abstract', 'NonAbstract', 'Patterned', 'Unpatterned']
values = [5, 7, 9, 4]

# Create additional data for two more variables
values2 = [6, 4, 10, 8]
values3 = [8, 12, 6, 8]

# Create a dot plot
plt.plot(categories, values, 'ro', markersize=10, label='Variable 1')
plt.plot(categories, values2, 'bs', markersize=10, label='Variable 2')
plt.plot(categories, values3, 'g^', markersize=10, label='Variable 3')

# Customize the plot
plt.title('Dear Data')
plt.xlabel('Categories')
plt.ylabel('Amount of Artwork')

# Add a legend
plt.legend()

# Show the plot
plt.show()


# In[17]:


import matplotlib.pyplot as plt

# Sample data
categories = ['Patterned', 'Unpatterned']
abstract_colors = [8, 10]
nonabstract_colors = [22, 15]

# Create a dot plot
plt.plot(categories, abstract_colors, 'ro', markersize=10, label='Abstract Colors')
plt.plot(categories, nonabstract_colors, 'bs', markersize=10, label='Nonabstract Colors')

# Customize the plot
plt.title('Dot Plot for Abstract and Nonabstract Colors')
plt.xlabel('Categories')
plt.ylabel('Values')

# Add a legend
plt.legend()

# Show the plot
plt.show()


# In[ ]:




