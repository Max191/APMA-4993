# Run 1st
# Converts the dates of the file to their numerical equivalent and puts the data table back into a csv.
# Assumes no NaN entries

import pandas as pd
import datetime
from datetime import datetime


def convert_date_to_number(date):

    d2 = datetime.strptime(date, "%Y-%m-%d")
    d1 = datetime.strptime("1899-12-30", "%Y-%m-%d") # start of excel time
    return abs((d2 - d1).days)


filepath = "C:/Users/justi/Documents/Covid research/FCA_Case_Line_Data_from_DOH.csv"
df = pd.read_csv(filepath)
df_dates = df['Case_Date']
print(df.head())
for i in range(0, len(df.index)):
    df_date1 = df_dates[i]
    df_date_formatted = df_date1[0:4] + "-" + df_date1[5:7] + "-" + df_date1[8:10]
    df_date_converted = convert_date_to_number(df_date_formatted)
    df.at[i, 'Case_Date'] = df_date_converted

df_dates1 = df['Case_Date']
print(df_dates1.head())

df.to_csv('FCA_Case_Line_Data_Dates_Converted.csv', index=False,)
