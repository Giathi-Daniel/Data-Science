import matplotlib.pyplot as plt;

x = [1, 2, 3, 4, 5, 6, 7, 8, 9]
y1 = [1, 3, 5, 3, 1, 3, 5, 3, 1]
y2 = [2, 4, 6, 4, 2, 4, 6, 4, 2]
plt.plot(x, y1, label="SEM1")
plt.plot(x, y2, label="SEM2")
plt.plot()

plt.xlabel("X axis")
plt.ylabel("Y axis")
plt.title("DISTRIBUTION PER SEM")
plt.legend()
plt.show()