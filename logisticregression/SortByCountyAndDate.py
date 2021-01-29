# Run 2nd IF COUNTIES
# Sorts all of the rows by date and outputs to a csv

import pandas as pd

filepath = "C:/Users/justi/PycharmProjects/COVID-19/Scripts after 12-14/FCA_Case_Line_Data_Dates_Converted_January_11.csv"
df = pd.read_csv(filepath)

df_dates1 = df['Case_Date']
print(df_dates1.head())
result_df = df.sort_values(by=['County', 'Case_Date'])

result_df_dates = result_df['Case_Date']
print(result_df_dates.head())
print(result_df.head())

result_df.to_csv('FCA_Case_Line_Data_County_Dates_Sorted_January_11.csv', index=False,)
