# Step 1: Import libraries
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

# Step 2: Load data
df = pd.read_csv(r'C:\Users\Banana\Documents\BIS Lab Report\BIS Lab 3\Lab_3_Data.csv')

# Step 3: Select relevant features
data = df[['Sales', 'Profit']].dropna()

# Step 4: Scale data
scaler = StandardScaler()
data_scaled = scaler.fit_transform(data)

# Step 5: Elbow Method to find optimal k
inertia = []
K_range = range(1, 11)

for k in K_range:
    kmeans = KMeans(n_clusters=k, random_state=42)
    kmeans.fit(data_scaled)
    inertia.append(kmeans.inertia_)

# Plot the Elbow Graph
plt.figure(figsize=(8, 5))
plt.plot(K_range, inertia, 'bo-')
plt.xlabel('Number of clusters (k)')
plt.ylabel('Inertia')
plt.title('Elbow Method For Optimal k')
plt.grid(True)
plt.show()

# Step 6: Apply KMeans using optimal k (choose based on the elbow, say k=3)
optimal_k = 3  # Update this after viewing the elbow plot
kmeans = KMeans(n_clusters=optimal_k, random_state=42)
data['Cluster'] = kmeans.fit_predict(data_scaled)

# Step 7: Plot using different markers
markers = ['o', 's', '^', 'P', '*', 'X', 'D']
plt.figure(figsize=(8, 6))

for cluster in range(optimal_k):
    cluster_data = data[data['Cluster'] == cluster]
    plt.scatter(
        cluster_data['Sales'],
        cluster_data['Profit'],
        marker=markers[cluster % len(markers)],
        label=f'Cluster {cluster}',
        edgecolor='black',
        s=80
    )

plt.title(f'Customer Segmentation using K-Means (k={optimal_k}) with Symbols')
plt.xlabel('Sales')
plt.ylabel('Profit')
plt.legend()
plt.grid(True)
plt.show()