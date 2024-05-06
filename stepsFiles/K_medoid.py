#!/usr/bin/env python
import customtkinter as tk
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from sklearn.preprocessing import MinMaxScaler
from sklearn.metrics import silhouette_score
from sklearn_extra.cluster import KMedoids

data = pd.read_csv(r"C:\Users\Ahmed Tarek\OneDrive\Desktop\mining_project\dataSet.csv")


def get_kmedoid_panel(root):
    panel = tk.CTkScrollableFrame(master=root, fg_color="#a5bcd9", corner_radius=20,
                                  bg_color="transparent", scrollbar_button_color="blue")
    panel.pack(side="left", padx=10, pady=10, fill="both", expand=True)

    data['Post Timestamp'] = pd.to_datetime(data['Post Timestamp'])
    data.rename(columns={'Engagement Rate ': 'Engagement Rate'}, inplace=True)

    # How many post types do we have and what are their Likes count?
    types = data.groupby('Post Type')['Likes'].sum().reset_index()
    types = types.sort_values('Likes', ascending=False)

    # How many platforms do we have and what are their Engagement Rates?
    platforms = data.groupby('Platform')['Likes'].sum().reset_index()
    platforms = platforms.sort_values('Likes', ascending=False)

    # How many sentiments do we have and what are their Engagement Rates?
    sentiments = data.groupby('Sentiment')['Likes'].sum().reset_index()
    sentiments = sentiments.sort_values('Likes', ascending=False)

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

    k_values = range(2, 7)

    # List to store silhouette scores
    silhouette_scores = []

    # Iterate over each value of k
    for k in k_values:
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

    kmedoids = KMedoids(n_clusters=optimal_k, random_state=42).fit(normalized_df)

    normalized_df['Cluster'] = kmedoids.labels_

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

    post_type_results = data.groupby(['Post Type', 'Cluster']).size().unstack(fill_value=0)

    cluster_results = post_type_results.T

    # Plot a pie chart for each cluster
    for cluster in cluster_results.index:
        # Get platform distribution for the current cluster
        post_type_distribution = cluster_results.loc[cluster]

        # Create a pie chart
        plt.subplot(1, 5, i+2)
        i += +2
        plt.pie(post_type_distribution, labels=post_type_distribution.index, autopct='%1.1f%%')

        # Add a title with the cluster name
        plt.title(f'Post Type Distribution for Cluster {cluster}')

    canvas = FigureCanvasTkAgg(fig, master=panel)
    canvas.draw()
    canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH)
    return panel
    # ## Videos usually perform better
