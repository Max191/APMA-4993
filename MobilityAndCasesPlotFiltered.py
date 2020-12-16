# Run 5th
# Same as the other plotting file, except this one smooths out the curves by adding a rolling average.
# Window size was defined arbitrarily (20), this is subject to change
from matplotlib import pyplot as plt
import pandas as pd

mobility_path = "C:/Users/justi/Documents/Covid research/Mobility Data/Florida Mobility Data 12-14.xlsx"
infection_path = "C:/Users/justi/PycharmProjects/COVID-19/Scripts after 12-14/Infection_Rate_Florida_All.csv"

df_mobility = pd.read_excel(mobility_path)
df_infection_rate = pd.read_csv(infection_path)

df_mobility_dates = df_mobility['date']
df_mobility_averages = df_mobility['average_percent_change']

df_infection_dates = df_infection_rate['Date'].rolling(20).mean().to_numpy()
df_infection_cases = df_infection_rate['New Cases'].rolling(20).mean().to_numpy()

# subtract 2; one for indexing at 0, one for header names in the first row
df_mobility_dates = df_mobility_dates[:300].rolling(20).mean().to_numpy()
df_mobility_averages = df_mobility_averages[:300].rolling(20).mean().to_numpy()

fig = plt.figure()
ax1 = fig.add_subplot(111)
ax1.plot(df_mobility_dates, df_mobility_averages)
ax1.set_ylabel('Average Mobility Change From Baseline (%)')

ax2 = ax1.twinx()
ax2.plot(df_infection_dates, df_infection_cases, 'r-')
ax2.set_ylabel('New Cases Per Day', color='r')
for tl in ax2.get_yticklabels():
    tl.set_color('r')

plt.tight_layout()
plt.show()




