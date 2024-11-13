import matplotlib.pyplot as plt
import pandas as pd

mydata = pd.read_csv("./medal.csv")
country_data = mydata['country']
medal_data = mydata['gold_medal']

plt.bar(country_data, medal_data, label="AWARD",color='g')

fig, ax = plt.subplots(figsize = (16, 9))
ax.barh(country_data, medal_data) # creates a horizontal bar chart ax.barh()
ax.xaxis.set_tick_params(pad = 5) # tick label padding for the x-axis
ax.yaxis.set_tick_params(pad = 10) # tick label padding for the y-axis
# add horizontal guideline to the plot's x-axis for better readability
ax.xaxis.grid(True, color ='grey',
    linestyle ='-', linewidth = 1.5,
    alpha = 0.5)
ax.set_axisbelow(True) # ensure the bars are drawn below the guidelines
ax.invert_yaxis() # display the countries from top to bottom

plt.ylabel("country_data")
plt.xlabel("medal_data")
plt.title("Gold medal achievements of five most successful\n"+"countries in 2023 Summer Olympics")
plt.legend()
plt.show()
