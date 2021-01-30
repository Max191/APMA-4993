import csv
import math

import pandas as pd
import datetime
from datetime import datetime


def convert_date_to_number(date):

    d2 = datetime.strptime(date, "%Y-%m-%d")
    d1 = datetime.strptime("1899-12-30", "%Y-%m-%d") # start of excel time
    return abs((d2 - d1).days)


filepath = "csv/FCA_Case_Line_Data_from_DOH_January_11.csv"
df = pd.read_csv(filepath)
df_dates = df['Case_Date']
for i in range(0, len(df.index)):
    df_date1 = df_dates[i]
    df_date_formatted = df_date1[0:4] + "-" + df_date1[5:7] + "-" + df_date1[8:10]
    df_date_converted = convert_date_to_number(df_date_formatted)
    df.at[i, 'Case_Date'] = df_date_converted

df_dates1 = df['Case_Date']
result_df = df.sort_values(by=['County', 'Case_Date'])
counties = result_df['County'].unique()
county_double_times = {}

for county in counties:
    county_cases = result_df[result_df['County'] == county]
    dates = county_cases['Case_Date'].tolist()
    doubles = int(math.log(len(dates), 2))
    index = 2**doubles - 1
    time = float(dates[index]) - float(dates[0])
    county_double_times[county] = time/float(doubles)

df_doubling_times = pd.DataFrame(list(county_double_times.items()), columns=['County', 'Avg Doubling Time'])
df_doubling_times.to_csv('csv/Florida_Avg_Doubling_Times.csv', index=False,)
