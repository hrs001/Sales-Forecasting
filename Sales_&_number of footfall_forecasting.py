
# Franchise Stall
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from datetime import timedelta

# Accessing dataset 
dataset = pd.read_csv("/Users/harshsrivastava/Downloads/coffee_shop_revenue.csv")
print(dataset)

##################################
# Dataset doesnot have the quantity, i am assuming it 1 for our case or can say it as number of orders and as we will be selling only chocolaty cold coffee hence the fixed price would be around INR 65 for regular or low sales day
##################################

"""Adding date 
to the dataset"""

start_date = pd.to_datetime("2023-01-01")
date_list = []

# Loop through the rows
for i in range(len(dataset)):
    # For each row, calculate the date by adding "i" days to the start_date
    new_date = start_date + timedelta(days=i)
    date_list.append(new_date)

# Assign the date list as a new column in the dataset
dataset["Date"] = date_list


"""Making a new category based column - Occassion 
[Categories - [Regular day, Low sales day, Peak day(either because of holiday or marketing campaign )] on the basis of no. of sales/or can say customer/footfall]"""

# Converting date into number (days since start) so that the clustering works
dataset["DayNumber"] = (dataset["Date"] - dataset["Date"].min()).dt.days


# Applying clustering algorithm
X = dataset[["Number_of_Customers_Per_Day"]]
kmeans = KMeans(n_clusters=3, random_state=42, n_init=10)
dataset["Cluster"] = kmeans.fit_predict(X)

# Adding label to the cluster and making a column
cluster_sales_mean = dataset.groupby("Cluster")["Number_of_Customers_Per_Day"].mean().sort_values()
labels_map = {cluster_sales_mean.index[0]: "Low busniess day", cluster_sales_mean.index[1]: "Regular Day", cluster_sales_mean.index[2]: "Peak Day"}
dataset["Occasion"] = dataset["Cluster"].map(labels_map)

#Plotting cluster
plt.figure(figsize=(10,6))
for cluster in dataset["Cluster"].unique():
    cluster_data = dataset[dataset["Cluster"] == cluster]
    plt.scatter(cluster_data["DayNumber"], cluster_data["Number_of_Customers_Per_Day"], label=labels_map[cluster])
plt.xlabel("Day Number")
plt.ylabel("Number_of_Customers_Per_Day")
plt.title("Clustering of Coffee Shop Sales")
plt.legend()
plt.show()
plt.close()
print(dataset)

"""
Finding the footfall & revenue on basis of occassion we can predict/forecast that the average sales should be this
"""


df = dataset.groupby('Occasion')["Number_of_Customers_Per_Day"].mean().reset_index()

avg_price_peak_day = 60
avg_price = 65
price = np.where(df['Occasion'] == 'Peak Day', avg_price_peak_day, avg_price)
df["Revenue (in INR)"] = df["Number_of_Customers_Per_Day"] * price
df["No. of Sachet used/day"] = np.ceil(df["Number_of_Customers_Per_Day"]).astype(int)
print(df)

