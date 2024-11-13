# Code that creates a 3D scatter plot using Matplotlib
import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import axes3d

# Create a 3D figure and subplot:
fig = plt.figure()
ax = fig.add_subplot(111,projection='3d')

# Define data for two sets of points:
x1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
y1 = np.random.randint(10, size=10)
z1 = np.random.randint(10, size=10)
x2 = [-1, -2, -3, -4, -5, -6, -7, -8, -9, -10]
y2 = np.random.randint(-10, 0, size=10)
z2 = np.random.randint(10, size=10)

# Create scatter plots for the data
ax.scatter(x1, y1, z1, c='b', marker='o', label='blue')
ax.scatter(x2, y2, z2, c='g', marker='D', label='green')

# Set labels for the axes
ax.set_xlabel('x axis')
ax.set_ylabel('y axis')
ax.set_zlabel('z axis')

# Set the plot title and legend
plt.title("3D Scatter Plot")
plt.legend()

# Adjust subplot layout
plt.tight_layout()

# Display the 3D scatter plot
plt.show()