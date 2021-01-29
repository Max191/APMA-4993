# Run 5th for Logistic
# Calculates mobility averages by county
import pandas as pd
import numpy as np

mobility_data_path = "C:/Users/justi/Documents/Covid research/Mobility Data/Florida Mobility Data 1-11 Counties All.xlsx"
income_data_path = 'C:/Users/justi/Documents/Covid research/Unemployment 2019.xlsx'
out_path = "Mobility_Vs_Income_All.csv"

df_mobility = pd.read_excel(mobility_data_path)
df_unemployment = pd.read_excel(income_data_path)

county = 'sub_region_2'
retail = 'retail_and_recreation_percent_change_from_baseline'
grocery = 'grocery_and_pharmacy_percent_change_from_baseline'
parks = 'parks_percent_change_from_baseline'
transit = 'transit_stations_percent_change_from_baseline'
workplaces = 'workplaces_percent_change_from_baseline'
residential = 'residential_percent_change_from_baseline'
average = 'average_percent_change_from_baseline'
header_list = [county, retail, grocery, parks, transit, workplaces, residential, average]
df_mobility_data = df_mobility[header_list]

print(df_mobility_data.head())

df_income = df_unemployment['Median Household Income']
df_income_county = df_unemployment['County']

arr_total = np.zeros(7)
arr_num = np.zeros(7)
dataset = []
current_county = df_mobility_data[county][0]


# add input parameters to dataset
def add_entry(county_name, a_total, a_num, income):
    data = [county_name, 0, 0, 0, 0, 0, 0, 0, income]
    for i in range(0, len(arr_total)):
        if a_num[i] != 0:
            data[i + 1] = a_total[i] / a_num[i]
        else:
            data[i + 1] = 0
    dataset.append(data)


for i in range(0, len(df_mobility_data[county])):
    if df_mobility_data[county][i] != "Unknown":
        if df_mobility_data[county][i] != current_county:
            add_entry(current_county, arr_total, arr_num,
                      df_income[df_income_county[df_income_county == current_county].index[0]])
            current_county = df_mobility_data[county][i]
            arr_total = np.zeros(7)
            arr_num = np.zeros(7)
        for j in range(0, len(arr_num)):
            arr_num[j] += 1
            arr_total[j] += df_mobility_data[header_list[j + 1]][i]
add_entry(current_county, arr_total, arr_num,
          df_income[df_income_county[df_income_county == current_county].index[0]])

header_list.append('income')
df_filtered_data = pd.DataFrame(data=dataset, columns=header_list)
df_filtered_data.to_csv(out_path, index=False,)
