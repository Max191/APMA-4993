# Run 3rd
# Calculates the new cases per day in the file. This one is specifically for all of Florida.
# Assumes no NaN entries
import pandas as pd
import numpy as np

filename = "csv/FCA_Case_Line_Data_Dates_Sorted.csv"
df = pd.read_csv(filename)

dates = df['Case_Date']
cases = 0
current_date = dates[0]

cases_list = []

for i in range(0, len(dates.index)):
    if dates[i] != current_date:
        cases_list.append([current_date, cases])
        cases = 1
        current_date = dates[i]
    else:
        cases += 1

# account for last line
cases_list.append([current_date, cases])

cases_list_np = np.array(cases_list)

df_infection_rate = pd.DataFrame({'Date': cases_list_np[:, 0], 'New Cases': cases_list_np[:, 1]})

df_infection_rate.to_csv('Infection_Rate_Florida_All.csv', index=False,)
