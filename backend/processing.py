import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

def process_locations():
    # Load dataset
    df = pd.read_csv("locations.csv", names=["latitude", "longitude", "is_customer"])

    # Cluster customers using K-Means
    customer_data = df[df["is_customer"] == 1][["latitude", "longitude"]].values
    kmeans = KMeans(n_clusters=5, random_state=0).fit(customer_data)
    
    df["cluster"] = -1
    df.loc[df["is_customer"] == 1, "cluster"] = kmeans.labels_

    # Generate cluster visualization
    plt.scatter(df["longitude"], df["latitude"], c=df["cluster"], cmap="viridis", marker="o")
    plt.title("Customer Clustering")
    plt.xlabel("Longitude")
    plt.ylabel("Latitude")
    plt.savefig("static/cluster_map.png")  # Save image for frontend
    plt.close()

    return {
        "message": "Processing completed",
        "image_url": "/static/cluster_map.png"
    }
