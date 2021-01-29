# Run 3rd IF COUNTIES
# Calculates the new cases per day in the file. This one is specifically for the counties of Florida.
# Assumes no NaN entries
import pandas as pd
import numpy as np

filename = "C:/Users/justi/PycharmProjects/COVID-19/Scripts after 12-14/FCA_Case_Line_Data_County_Dates_Sorted_January_11.csv"
df = pd.read_csv(filename)

dates = df['Case_Date']
counties = df['County']
cases = 0
current_county = counties[0]
current_date = dates[0]

cases_list = []

for i in range(0, len(dates.index)):
    if counties[i] != current_county:
        cases_list.append([current_county, current_date, cases])
        cases = 1
        current_date = dates[i]
        current_county = counties[i]
    elif dates[i] != current_date:
        cases_list.append([current_county, current_date, cases])
        cases = 1
        current_date = dates[i]
    else:
        cases += 1

# account for last line
cases_list.append([current_county, current_date, cases])

cases_list_np = np.array(cases_list)

df_infection_rate = pd.DataFrame(
    {'County': cases_list_np[:, 0], 'Date': cases_list_np[:, 1], 'New Cases': cases_list_np[:, 2]})

df_infection_rate.to_csv('Infection_Rate_Florida_Counties_January_11.csv', index=False, )
