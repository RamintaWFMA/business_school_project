import pandas as pd
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt
from datetime import datetime
import seaborn as sns
# Show current working directory
# print("Current working directory:", os.getcwd())

# Load Omnisend Export & add the sep argument corrected if needed
df = pd.read_csv("./Raminta_Ker/orders_export_pp.csv", sep=";") 

#Trying tab separator correct sep argument
# df = pd.read_csv("./Raminta_Ker/orders_export_pp.csv", sep="\t")

# Preview column names
print("Columns:", df.columns.tolist())

# Rename columns to RFM-friendly names
df.rename(columns={
    'Email': 'customer_id',
    'Created at': 'purchase_date',
    'Total': 'order_value'
}, inplace=True)

# Clean and convert data
df['purchase_date'] = pd.to_datetime(df['purchase_date'], errors='coerce')

# If Total column includes currency symbols, clean them:
# df['order_value'] = df['order_value'].replace('[\$,]', '', regex=True).astype(float)

# Remove rows with missing critical values
df.dropna(subset=['customer_id', 'purchase_date', 'order_value'], inplace=True)

# Set snapshot date = day after latest purchase
snapshot_date = df['purchase_date'].max() + pd.Timedelta(days=1)

# Calculate RFM per customer
rfm = df.groupby('customer_id').agg({
    'purchase_date': lambda x: (snapshot_date - x.max()).days,  # Recency
    'customer_id': 'count',                                     # Frequency
    'order_value': 'sum'                                        # Monetary
}).rename(columns={
    'purchase_date': 'Recency',
    'customer_id': 'Frequency',
    'order_value': 'Monetary'
})

# Remove customers with zero spend
rfm = rfm[rfm['Monetary'] > 0]

# Normalize RFM
scaler = StandardScaler()
rfm_scaled = scaler.fit_transform(rfm)

# Cluster with KMeans
kmeans = KMeans(n_clusters=4, random_state=42)
rfm['Segment'] = kmeans.fit_predict(rfm_scaled)

# Calculate Silhouette score
from sklearn.metrics import silhouette_score
score = silhouette_score(rfm_scaled, rfm['Segment'])
print(f"\n🧪 Silhouette Score for KMeans clustering: {score:.3f}")

#Add human readable segment labels
segment_labels = {
    0: "Cold One-Timers",
    1: "Growing Potential",
    2: "Lapsed Customers",
    3: "Recent Repeat Buyers"
}
rfm['Segment_Label'] = rfm['Segment'].map(segment_labels)

# Show summary
print("\n📊 RFM Segment Summary:")
print(rfm.groupby('Segment')[['Recency', 'Frequency', 'Monetary']].mean().round(1))

# Visualize segments
sns.pairplot(rfm.reset_index(), hue='Segment_Label', vars=['Recency', 'Frequency', 'Monetary'])
plt.suptitle("RFM Segments from Omnisend Order Export", y=1.02)
plt.show()

# Optional: Export to CSV
rfm.to_csv("rfm_segmented_customers.csv")

rfm['Segment_Label'] = rfm['Segment'].map(segment_labels)

#inspect min and max dates
print("Min purchase date:", df['purchase_date'].min())
print("Max purchase date:", df['purchase_date'].max())

#Confirm the delimiter with a quick check
with open("./Raminta_Ker/orders_export_pp.csv", "r") as f:
    print(f.readline())

