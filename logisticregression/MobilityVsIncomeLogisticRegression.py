# Multinomial Logistic Regression with K-Means Clustering
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn import metrics
from yellowbrick.cluster import KElbowVisualizer
from scipy.spatial.distance import cdist
from sklearn.cluster import KMeans
from scipy.stats import zscore
from matplotlib.ticker import MaxNLocator
from scipy.special import expit

data_path = "Mobility_Vs_Income_All.csv"
df_data = pd.read_csv(data_path)

# header names
county = 'sub_region_2'
retail = 'retail_and_recreation_percent_change_from_baseline'
grocery = 'grocery_and_pharmacy_percent_change_from_baseline'
parks = 'parks_percent_change_from_baseline'
transit = 'transit_stations_percent_change_from_baseline'
workplaces = 'workplaces_percent_change_from_baseline'
residential = 'residential_percent_change_from_baseline'
average = 'average_percent_change_from_baseline'
income = 'income'
header_list = [retail, grocery, parks, transit, workplaces, residential]
df_income_zscore = zscore(df_data[income])
x = df_income_zscore.reshape(-1, 1)

# variable for tracking figure index
index = 0
# range to test number of clusters
kmeans_range = range(1, 20)
# for debugging
header_list_accurate = []


# generates a k-mean graph of distortion vs. number of clusters and returns the kmean model with the optimal number of clusters,
# seen from the elbow method
# also creates a logistic model with optimal number of clusters, classifies the mobilities into said clusters, and then fits the 
# the classifications to income with the logistic model. Prints out the number of clusters used, model accuracy, and cluster centers
# to the console.
def graph_kmeans(df, message):
    kmean = KMeans()
    visualizer = KElbowVisualizer(kmean, k=(min(kmeans_range), max(kmeans_range)),
                                  title=message + " distortion score elbow method for k means clustering")
    visualizer.fit(df)
    visualizer.show()

    kmean = KMeans(n_clusters=visualizer.elbow_value_)
    kmean.fit(df)
    y = kmean.labels_
    model = LogisticRegression().fit(x, y)
    print(message + "| clusters: ", visualizer.elbow_value_, "| accuracy: ", model.score(x, y),
          "| clusters at: ", kmean.cluster_centers_)
    return kmean


# mobility vs. income, combined
df_mobilities_zscores = df_data[header_list].apply(zscore)
graph_kmeans(df_mobilities_zscores, "All mobilities combined")

# mobility vs income classifications, individal
for i in range(0, len(header_list)):
    df_mobility_var_zscore = zscore(df_data[header_list[i]]).reshape(-1, 1)

    kmean = graph_kmeans(df_mobility_var_zscore, header_list[i])
    y = kmean.labels_

    index += 1
    fig = plt.figure(index)
    ax = fig.add_subplot(111)
    ax.scatter(x, y)
    ax.set_title(header_list[i] + " classification")
    ax.set_xlabel("Income Z-score")
    ax.set_ylabel("Mobility State")
    ax.yaxis.set_major_locator(MaxNLocator(integer=True))
    # plt.scatter(x, y)
    # plt.title(header_list[i] + " classification")
    # plt.xlabel("Income Z-score")
    # plt.ylabel("Mobility State")

    index += 1
    plt.figure(index)
    plt.scatter(x, df_mobility_var_zscore)
    centers = kmean.cluster_centers_
    x_plot = np.linspace(-3.5, 3.5, 300)
    for k in range(0, len(centers)):
        boundary = x_plot * 0 + centers[k]
        plt.plot(x_plot, boundary)
    plt.title(header_list[i] + " scatter")
    plt.xlabel("Income Z-score")
    plt.ylabel("Mobility Z-score")
    plt.show()

