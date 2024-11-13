import matplotlib.pyplot as plt
MONTHS = [ 1, 2, 3, 4, 5, 6, 7, 8, 9]
GEORGE = [23, 40, 28, 43, 8, 44, 43, 18, 17]
PETER = [17, 30, 22, 14, 17, 17, 29, 22, 30]
JOYCE = [15, 31, 18, 22, 18, 19, 13, 32, 39]
# Adding legend for stack plots is tricky.
plt.plot([], [], color='r', label = 'GEORGE')
plt.plot([], [], color='g', label = 'PETER')
plt.plot([], [], color='b', label = 'JOYCE')
plt.stackplot(MONTHS, GEORGE, PETER, JOYCE, colors= ['r', 'g', 'b'])
plt.xlabel("MONTH")
plt.ylabel("POINTS")
plt.title('POINTS GARNERED BY MEMBERS')
plt.legend()
plt.show()