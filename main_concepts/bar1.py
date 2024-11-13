import matplotlib.pyplot as plt
x1 = [2,3,4,5,6]
y1 = [20,40,25,10,15]
x2 = [2,4,5,6,7]
y2 = [10,15,10,10,30]

plt.bar(x1,y1, label="Campus A",color='y')
plt.bar(x2,y2, label="Campus B",color='g')
plt.plot()
plt.xlabel("UNITS REGISTERED")
plt.ylabel("NUMBER OF STUDENTS")
plt.title("UNITS REGISTRATION")
plt.legend()
plt.show()