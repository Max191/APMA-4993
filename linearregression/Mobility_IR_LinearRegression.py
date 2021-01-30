import pandas as pd
import numpy as np
import datetime
from datetime import datetime
from matplotlib import pyplot as plt
from sklearn.linear_model import LinearRegression

df = pd.read_csv(
    "C:/Users/justi/PycharmProjects/COVID-19/Scripts after 12-14/MobilityAndInfectionRateAligned_January_11.csv")

df_time = df['Date'].to_numpy()
df_mobility = df['average_percent_change_from_baseline'].rolling(20).mean().to_numpy()
df_infection_rate = df['New Cases'].rolling(20).mean().to_numpy()
# df_infection_rate_percentages = df['cases_infection_rate_percentages'].rolling(20).mean().to_numpy()
# cut out the first 50 values to start after covid starts rolling out
df_time = df_time[50:]
df_mobility = df_mobility[50:]
df_infection_rate = df_infection_rate[50:]
# df_infection_rate_percentages = df_infection_rate_percentages[50:]
# plt.plot(df_time, df_mobility)
# plt.show()

best_offset = 0
highest_rsq = 0
# iterates through an offset and finds the offset that generates the highest r_sq linear model.
for offset in range(0, 100):
    # cut out the first 20 points in each set due to the rolling filter window of size 20
    df_mobility_sample = df_mobility[20:len(df_mobility) - offset].reshape(-1, 1)
    df_infection_rate_sample = df_infection_rate[offset + 20:]
    # df_infection_rate_percentages_sample = df_infection_rate_percentages[offset + 20:]
    model = LinearRegression()
    model.fit(df_mobility_sample, df_infection_rate_sample)
    model = LinearRegression().fit(df_mobility_sample, df_infection_rate_sample)
    r_sq = model.score(df_mobility_sample, df_infection_rate_sample)

    if r_sq > highest_rsq:
        highest_rsq = r_sq
        best_offset = offset

print("highest r_sq", highest_rsq)
print("best offset", best_offset)

fig, ax1 = plt.subplots()

# plot mobility vs. time and new cases vs. time
x = df_time[20:len(df_mobility) - best_offset].reshape(-1, 1)
ax1.plot(x, df_mobility[20:len(df_mobility) - best_offset])
ax1.set_xlabel("Date (Year-Month-Day)")
ax1.set_ylabel('Average Mobility Change From Baseline (%)')
start, end = ax1.get_xlim()
ax1.xaxis.set_ticks(np.arange(start, end, (end-start)/5))

ax2 = ax1.twinx()
ax2.plot(x, df_infection_rate[best_offset + 20:], 'r-')
ax2.set_ylabel('New Cases', color='r')
for tl in ax2.get_yticklabels():
    tl.set_color('r')
plt.title("New Cases vs. Average Mobility with Offset: " + str(best_offset))
xticks = ax1.xaxis.get_major_ticks()
xticks[0].label1.set_visible(False)

# convert time labels to string dates
numerical_labels, locs = plt.xticks()
date_labels = []
unix_epoch = datetime.utcfromtimestamp(0)
excel_epoch = datetime.strptime("1899-12-30", "%Y-%m-%d")
difference = (unix_epoch - excel_epoch).total_seconds()

for i in range(0, len(numerical_labels)):
    # multiply by seconds in a day, then subtract for epoch time differences (excel epoch starts at the end of 12/30/1899)
    seconds = numerical_labels[i] * 86400 - difference + 86400
    date = datetime.fromtimestamp(seconds).strftime("%Y-%m-%d")
    date_labels.append(date)

plt.xticks(numerical_labels, date_labels)
plt.show()

# plot new cases vs. average mobility
plt.scatter(df_mobility[20:len(df_mobility) - best_offset], df_infection_rate[best_offset + 20:])
plt.xlabel("Average Mobility % Change From Baseline")
plt.ylabel("New Cases")
plt.title("New Cases (shifted by " + str(best_offset) + " days) vs. Average Mobility")
plt.show()
# for debugging purposes
df_out = pd.DataFrame({"Date": df_time[20:], "Mobility": df_mobility[20:], "New Cases": df_infection_rate[20:]})

# df_out.to_csv("MobilityAndInfectionRateFiltered_Jan_11.csv")
