README
Contains necessary scripts/certain datasets necessary for logistic regression.
Output Paths have not been changed.
Run order is:
1. ConvertDates.py - changes FCA case line dates to an integer, calculated as the difference between date stated and excel's epoch time.
2. SortByCountyAndDate.py - sorts FCA case line data by county then by date
3. InfectionRateCounties.py - calculates infection rate as new cases per day in each county
4. FilterCountyData.py - removes data points in mobility and infection rate that do not have the same date in both datasets. Requires filtered mobilities by excel,
  "Florida Mobility Data 1-11 Counties All.xlsx"
5. MobilityVsIncomePreprocessing.py - calculates averages for each mobility by county and adds county incomes. Requires income data, "Unemployment 2019.xlsx"
6. MobilityVsIncomeLogisticRegression.py - creates elbow method for k means clustering and multinomial logistic regression models.
