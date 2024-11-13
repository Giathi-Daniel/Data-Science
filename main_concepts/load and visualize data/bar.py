import matplotlib.pyplot as plt
import pandas as pd

mydata = pd.read_csv("./medal.csv")
country_data = mydata['country']
medal_data = mydata['gold_medal']

plt.bar(country_data, medal_data, label="AWARD",color='g')
plt.plot()

plt.xlabel("country_data")
plt.ylabel("medal_data")

plt.title("Gold medal achievements of five most successful\n"+"countries in 2023 Summer Olympics")
plt.legend()
plt.show()