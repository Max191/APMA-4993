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

retail_and_recreation_np = np.array([[x] for x in retail_and_recreation_by_fips])
grocery_and_pharmacy_by_fips_np = np.array([[x] for x in grocery_and_pharmacy_by_fips])
parks_by_fips_np = np.array([[x] for x in parks_by_fips])
transit_stations_by_fips_np = np.array([[x] for x in transit_stations_by_fips])
workplaces_by_fips_np = np.array([[x] for x in workplaces_by_fips])
residential_by_fips_np = np.array([[x] for x in residential_by_fips])
avg_by_fips_np = np.array([[x] for x in avg_by_fips])
incomes_by_fips_np = np.array([[x] for x in incomes_by_fips])

temp1 = np.append(retail_and_recreation_np, grocery_and_pharmacy_by_fips_np, 1)
temp2 = np.append(temp1, parks_by_fips_np, 1)
temp3 = np.append(temp2, transit_stations_by_fips_np, 1)
temp4 = np.append(temp3, workplaces_by_fips_np, 1)
temp5 = np.append(temp4, residential_by_fips_np, 1)
temp6 = np.append(temp5, avg_by_fips_np, 1)
all_data = np.append(temp6, incomes_by_fips_np, 1)

df = pd.DataFrame(all_data, columns=['retail and recreation', 'grocery and pharmacy',
                                     'parks', 'transit stations', 'workplaces', 'residential',
                                     'avg', 'incomes'])

num_bins = int(len(incomes_by_fips)/6)
name = str(num_bins) + ' income bins'
df[name] = pd.qcut(df['incomes'], q=num_bins)

boxplot = df.boxplot(column='retail and recreation', by=name)
plt.ylabel('Average Mobility Change from Baseline (%)')
plt.xlabel('Median Household Income Range (% of state total median household income)')
plt.title('Florida Retail and Recreation Mobility vs Median Household Income')
plt.show()

boxplot = df.boxplot(column='grocery and pharmacy', by=name)
plt.ylabel('Average Mobility Change from Baseline (%)')
plt.xlabel('Median Household Income Range (% of state total median household income)')
plt.title('Florida Grocery and Pharmacy Mobility vs Median Household Income')
plt.show()

boxplot = df.boxplot(column='parks', by=name)
plt.ylabel('Average Mobility Change from Baseline (%)')
plt.xlabel('Median Household Income Range (% of state total median household income)')
plt.title('Florida Parks Mobility vs Median Household Income')
plt.show()

boxplot = df.boxplot(column='transit stations', by=name)
plt.ylabel('Average Mobility Change from Baseline (%)')
plt.xlabel('Median Household Income Range (% of state total median household income)')
plt.title('Florida Transit Station Mobility vs Median Household Income')
plt.show()

boxplot = df.boxplot(column='workplaces', by=name)
plt.ylabel('Average Mobility Change from Baseline (%)')
plt.xlabel('Median Household Income Range (% of state total median household income)')
plt.title('Florida Workplace Mobility vs Median Household Income')
plt.show()

boxplot = df.boxplot(column='residential', by=name)
plt.ylabel('Average Mobility Change from Baseline (%)')
plt.xlabel('Median Household Income Range (% of state total median household income)')
plt.title('Florida Residential Mobility vs Median Household Income')
plt.show()

boxplot = df.boxplot(column='avg', by=name)
plt.ylabel('Average Mobility Change from Baseline (%)')
plt.xlabel('Median Household Income Range (% of state total median household income)')
plt.title('Florida Average Mobility vs Median Household Income')
plt.show()