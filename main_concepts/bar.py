import matplotlib.pyplot as plt
x1 = ["BSE", "BSCIT", "BBIT", "BCS", "BCM"]
y1 = [200,400,250,180,180]

plt.bar(x1,y1, label="yellow Bar",color='y')
plt.plot()
plt.xlabel("COURSE")
plt.ylabel("NUMBER OF STUDENTS")
plt.title("INTAKE AS PER THE COURSES")
plt.legend()
plt.show()