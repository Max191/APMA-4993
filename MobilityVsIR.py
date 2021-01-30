import numpy as np
import pandas as pd
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
ir = {}
with open(path, "r") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")
    for line in csv_reader:
        if line[87] != '' and len(line[87]) < 10:
            incomes[line[0]] = float(line[87])

path = "csv/Doubling_time_by_fips.csv"
with open(path, "r") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")
    for line in csv_reader:
        if line[0] != "FIPS":
            ir[line[0]] = float(line[2])

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
ir_by_fips = []
for fips in incomes:
    if fips in retail_and_recreation and fips in ir and num_points[fips] > 10:
        retail_and_recreation_by_fips.append(retail_and_recreation[fips])
        grocery_and_pharmacy_by_fips.append(grocery_and_pharmacy[fips])
        parks_by_fips.append(parks[fips])
        transit_stations_by_fips.append(transit_stations[fips])
        workplaces_by_fips.append(workplaces[fips])
        residential_by_fips.append(residential[fips])
        avg_by_fips.append(avg[fips])
        incomes_by_fips.append(incomes[fips])
        ir_by_fips.append(ir[fips])

retail_and_recreation_np = np.array([[x] for x in retail_and_recreation_by_fips])
grocery_and_pharmacy_by_fips_np = np.array([[x] for x in grocery_and_pharmacy_by_fips])
parks_by_fips_np = np.array([[x] for x in parks_by_fips])
transit_stations_by_fips_np = np.array([[x] for x in transit_stations_by_fips])
workplaces_by_fips_np = np.array([[x] for x in workplaces_by_fips])
residential_by_fips_np = np.array([[x] for x in residential_by_fips])
avg_by_fips_np = np.array([[x] for x in avg_by_fips])
incomes_by_fips_np = np.array([[x] for x in incomes_by_fips])
ir_by_fips_np = np.array([[x] for x in ir_by_fips])

temp1 = np.append(retail_and_recreation_np, grocery_and_pharmacy_by_fips_np, 1)
temp2 = np.append(temp1, parks_by_fips_np, 1)
temp3 = np.append(temp2, transit_stations_by_fips_np, 1)
temp4 = np.append(temp3, workplaces_by_fips_np, 1)
temp5 = np.append(temp4, residential_by_fips_np, 1)
temp6 = np.append(temp5, avg_by_fips_np, 1)
temp7 = np.append(temp6, incomes_by_fips_np, 1)
all_data = np.append(temp7, ir_by_fips_np, 1)

df = pd.DataFrame(all_data, columns=['retail and recreation', 'grocery and pharmacy',
                                     'parks', 'transit stations', 'workplaces', 'residential',
                                     'avg', 'incomes', 'ir'])

X = df[['retail and recreation', 'grocery and pharmacy', 'parks', 'transit stations', 'workplaces', 'residential']]
y = df['ir']

X1 = df[['retail and recreation']]
X2 = df[['grocery and pharmacy']]
X3 = df[['parks']]
X4 = df[['transit stations']]
X5 = df[['workplaces']]
X6 = df[['residential']]

model = LinearRegression()
model.fit(X,y)

print("Multiple linear regression (retail & recreation, grocery & pharmacy vs doubling time):")
r_sq = model.score(X, y)
print('coefficient of determination:', r_sq)
print('intercept:', model.intercept_)
print('slope:', model.coef_)
print()

print("Linear regression (retail and recreation vs doubling time):")
model.fit(X1,y)
r_sq = model.score(X1, y)
print('coefficient of determination:', r_sq)
print('intercept:', model.intercept_)
print('slope:', model.coef_)
print()

print("Linear regression (grocery and pharmacy vs doubling time):")
model.fit(X2,y)
r_sq = model.score(X2, y)
print('coefficient of determination:', r_sq)
print('intercept:', model.intercept_)
print('slope:', model.coef_)
print()

print("Linear regression (parks vs doubling time):")
model.fit(X3,y)
r_sq = model.score(X3, y)
print('coefficient of determination:', r_sq)
print('intercept:', model.intercept_)
print('slope:', model.coef_)
print()

print("Linear regression (transit stations vs doubling time):")
model.fit(X4,y)
r_sq = model.score(X4, y)
print('coefficient of determination:', r_sq)
print('intercept:', model.intercept_)
print('slope:', model.coef_)
print()

print("Linear regression (workplaces vs doubling time):")
model.fit(X5,y)
r_sq = model.score(X5, y)
print('coefficient of determination:', r_sq)
print('intercept:', model.intercept_)
print('slope:', model.coef_)
print()

print("Linear regression (residential vs doubling time):")
model.fit(X6,y)
r_sq = model.score(X6, y)
print('coefficient of determination:', r_sq)
print('intercept:', model.intercept_)
print('slope:', model.coef_)
print()