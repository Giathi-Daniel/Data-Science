import matplotlib.pyplot as plt # create plots and charts
import pandas as pd # data manipulation

mydata = pd.read_csv("./medal.csv")
country_data = mydata['country']
medal_data = mydata['gold_medal']

plt.plot(country_data, medal_data, label="DISTRIBUTION",color='g')

# Creates the line plot but doesn't display it immediately. It prepares the
# plot for further customization
plt.plot() 

plt.xlabel("country_data")
plt.ylabel("medal_data")
plt.title("Gold medal achievements of five most successful\n"+"countries in 2023 Summer Olympics")
plt.legend()
plt.show()