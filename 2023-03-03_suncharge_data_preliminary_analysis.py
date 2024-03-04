#!/usr/bin/env python
# coding: utf-8

# In[1]:


import os
import glob
import pandas as pd
import numpy as np
import calendar
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
from sklearn.manifold import TSNE
from sklearn.cluster import KMeans
from scipy.cluster.hierarchy import dendrogram, linkage
from sklearn.cluster import AgglomerativeClustering
import matplotlib.pyplot as plt
import seaborn as sns

import help_functions
dataframe_obj = help_functions.Dataframes()
histogram_obj = help_functions.Histograms()
clusterer_obj = help_functions.Clusterer()
pca_obj       = help_functions.CustomPCA()
correlations_obj = help_functions.Correlations()


# In[2]:


# read in data
data_directory = "C:\\Users\\irina\\Documents\\UH\\Vizualization in Data Science DL\\suncharge\\data"
files = os.listdir(data_directory)
dataframes = {}

# Loop through each file in the data directory
for filename in os.listdir(data_directory):
    # Check if the file is a CSV
    if filename.endswith('.csv'):
        # Construct the full file path
        file_path = os.path.join(data_directory, filename)
        # Read the CSV file into a DataFrame
        df = pd.read_csv(file_path)
        # Remove the '.csv' from filename and use it as the key in the dictionary
        key_name = filename[:-4]
        # Store the DataFrame in the dictionary
        dataframes[key_name] = df
# List all keys in the 'dataframes' dictionary
#print(list(dataframes.keys()))


# In[3]:


# Looking at BOM data:
dataframe_obj.print_summary(dataframes, 'BOM')


# In[4]:


clusterer_obj.plot_hierarchical_clustering(dataframes['BOM'], figsize=(8, 4), max_d=5)


# In[5]:


clusterer_obj.visualize_clusters(dataframes['BOM'], n_clusters=4, figsize=(6, 4))


# In[6]:


# Example usage within subplots context:
fig, axs = plt.subplots(1, 2, figsize=(14, 5))  # Define the figure and axes for subplots

# Call the function for each subplot
histogram_obj.plot_horizontal(axs[0], dataframes['BOM'], 'Product Category', title='BOM Product Categories')
histogram_obj.plot_horizontal(axs[1], dataframes['BOM'], 'Finished Product', title='BOM Finished Products')

plt.tight_layout()  # Adjust the layout of the plots
plt.show()


# In[7]:


# Looking at CustomerPlantRelation:
dataframe_obj.print_summary(dataframes, 'CustomerPlantRelation')


# In[8]:


# I will take a closer look at the values of PlantKey column
histogram_obj.plot_vertical(dataframes['CustomerPlantRelation'], 'PlantKey', title="Plant Key values")


# In[9]:


#I will not do PCA or cluster analysis since I am not sure this makes sense for a mapping table


# In[10]:


# Looking at the Customers:
dataframe_obj.print_summary(dataframes, 'Customers')


# In[11]:


clusterer_obj.plot_hierarchical_clustering(dataframes['Customers'], figsize=(12, 4), max_d=5)


# In[12]:


# This data is quite inconvenient for being clustered, so I will try to split it into 2 clusters
clusterer_obj.visualize_clusters(dataframes['Customers'], n_clusters=2, figsize=(6, 4))


# In[13]:


pca_obj.perform_pca(data = dataframes['Customers'], n_components=4, plot_loadings=False)


# <br>**Comm:**<br>  <span style="font-size:13px;"> The conclusion here is that PCA is unlikely to effectively reduce the dimentionality of this set

# In[14]:


#here, where customers are residing and what is the number of customers per plant seems to be the most interesting information.
# I will take a closer look at how values are distributed
histogram_obj.plot_vertical(dataframes['Customers'], 'CustomerCountry', title='Customers by  Countries', figsize=(12, 2.5),)


# In[15]:


histogram_obj.plot_vertical(dataframes['Customers'], 'PlantKey', title='Customers by Plants', figsize=(3.5, 2.5),)


# In[16]:


# Taking a glimpes of what is in Forecast:
dataframe_obj.print_summary(dataframes, 'Forecast')


# In[17]:


histogram_obj.plot_monthly_quantity_distribution(dataframes['Forecast'], date_column = 'RequestedDeliveryMonth', quantity_column ='Quantity',  figsize=(13, 2), value_format='{:.0f} K')


# <br>**Comm:**<br>  <span style="font-size:13px;"> Having checked the seasonal pattern behind the forecast I see that Quantity correlates with the number of days in a month <br>

# In[18]:


# taking a look at the Inventory file:
dataframe_obj.print_summary(dataframes, 'Inventory')


# In[19]:


#It would be interesting to understand the principle for making snapshots, so I will take a look at the SnapshotDate values
print(dataframes['Inventory']['SnapshotDate'].value_counts())


# **Comm**<br><span style="font-size:13px;">Snapshots are taken at the end of every month 

# In[20]:


#Adding year and month columns for checking for seasonal pattern
dataframes['Inventory']['SnapshotDate'] = pd.to_datetime(dataframes['Inventory']['SnapshotDate'])
dataframes['Inventory']['Year'] = dataframes['Inventory']['SnapshotDate'].dt.year
dataframes['Inventory']['Month'] = dataframes['Inventory']['SnapshotDate'].dt.month


# In[21]:


# Example usage within subplots context:
fig, axs = plt.subplots(1, 2, figsize=(14, 5))  # Define the figure and axes for subplots

# Call the function for each subplot
histogram_obj.plot_horizontal(axs[0], dataframes['Inventory'], 'Year', title='Inventory by Years')
histogram_obj.plot_horizontal(axs[1], dataframes['Inventory'], 'Month', title='Inventory by Months')

plt.tight_layout()  # Adjust the layout of the plots
plt.show()


# In[22]:


#Prepare data for a polar plot
monthly_inventory = dataframes['Inventory'].groupby(['Year', 'Month'])['GrossInventoryQuantity'].sum().unstack(0)
years = sorted(dataframes['Inventory']['Year'].unique())
# aggregate data for a polar plot
monthly_inventory_in_transit = dataframes['Inventory'].groupby(['Year', 'Month'])['InTransitQuantity'].sum().unstack(0)


# In[23]:


histogram_obj.polar_plot(df1 = dataframes['Inventory'], df1_quantity_column = 'GrossInventoryQuantity',\
                         df2 =  dataframes['Inventory'], df2_quantity_column = 'InTransitQuantity',\
                         plot1_title="Gross Inventory", plot2_title="Inventory in Transit")


# **Commentary:**<br> 
# <span style="font-size:13px;"> The data is covering mainly 2022 and 2023 years, in 2023 the amount of inventory went significantly down, in 2023 it looks like December to April are seeing higher amount of inventory vs. April to December period<br>
# For Inventory in Transit, this is different: while total amount got down in 2023 from 2022 similarly to the Gross Inventory, amounts in transit seem to be higher in summer months 

# In[24]:


dataframe_obj.print_summary(dataframes, 'MaterialPlantRelation')


# In[25]:


# converting StandardCost to euro could be handy for the fiture
print(dataframes['MaterialPlantRelation']['Currency'].value_counts())


# In[26]:


# For the sake of simplicity I will disregard the year and convert the prices at the current value. 
exchange_rates = {
    'PLN': 0.23,  # Example rate: 1 USD = 0.93 EUR
    'EUR': 1,     # No conversion needed for EUR
    'GBP': 1.17,  # Example rate: 1 GBP = 1.17 EUR
    'SEK': 0.0089 # Example rate: 1 JPY = 0.0074 EUR
}

# Convert prices to euros
dataframes['MaterialPlantRelation']['EurStandardCost'] = dataframes['MaterialPlantRelation'].apply(lambda row: row['StandardCost'] * exchange_rates[row['Currency']], axis=1)


# In[27]:


mpr = dataframes['MaterialPlantRelation'].drop(['Currency', 'StandardCost'], axis=1)
clusterer_obj.plot_hierarchical_clustering(mpr, figsize=(12, 4), max_d=5)


# In[28]:


# It looks like this data can be clustered into a few clusters
clusterer_obj.visualize_clusters(mpr, n_clusters=6, figsize=(6, 4))


# In[29]:


pca_obj.perform_pca(data = mpr, n_components=4, plot_loadings=True)


# In[30]:


# it looks like the original features are highly correlated and this dataframe is a candidate for dimentionality reduction with 
#the cumulative explained variance ratio of the components falling in 70-90% range. 
# from this PCA we can see high correlation between InboundTRansportationTime and TotalInboundLeadTime, MaterialKey and MaterialPlantKey, 
#a significant negative correlation between labels and SafetyStockQty, we can also spot that GoodReceiptProcessingTime is not contributing much (1 value)
# to the principal components

# I will also check the correlation of the features usig the correlation matrix:
correlations_obj.plot_correlation_matrix(mpr)


# In[31]:


dataframe_obj.print_summary(dataframes, 'Materials')


# In[32]:


clusterer_obj.plot_hierarchical_clustering(dataframes['Materials'], figsize=(10, 3), max_d=5)


# In[33]:


# It looks like this data can be clustered into a few clusters
clusterer_obj.visualize_clusters(dataframes['Materials'], n_clusters=6, figsize=(6, 4))


# In[34]:


pca_obj.perform_pca(data = dataframes['Materials'], n_components=4, plot_loadings=False)


# In[35]:


dataframe_obj.print_summary(dataframes, 'Plants')


# In[36]:


clusterer_obj.plot_hierarchical_clustering(dataframes['Plants'], figsize=(10, 3), max_d=5)


# In[37]:


# It looks like this data can be clustered into a few clusters
#but this is not a very meaningful exercise for 8 plants
clusterer_obj.visualize_clusters(dataframes['Plants'], n_clusters=4, figsize=(6, 4))


# In[38]:


pca_obj.perform_pca(data = dataframes['Plants'], n_components=4, plot_loadings=True)


# In[39]:


dataframe_obj.print_summary(dataframes, 'Purchases')


# In[40]:


#for purchases, I would like to measure the time span between key dates and check for
#whether the PurchaseOrderQuantity correlates with any of those values:

# Convert columns to datetime
dataframes['Purchases']['PurchaseOrderCreationDate'] = pd.to_datetime(dataframes['Purchases']['PurchaseOrderCreationDate'])
dataframes['Purchases']['PlannedVendorShipmentDate'] = pd.to_datetime(dataframes['Purchases']['PlannedVendorShipmentDate'])
dataframes['Purchases']['ActualVendorShipmentDate'] = pd.to_datetime(dataframes['Purchases']['ActualVendorShipmentDate'])
dataframes['Purchases']['PlannedArrivalDateYard'] = pd.to_datetime(dataframes['Purchases']['PlannedArrivalDateYard'])
dataframes['Purchases']['ActualArrivalDateYard'] = pd.to_datetime(dataframes['Purchases']['ActualArrivalDateYard'])
dataframes['Purchases']['PlannedGoodsReceiptDate'] = pd.to_datetime(dataframes['Purchases']['PlannedGoodsReceiptDate'])
dataframes['Purchases']['ActualGoodsReceiptDate'] = pd.to_datetime(dataframes['Purchases']['ActualGoodsReceiptDate'])


# Calculate new columns based on datetime differences
dataframes['Purchases']['PlannedShipmentToYard'] = (dataframes['Purchases']['PlannedArrivalDateYard'] - dataframes['Purchases']['PlannedVendorShipmentDate']).dt.days
dataframes['Purchases']['ActualShipmentToYard'] = (dataframes['Purchases']['ActualArrivalDateYard'] - dataframes['Purchases']['ActualVendorShipmentDate']).dt.days
dataframes['Purchases']['PlannedYardToReceipt'] = (dataframes['Purchases']['PlannedGoodsReceiptDate'] - dataframes['Purchases']['PlannedArrivalDateYard']).dt.days
dataframes['Purchases']['ActualYardToReceipt'] = (dataframes['Purchases']['ActualGoodsReceiptDate'] - dataframes['Purchases']['ActualArrivalDateYard']).dt.days

# Calculate lead times and their delta
dataframes['Purchases']['PlannedLead'] = dataframes['Purchases']['PlannedShipmentToYard'] + dataframes['Purchases']['PlannedYardToReceipt']
dataframes['Purchases']['ActualLead'] = dataframes['Purchases']['ActualShipmentToYard'] + dataframes['Purchases']['ActualYardToReceipt']
dataframes['Purchases']['DeltaPlannedActual'] = dataframes['Purchases']['PlannedLead'] - dataframes['Purchases']['ActualLead']


# In[41]:


histogram_obj.plot_vertical(dataframes['Purchases'], column = 'PlannedShipmentToYard', title='PlannedShipmentToYard', figsize=(3.5, 2.5))


# In[42]:


histogram_obj.plot_vertical(dataframes['Purchases'], 'PlannedYardToReceipt', title='PlannedYardToReceipt', figsize=(3.5, 2.5))


# In[43]:


histogram_obj.plot_vertical(dataframes['Purchases'], column = 'ActualShipmentToYard', title='ActualShipmentToYard', figsize=(10, 2.5))


# In[44]:


histogram_obj.plot_vertical(dataframes['Purchases'], column = 'ActualYardToReceipt', title='ActualYardToReceipt', figsize=(10, 2.5))


# In[45]:


#if I look at a simplified "Purchases" dataset that does not include datetime columns
clusterer_obj.plot_hierarchical_clustering(dataframes['Purchases'], figsize=(10, 3), max_d=5)


# In[57]:


# the dataset itself is quite heavy for this clusterization, but it does not look unpromising
clusterer_obj.visualize_clusters(dataframes['Purchases'], n_clusters=10, figsize=(6, 4))


# In[47]:


correlations_obj.plot_correlation_matrix(dataframes['Purchases'])


# In[ ]:


#> **Comm:** <br>
# We can see the correlation between PlannedShipmentToYard and PlantKey, VendorKey and PlantKey, ActualLead and ActuaYardToReceipt, 
#a negative correlation between ActualYardToReceipt and DeltaPlannedActual and ActualLead and DeltaPlannedActual
#PlannedYardToReceipt is not showing any correlation in this plot, because there is just 1 value in that columnn


# In[48]:


dataframe_obj.print_summary(dataframes, 'Sales')


# In[92]:


# I will change format of some columns to datetimes 
dataframes['Sales']['RequestedDeliveryDate']  =  pd.to_datetime(dataframes['Sales']['RequestedDeliveryDate'])
dataframes['Sales']['DeliveryDate']  =  pd.to_datetime(dataframes['Sales']['DeliveryDate'])
dataframes['Sales']['deltaRequestedActualDelivery'] =  (dataframes['Sales']['DeliveryDate'] - dataframes['Sales']['RequestedDeliveryDate']).dt.days


# In[93]:


sales_encoded = pd.get_dummies(dataframes['Sales'], columns=['MaterialKey'], prefix='MK_')
sales_encoded = pd.get_dummies(sales_encoded, columns=['PlantKey'], prefix='PK_')
sales_encoded = pd.get_dummies(sales_encoded, columns=['SalesDocType'], prefix='SDT_')
sales_encoded = pd.get_dummies(sales_encoded, columns=['HighOrderQtyFlag'], prefix='HOQF_')
sales_encoded.columns


# In[94]:


# Select the subset of columns
subset = sales_encoded[['OrderQuantity', 'RequestedDeliveryDate', 'DeliveryDate', 'deltaRequestedActualDelivery',\
                   'MK__1', 'MK__2', 'PK__4', 'PK__5','PK__6', 'PK__7', 'PK__8','SDT__Express','SDT__Regular', 'HOQF__0', 'HOQF__1']]

# Calculate the correlation matrix
correlation_matrix = subset.corr()
# Set the context for the plot to make it suitably sized
sns.set(context='notebook', style='whitegrid', font_scale = 0.75)

# Create the heatmap
plt.figure(figsize=(10, 6))  # Adjust the figure size as necessary
sns.heatmap(correlation_matrix, 
            annot=True,       # Annotate the boxes with the correlation values
            cmap='coolwarm',  # Choose a color scheme
            vmin=-1, vmax=1,  # Set the color scale limits
            linewidths=.5,    # Set linewidths between squares
            annot_kws={"size": 8})

# Show the plot
plt.show()


# >**Comm:** <br> Here, the correlation between OrderQuantity and other columns is also quite low

# In[ ]:


## Checking Sales and purchases for seasonality
#Adding year and month columns for checking for seasonal pattern
dataframes['Purchases']['SnapshotDate'] = pd.to_datetime(dataframes['Purchases']['PlannedGoodsReceiptDate'])
dataframes['Purchases']['Year'] = dataframes['Purchases']['PlannedGoodsReceiptDate'].dt.year
dataframes['Purchases']['Month'] = dataframes['Purchases']['PlannedGoodsReceiptDate'].dt.month

# Aggregate data
monthly_purchases = dataframes['Purchases'].groupby(['Year', 'Month'])['PurchaseOrderQuantity'].sum().unstack(0)
years = sorted(dataframes['Purchases']['Year'].unique())
#Adding year and month columns for checking for seasonal pattern
dataframes['Sales']['RequestedDeliveryDate'] = pd.to_datetime(dataframes['Sales']['RequestedDeliveryDate'])
dataframes['Sales']['Year'] = dataframes['Sales']['RequestedDeliveryDate'].dt.year
dataframes['Sales']['Month'] = dataframes['Sales']['RequestedDeliveryDate'].dt.month

# Aggregate data
monthly_sales = dataframes['Sales'].groupby(['Year', 'Month'])['OrderQuantity'].sum().unstack(0)
years = sorted(dataframes['Sales']['Year'].unique())


common_years = sorted(set(monthly_purchases.columns) & set(monthly_sales.columns))
# Setup the figure and subplots
fig, axs = plt.subplots(1, 2, figsize=(10, 4), subplot_kw=dict(polar=True))

# Function to plot each dataset
def plot_data(ax, data, years, title):
    num_vars = len(data.index)
    angles = np.linspace(0, 2 * np.pi, num_vars, endpoint=False).tolist()
    angles += angles[:1]  # Complete the loop
    for year in years:
        if year in data.columns:  # Check if the year is in the DataFrame
            values = data[year].values.flatten().tolist()
            values += values[:1]  # Complete the loop for values
            ax.plot(angles, values, linewidth=1, linestyle='solid', label=f'Year {year}')
            ax.fill(angles, values, alpha=0.25)
    ax.set_xticks(angles[:-1])
    ax.set_xticklabels([calendar.month_abbr[month] for month in range(1, 13)])
    ax.set_title(title, fontsize=10, pad=20)

# Plot for 'monthly_purchases'
plot_data(axs[0], monthly_purchases, common_years, "Purchases")

# Plot for 'monthly_sales'
plot_data(axs[1], monthly_sales, common_years, "Sales")

# Adjust layout and add a common legend
plt.tight_layout()
fig.legend(loc='upper center', bbox_to_anchor=(0.5, -0.05), ncol=len(common_years))

plt.show()


# **Comm**<br> 
# <span style="font-size:13px;"> Inlike inventory, both sales and purchases do not differ significantly between months. There seems to be a relation with the number of days per month. 

# In[95]:


print_dataframe_summary(dataframes, 'Vendors')

