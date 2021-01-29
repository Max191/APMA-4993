import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from sklearn.linear_model import LinearRegression

file = "C:/Users/justi/PycharmProjects/COVID-19/Scripts after 12-14/MobilityAndInfectionRateAligned_January_11.csv"
df = pd.read_csv(file)

date = 'date'
cases = 'New Cases'
retail = 'retail_and_recreation_percent_change_from_baseline'
grocery = 'grocery_and_pharmacy_percent_change_from_baseline'
parks = 'parks_percent_change_from_baseline'
transit = 'transit_stations_percent_change_from_baseline'
workplaces = 'workplaces_percent_change_from_baseline'
residential = 'residential_percent_change_from_baseline'
average = 'average_percent_change_from_baseline'

delay = 22
threshold = 50
rfilter = 20

header_list = [retail, grocery]
x = df[header_list].rolling(window=rfilter).mean()
y = df[cases].rolling(window=rfilter).mean()
t = df[date].to_numpy()

x = x.iloc[threshold:]
y = y.iloc[threshold:]
t = t[threshold:]

plt.plot(t, y)
plt.show()
model = LinearRegression()
model.fit(x, y)
print("Score, without time delay: ", model.score(x, y))
print("Coefficients: ", model.coef_)
print("Intercept: ", model.intercept_)

x = x.iloc[:len(x) - delay]
y = y.iloc[delay:]
t = t[:len(t) - delay]
plt.plot(t, y)
plt.show()
model.fit(x, y)
coefs = np.array(model.coef_)
intercept = model.intercept_
print("Score, with time delay: ", model.score(x, y))
print("Coefficients: ", coefs)
print("Intercept: ", intercept)

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

ax.scatter(x.iloc[:, 0], x.iloc[:, 1], y)
x_ax = np.linspace(-50, -15, 3000)
y_ax = np.linspace(-28, -6, 3000)
z_ax = intercept + x_ax * coefs[0] + y_ax * coefs[1]
nonzero = 0
for i in z_ax:
    if i <= 0:
        nonzero += 1
    else:
        break
ax.plot(x_ax[nonzero:], y_ax[nonzero:], z_ax[nonzero:])

ax.set_xlabel("Retail Change From Baseline (avg %)")
ax.set_ylabel("Grocery Change From Baseline (avg %)")
ax.set_zlabel("New Cases")
ax.set_title("Infection Rate (New Cases) vs. Retail and Grocery Mobility")
plt.show()
# a = df[average].rolling(rfilter).mean().to_numpy().reshape(-1, 1)
# y = df[cases].rolling(rfilter).mean().to_numpy()
# a = a[threshold + rfilter:len(a) - delay]
# y = y[threshold + rfilter + delay:]
# model.fit(a, y)
# print("average: ", model.score(a, y))
