#   This script demonstrates basic data manipulation using pandas.

import pandas as pd
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt
from datetime import datetime

#Confirm your script is using the correct working directory
import os
print("Current working directory:", os.getcwd())

# 1. Load GA4 export CSV
df = pd.read_csv("./Raminta_Ker/orders_export_pp.csv")


# #Old Path
# df = pd.read_csv("/Users/ramintakersulyte/Desktop/Hacker300/business_school_project/Raminta_Ker/data/orders_export_pp.csv")


# 2. Preview and mapped column names
print("Columns:", df.columns.tolist())

# Rename columns to match RFM model
df.rename(columns={
    'Paid at': 'purchase_date',
    'total': 'order_value',
    'email': 'transaction_id',
}, inplace=True)

# # Convert purchase date to datetime
# df['purchase_date'] = pd.to_datetime(df['purchase_date'])

# # Use transaction ID as proxy for customer
# df['customer_id'] = df['transaction_id']

# Snapshot date = day after last purchase
snapshot_date = df['purchase_date'].max() + pd.Timedelta(days=1)

# Group by customer proxy (transaction_id)
rfm = df.groupby('customer_id').agg({
    'purchase_date': lambda x: (snapshot_date - x.max()).days,
    'customer_id': 'count',  # Frequency is always 1 here unless repeat IDs exist
    'order_value': 'sum'
}).rename(columns={
    'purchase_date': 'Recency',
    'customer_id': 'Frequency',
    'order_value': 'Monetary'
})

# Drop rows with missing/zero values
rfm = rfm[rfm['Monetary'] > 0]

# Normalize RFM data
scaler = StandardScaler()
rfm_scaled = scaler.fit_transform(rfm)

# KMeans clustering
kmeans = KMeans(n_clusters=4, random_state=42)
rfm['Segment'] = kmeans.fit_predict(rfm_scaled)

# Show results
print("\nRFM Segment Summary:")
print(rfm.groupby('Segment').mean().round(1))

# Plot
import seaborn as sns
sns.pairplot(rfm.reset_index(), hue='Segment', vars=['Recency', 'Frequency', 'Monetary'])
plt.suptitle("RFM Segments from GA4 Purchase Data", y=1.02)
plt.show()

# Read CSV (with real path and delimiter if needed)
df = pd.read_csv("orders_export_pp.csv")

# Rename columns to match your file
df.rename(columns={
    'Email': 'customer_id',               # use 'Email' if available
    'Created at': 'purchase_date',
    'Total': 'order_value'
}, inplace=True)

# Convert dates
df['purchase_date'] = pd.to_datetime(df['purchase_date'], errors='coerce')

# Filter clean rows
df = df.dropna(subset=['customer_id', 'purchase_date', 'order_value'])

# Set snapshot date (usually day after last purchase)
snapshot_date = df['purchase_date'].max() + pd.Timedelta(days=1)

# Group by customer (email)
rfm = df.groupby('customer_id').agg({
    'purchase_date': lambda x: (snapshot_date - x.max()).days,
    'customer_id': 'count',
    'order_value': 'sum'
}).rename(columns={
    'purchase_date': 'Recency',
    'customer_id': 'Frequency',
    'order_value': 'Monetary'
})
# Fxing the FileNotFoundError
df = pd.read_csv("orders_export_pp.csv")

