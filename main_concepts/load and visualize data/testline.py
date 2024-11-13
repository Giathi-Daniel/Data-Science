import matplotlib.pyplot as plt
import pandas as pd

mydata = pd.read_csv("./test2.csv")
name_data = mydata["Name"]
age_data = mydata["Age"]
city_data = mydata["City"]
salary_data = mydata["Salary"]

plt.plot(salary_data, age_data, label="DISTRIBUTION", color="g")
plt.plot()

plt.xlabel("Salary Data")
plt.ylabel("Age Data")
# plt.clabel("city_data")

plt.title("DISTRIBUTION OF AGE, CITY AND SALARY")
plt.legend()
plt.show()