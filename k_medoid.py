#!/usr/bin/env python
import customtkinter as tk
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from sklearn.preprocessing import MinMaxScaler  # To normalize the values before the clustering
from sklearn.metrics import silhouette_score  # To optimize number of clusters
from sklearn_extra.cluster import KMedoids  # To perform k-medoids clustering

data = pd.read_csv(r"C:\Users\Ahmed Tarek\OneDrive\Desktop\mining_project\dataSet.csv")
data.head()


def get_kmedoid_panel(root):
    panel = tk.CTkScrollableFrame(master=root, fg_color="#a5bcd9", corner_radius=20,
                                  bg_color="transparent", scrollbar_button_color="blue")
    panel.pack(side="left", padx=10, pady=10, fill="both", expand=True)

    data['Post Timestamp'] = pd.to_datetime(data['Post Timestamp'])
    data.rename(columns={'Engagement Rate ': 'Engagement Rate'}, inplace=True)
    data.info()

    # ## Goal of the analysis
    # Perform K-medoids clustering on the data to gain insights on the following:
    # Which combinations of platform & post type usually perform better?
    #
    # Based on 2 metrics:
    #
    # 1- Engagment(Likes, comments,  and shares)
    #
    # 2- Reach
    #
    # Then, observe the best and worst clusters and try to conclude if the sentiment has any effect

    # How many post types do we have and what are their Likes count?
    types = data.groupby('Post Type')['Likes'].sum().reset_index()
    types = types.sort_values('Likes', ascending=False)
    print(types)

    # How many platforms do we have and what are their Engagement Rates?
    platforms = data.groupby('Platform')['Likes'].sum().reset_index()
    platforms = platforms.sort_values('Likes', ascending=False)
    print(platforms)

    # How many sentiments do we have and what are their Engagement Rates?
    sentiments = data.groupby('Sentiment')['Likes'].sum().reset_index()
    sentiments = sentiments.sort_values('Likes', ascending=False)
    print(sentiments)

    fig, axs = plt.subplots(1, 3, figsize=(15, 5))
    axs[0].bar(types['Post Type'], types['Likes'], color='blue')
    axs[0].set_title('Post Types')

    axs[1].bar(platforms['Platform'], platforms['Likes'], color='orange')
    axs[1].set_title('Platform')

    axs[2].bar(sentiments['Sentiment'], sentiments['Likes'], color='red')
    axs[2].set_title('Sentiment')

    canvas = FigureCanvasTkAgg(fig, master=panel)
    canvas.draw()
    canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH)

    # Choosing only the necessary columns for clustering
    columns_for_clustering = data[['Likes', 'Comments', 'Shares', 'Reach']]

    # Normalization
    scaler = MinMaxScaler()
    columns_for_clustering_normalized = scaler.fit_transform(columns_for_clustering)

    normalized_df = pd.DataFrame(columns_for_clustering_normalized, columns=['Likes', 'Comments', 'Shares', 'Reach'])

    normalized_df.describe()

    normalized_df['Engagment Total'] = normalized_df['Likes'] + normalized_df['Comments'] + normalized_df['Shares']
    normalized_df.drop(['Likes', 'Comments', 'Shares'], axis=1, inplace=True)

    normalized_df.head()

    # >Performing k medoids clustering, and comparing silhouette scores to determine the best number of clusters

    # Here's a simple explanation of the silhouette score:
    # 1. **Cohesion (How Close the Points Are to Each Other)**: For each data point in a cluster, the silhouette score
    # measures how close it is to the other points in the same cluster. A high cohesion means that the points within
    # the same cluster are close to each other.
    # 2. **Separation (How Far Apart the Clusters Are)**: The silhouette score also considers how far apart the
    # clusters are from each other. It measures the distance between a data point and the points in the nearest
    # neighboring cluster. A high separation means that the clusters are well-separated from each other.
    # 3. **Silhouette Score Calculation**: The silhouette score is calculated for each data point using the formula:
    #
    #    Silhouette Score = (b - a)/max(a, b)
    #
    #    where:
    #    - \(a\) is the average distance from the data point to other points in the same cluster (cohesion).
    #    - \(b\) is the average distance from the data point to points in the nearest neighboring cluster (separation).
    #    - The silhouette score ranges from -1 to 1:
    #      - A score close to +1 indicates that the data point is well-clustered and far from other clusters.
    #      - A score close to 0 indicates that the data point is close to the decision boundary between clusters.
    #      - A score close to -1 indicates that the data point may have been assigned to the wrong cluster.
    #
    # 4. **Interpretation**: To interpret the silhouette score:
    #    - A higher average silhouette score across all data points indicates better clustering.
    #    - Negative silhouette scores suggest that the data may have been clustered incorrectly.
    #
    # In summary, the silhouette score provides a way to evaluate the quality of clustering results by considering both
    # how close the points are within clusters and how well-separated the clusters are from each other. Higher
    # silhouette scores indicate better clustering.

    k_values = range(2, 7)

    # List to store silhouette scores
    silhouette_scores = []

    # Iterate over each value of k
    for k in k_values:
        # Fit K-Medoids clustering model
        # We set the random seed number to a specific value to ensure that the algorithm
        # starts with the same centers each time
        kmedoids = KMedoids(n_clusters=k, random_state=42).fit(normalized_df)
        # Compute silhouette score
        silhouette_scores.append(silhouette_score(normalized_df, kmedoids.labels_))

    # Plot silhouette scores for different values of k
    fig = plt.figure(figsize=(14, 6))
    plt.plot(k_values, silhouette_scores, marker='o')
    plt.xlabel('Number of Clusters (k)')
    plt.ylabel('Silhouette Score')
    plt.title('Silhouette Score vs. Number of Clusters')
    canvas = FigureCanvasTkAgg(fig, master=panel)
    canvas.draw()
    canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH)

    # Choose the value of k that maximizes silhouette score
    optimal_k = k_values[np.argmax(silhouette_scores)]
    print("Optimal number of clusters:", optimal_k)

    kmedoids = KMedoids(n_clusters=optimal_k, random_state=42).fit(normalized_df)

    normalized_df['Cluster'] = kmedoids.labels_
    normalized_df.head()

    cluster_labels = kmedoids.labels_

    fig = plt.figure(figsize=(14, 6))
    # Iterate over each unique cluster label
    for cluster_label in np.unique(cluster_labels):
        # Filter data points belonging to the current cluster
        cluster_points = normalized_df.values[cluster_labels == cluster_label]

        # Plot the data points with a different color for each cluster
        plt.scatter(cluster_points[:, 0], cluster_points[:, 1], label=f'Cluster {cluster_label}')

    plt.title('K-Medoids Clustering')
    plt.xlabel('Engagement (Normalized)')
    plt.ylabel('Reach (Normalized)')
    plt.legend()
    canvas = FigureCanvasTkAgg(fig, master=panel)
    canvas.draw()
    canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH)

    data['Cluster'] = kmedoids.labels_

    # # Clustering Results

    # First, we group the data by platform and see how many instances of each platform are in each cluster.
    # The platforms with the most posts in the better performing cluster are considered superior.

    platform_results = data.groupby(['Platform', 'Cluster']).size().unstack(fill_value=0)

    cluster_results = platform_results.T

    i = 1
    # Plot a pie chart for each cluster
    for cluster in cluster_results.index:
        # Get platform distribution for the current cluster
        platform_distribution = cluster_results.loc[cluster]

        fig = plt.figure(figsize=(14, 6))
        plt.subplot(1, 5,  1)
        plt.pie(platform_distribution, labels=platform_distribution.index, autopct='%1.1f%%', startangle=140)

        # Add a title with the cluster name
        plt.title(f'Platform Distribution for Cluster {cluster}')

    # Twitter & Instagram usually perform better

    # Next, we do the same thing for post types

    postType_results = data.groupby(['Post Type', 'Cluster']).size().unstack(fill_value=0)

    cluster_results = postType_results.T

    # Plot a pie chart for each cluster
    for cluster in cluster_results.index:
        # Get platform distribution for the current cluster
        postType_distribution = cluster_results.loc[cluster]

        # Create a pie chart
        plt.subplot(1, 5, i+2)
        i += +2
        plt.pie(postType_distribution, labels=postType_distribution.index, autopct='%1.1f%%')

        # Add a title with the cluster name
        plt.title(f'Post Type Distribution for Cluster {cluster}')

    canvas = FigureCanvasTkAgg(fig, master=panel)
    canvas.draw()
    canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH)
    # ## Videos usually perform better
