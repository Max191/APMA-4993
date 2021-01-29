# Run 4th for Logistic Regression
# Filters out mobility and income data by date - removes all datapoints without a date in both mobility and
# income sets
import pandas as pd
import numpy as np

infection_rate_path = "C:/Users/justi/PycharmProjects/COVID-19/Scripts after " \
                      "12-14/Infection_Rate_Florida_Counties_January_11.csv "
mobility_path = "C:/Users/justi/Documents/Covid research/Mobility Data/Florida Mobility Data 1-11 Counties All.xlsx"

df_infection = pd.read_csv(infection_rate_path)
df_mobility = pd.read_excel(mobility_path)

county = 'sub_region_2'
date = 'date'
retail = 'retail_and_recreation_percent_change_from_baseline'
grocery = 'grocery_and_pharmacy_percent_change_from_baseline'
parks = 'parks_percent_change_from_baseline'
transit = 'transit_stations_percent_change_from_baseline'
workplaces = 'workplaces_percent_change_from_baseline'
residential = 'residential_percent_change_from_baseline'
# average = 'average_percent_change_from_baseline'
header_list = [county, date, retail, grocery, parks, transit, workplaces, residential]

mobility_list = df_mobility[header_list]
mobility_list_counties = mobility_list[county].to_numpy()
mobility_list_dates = mobility_list[date].to_numpy()
mobility_list_dates_appended = [None] * len(mobility_list_dates)

infection_list_dates = df_infection[["County", "Date"]].to_numpy()
infection_list_cases = df_infection["New Cases"].to_numpy()
infection_list_dates_appended = [None] * len(infection_list_dates)

contained_lists = []
filtered_data_complete = []

for i in range(0, len(mobility_list_dates)):
    mobility_list_dates_appended[i] = mobility_list_counties[i] + str(mobility_list_dates[i])

for i in range(0, len(infection_list_dates)):
    infection_list_dates_appended[i] = infection_list_dates[i, 0] + " County" + str(infection_list_dates[i, 1])

for i in range(0, len(mobility_list_dates_appended)):
    for j in range(0, len(infection_list_dates_appended)):
        if mobility_list_dates_appended[i] == infection_list_dates_appended[j]:
            if infection_list_dates_appended[j] not in contained_lists:
                contained_lists.append(infection_list_dates_appended[j])
                arr = [infection_list_dates_appended[j][:-5], infection_list_dates_appended[j][-5:]]
                for k in range(2, len(header_list)):
                    arr.append(mobility_list[header_list[k]][i])
                arr.append(infection_list_cases[j])
                filtered_data_complete.append(arr)

# commonalities = np.array(
# list(set(mobility_list_dates_appended) - (set(mobility_list_dates_appended) - set(infection_list_dates_appended))))

header_list.append("New Cases")
filtered_data_complete_np = np.array(filtered_data_complete)
df_filtered = pd.DataFrame(data=filtered_data_complete_np, columns=header_list)
print(df_filtered.head())
# df_filtered = pd.DataFrame(
#     {'County': filtered_data_complete_np[:, 0], 'Date': filtered_data_complete_np[:, 1],
#      'average_percent_change_from_baseline': filtered_data_complete_np[:, 2], 'New Cases': filtered_data_complete_np[:, 3]})
#
df_filtered.to_csv('Mobility_Infection_Rate_January_11_Filtered_All.csv', index=False,)
