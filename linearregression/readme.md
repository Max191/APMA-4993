README
Contains scripts and certain data for linear regression and multiple regression. 
Output paths not changed.
Run order is:
1. ConvertDates.py - converts FCA case line dates to integers, calculated as the difference in the day since Excel's epoch time.
2. SortByDate.py - sorts FCA case line data by date
3. InfectionRateAllFlorida.py - calculates infection rate, as new cases per day, in all of Florida
4. "MobilityAndInfectionRateAligned_January_11.csv" was created by filtering out the dates that only contained either infection rate data or mobility data. This was created by hand.
  The file is provided in the folder as well.
5. Mobility_IR_LinearRegression.py/Mobility_IR_MultipleRegression.py - creates the linear/multiple regression plots and information
