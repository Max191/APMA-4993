import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
import csv
from matplotlib import pyplot as plt

path = "csv/Unemployment.csv"
incomes = {}
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

ir_by_fips = []
incomes_by_fips = []
for fips in ir:
    if fips in incomes:
        ir_by_fips.append(ir[fips])
        incomes_by_fips.append(incomes[fips])

incomes_by_fips_np = np.array([[x] for x in incomes_by_fips])
ir_by_fips_np = np.array([[x] for x in ir_by_fips])
data = np.append(incomes_by_fips_np, ir_by_fips_np, 1)
df = pd.DataFrame(data, columns=['incomes', 'doubling time'])

num_bins = int(len(incomes_by_fips)/7)
name = str(num_bins) + ' income bins'
df[name] = pd.qcut(df['incomes'], q=num_bins)

boxplot = df.boxplot(column='doubling time', by=name)

plt.ylabel('Average doubling time (days)')
plt.xlabel('Median Household Income (% of state total median household income)')
plt.title('Florida Doubling Time vs Median Household Income')
plt.show()