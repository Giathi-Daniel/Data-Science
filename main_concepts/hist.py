import matplotlib.pyplot as plt
import numpy as np

n = 5 + np.random.randn(100)

m = [m for m in range(len(n))]
plt.bar(m,n)
plt.title("Raw Data")
plt.show()

plt.hist(n, bins = 20) # no. of intervals you want to divide your data
plt.title("Histogram")
plt.show()

plt.hist(n, cumulative=True, bins=20, edgecolor="yellow", color="green") 
plt.title("Cumulative Histogram")
plt.show()