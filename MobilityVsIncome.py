import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
import csv
from matplotlib import pyplot as plt

path = "csv/Unemployment.csv"
incomes = {}
retail_and_recreation = {}
grocery_and_pharmacy = {}
parks = {}
transit_stations = {}
workplaces = {}
residential = {}
avg = {}
num_points = {}
with open(path, "r") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")
    for line in csv_reader:
        if line[87] != '' and len(line[87]) < 10:
            incomes[line[0]] = float(line[87])

path = "csv/Mobility_by_fips.csv"
with open(path, "r") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")
    for line in csv_reader:
        if line[0] != "FIPS":
            retail_and_recreation[line[0]] = float(line[1])
            grocery_and_pharmacy[line[0]] = float(line[2])
            parks[line[0]] = float(line[3])
            transit_stations[line[0]] = float(line[4])
            workplaces[line[0]] = float(line[5])
            residential[line[0]] = float(line[6])
            avg[line[0]] = float(line[7])
            num_points[line[0]] = float(line[8])

retail_and_recreation_by_fips = []
grocery_and_pharmacy_by_fips = []
parks_by_fips = []
transit_stations_by_fips = []
workplaces_by_fips = []
residential_by_fips = []
avg_by_fips = []
incomes_by_fips = []
for fips in incomes:
    if fips in retail_and_recreation and num_points[fips] > 10:
        retail_and_recreation_by_fips.append(retail_and_recreation[fips])
        grocery_and_pharmacy_by_fips.append(grocery_and_pharmacy[fips])
        parks_by_fips.append(parks[fips])
        transit_stations_by_fips.append(transit_stations[fips])
        workplaces_by_fips.append(workplaces[fips])
        residential_by_fips.append(residential[fips])
        avg_by_fips.append(avg[fips])
        incomes_by_fips.append(incomes[fips])

x = np.array(incomes_by_fips).reshape((-1, 1))
y_retail_and_recreation = np.array(retail_and_recreation_by_fips)
y_grocery_and_pharmacy = np.array(grocery_and_pharmacy_by_fips)
y_parks = np.array(parks_by_fips)
y_transit_stations = np.array(transit_stations_by_fips)
y_workplaces = np.array(workplaces_by_fips)
y_residential = np.array(residential_by_fips)
y_avg = np.array(avg_by_fips)

print("Linear Regression:")
print()
print("Retail and Recreation:")
model = LinearRegression().fit(x, y_retail_and_recreation)
r_sq = model.score(x, y_retail_and_recreation)
print('coefficient of determination:', r_sq)
print('intercept:', model.intercept_)
print('slope:', model.coef_)
print()

print("Grocery and Pharmacy:")
model = LinearRegression().fit(x, y_grocery_and_pharmacy)
r_sq = model.score(x, y_grocery_and_pharmacy)
print('coefficient of determination:', r_sq)
print('intercept:', model.intercept_)
print('slope:', model.coef_)
print()

print("Parks:")
model = LinearRegression().fit(x, y_parks)
r_sq = model.score(x, y_parks)
print('coefficient of determination:', r_sq)
print('intercept:', model.intercept_)
print('slope:', model.coef_)
print()

print("Transit Stations:")
model = LinearRegression().fit(x, y_transit_stations)
r_sq = model.score(x, y_transit_stations)
print('coefficient of determination:', r_sq)
print('intercept:', model.intercept_)
print('slope:', model.coef_)
print()

print("Workplaces:")
model = LinearRegression().fit(x, y_workplaces)
r_sq = model.score(x, y_workplaces)
print('coefficient of determination:', r_sq)
print('intercept:', model.intercept_)
print('slope:', model.coef_)
print()

print("Residential:")
model = LinearRegression().fit(x, y_residential)
r_sq = model.score(x, y_residential)
print('coefficient of determination:', r_sq)
print('intercept:', model.intercept_)
print('slope:', model.coef_)
print()

print("Average:")
model = LinearRegression().fit(x, y_avg)
r_sq = model.score(x, y_avg)
print('coefficient of determination:', r_sq)
print('intercept:', model.intercept_)
print('slope:', model.coef_)
print()

################################################################################################
# transformer = PolynomialFeatures(degree=2, include_bias=False)
#
# print("Polynomial Regression:")
# print()
# print("Retail and Recreation:")
# model = LinearRegression().fit(x, y_retail_and_recreation)
# r_sq = model.score(x, y_retail_and_recreation)
# print('coefficient of determination:', r_sq)
# print('intercept:', model.intercept_)
# print('slope:', model.coef_)
# print()
#
# print("Grocery and Pharmacy:")
# model = LinearRegression().fit(x, y_grocery_and_pharmacy)
# r_sq = model.score(x, y_grocery_and_pharmacy)
# print('coefficient of determination:', r_sq)
# print('intercept:', model.intercept_)
# print('slope:', model.coef_)
# print()
#
# print("Parks:")
# model = LinearRegression().fit(x, y_parks)
# r_sq = model.score(x, y_parks)
# print('coefficient of determination:', r_sq)
# print('intercept:', model.intercept_)
# print('slope:', model.coef_)
# print()
#
# print("Transit Stations:")
# model = LinearRegression().fit(x, y_transit_stations)
# r_sq = model.score(x, y_transit_stations)
# print('coefficient of determination:', r_sq)
# print('intercept:', model.intercept_)
# print('slope:', model.coef_)
# print()
#
# print("Workplaces:")
# model = LinearRegression().fit(x, y_workplaces)
# r_sq = model.score(x, y_workplaces)
# print('coefficient of determination:', r_sq)
# print('intercept:', model.intercept_)
# print('slope:', model.coef_)
# print()
#
# print("Residential:")
# model = LinearRegression().fit(x, y_residential)
# r_sq = model.score(x, y_residential)
# print('coefficient of determination:', r_sq)
# print('intercept:', model.intercept_)
# print('slope:', model.coef_)
# print()
#
# print("Average:")
# model = LinearRegression().fit(x, y_avg)
# r_sq = model.score(x, y_avg)
# print('coefficient of determination:', r_sq)
# print('intercept:', model.intercept_)
# print('slope:', model.coef_)
# print()

# plt.scatter(incomes_by_fips, retail_and_recreation_by_fips, label='Retail and Recreation')
# plt.scatter(incomes_by_fips, grocery_and_pharmacy_by_fips, label='Grocery and Pharmacy')
# plt.scatter(incomes_by_fips, parks_by_fips, label='Parks')
# plt.scatter(incomes_by_fips, transit_stations_by_fips, label='Transit Stations')
# plt.scatter(incomes_by_fips, workplaces_by_fips, label='Workplaces')
# plt.scatter(incomes_by_fips, residential_by_fips, label='Residential')
# plt.scatter(incomes_by_fips, avg_by_fips, label='Average')
# plt.xlabel('Median Household Income')
# plt.ylabel('Mobility Percent Change from Baseline')
# plt.title('Florida Mobility Percent Change from Baseline vs Median Household Income')
# plt.legend()
# plt.show()