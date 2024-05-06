#!/usr/bin/env python
import pandas as pd
import customtkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

df = pd.read_csv(r"C:\Users\Ahmed Tarek\OneDrive\Desktop\mining_project\dataSet.csv")


def get_visualization_panel(root):
    panel = tk.CTkScrollableFrame(master=root, fg_color="#a5bcd9", corner_radius=20,
                                  bg_color="transparent", scrollbar_button_color="blue")
    panel.pack(side="left", padx=10, pady=10, fill="both", expand=True)

    import matplotlib.pyplot as plt
    # Calculate frequency of each post type
    frequency = df['Post Type'].value_counts()

    # Define custom colors
    colors = ['lightblue', 'blue', 'skyblue']

    fig = plt.figure(figsize=(14, 6))
    plt.subplot(2, 3, 1)
    plt.pie(frequency.values, labels=frequency.index, autopct='%1.1f%%', startangle=140, colors=colors)
    plt.title('Frequency of Post Types')

    # Calculate frequency of each platform type
    frequency = df['Platform'].value_counts()

    plt.subplot(2, 3, 2)
    plt.pie(frequency.values, labels=frequency.index, autopct='%1.1f%%', startangle=140)
    plt.title('Frequency of Platform')

    import matplotlib.pyplot as plt

    # Calculate frequency of each weekday type
    frequency = df['Weekday Type'].value_counts()

    # Define custom colors
    colors = ['gray', 'lightgray']
    plt.subplot(2, 3, 3)
    plt.pie(frequency.values, labels=frequency.index, autopct='%1.1f%%', startangle=140, colors=colors)
    plt.title('Frequency of Weekday Types')

    # Calculate frequency of each age group
    frequency = df['Age Group'].value_counts()

    # Plot the bar plot
    plt.subplot(2, 3, 4)
    plt.bar(frequency.index, frequency.values, color='blue')
    plt.xlabel('Age Group')
    plt.ylabel('Frequency')
    plt.title('Frequency of Age Group')
    plt.xticks()
    plt.grid(axis='y', linestyle='--', alpha=0.7)

    # Calculate frequency of each audience gender
    frequency = df['Audience Gender'].value_counts()

    # Plot the bar plot

    plt.subplot(2, 3, 5)
    plt.bar(frequency.index, frequency.values, color='blue')
    plt.xlabel('Audience Gender')
    plt.ylabel('')
    plt.title('Frequency of Audience Gender')
    plt.grid(axis='y', linestyle='--', alpha=0.7)

    # Calculate frequency of each sentiment category
    frequency = df['Sentiment'].value_counts()

    # Plot the histogram
    plt.subplot(2, 3, 6)
    plt.hist(df['Sentiment'], bins=len(frequency), align='left', rwidth=0.99, color='blue')
    plt.xlabel('Sentiment')
    plt.ylabel('')
    plt.title('Frequency of Sentiment')
    plt.grid(axis='y', linestyle='--', alpha=0.7)

    plt.subplots_adjust(wspace=0.4, hspace=0.4)
    canvas = FigureCanvasTkAgg(fig, master=panel)
    canvas.draw()
    canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH)

    likes = df['Likes']
    comments = df['Comments']
    reach = df['Reach']
    shares = df['Shares']

    # Plotting the scatter plot
    fig = plt.figure(figsize=(14, 6))
    plt.subplot(2, 2, 1)
    plt.scatter(likes, reach, alpha=0.5)
    plt.title('Scatter Plot of Likes vs Reach')
    plt.xlabel('Likes')
    plt.ylabel('Reach')
    plt.grid(True)

    # Plotting the scatter plot
    plt.subplot(2, 2, 2)
    plt.scatter(comments, reach, alpha=0.5)
    plt.title('Scatter Plot of Comments vs Reach')
    plt.xlabel('Comments')
    plt.ylabel('Reach')
    plt.grid(True)

    # Plotting the scatter plot
    plt.subplot(2, 1, 2)
    plt.scatter(shares, reach, alpha=0.5)
    plt.title('Scatter Plot of Shares vs Reach')
    plt.xlabel('Shares')
    plt.ylabel('Reach')
    plt.grid(True)

    plt.subplots_adjust(wspace=0.7, hspace=0.8)
    canvas = FigureCanvasTkAgg(fig, master=panel)
    canvas.draw()
    canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH)

    # Plotting the scatter plot
    fig = plt.figure(figsize=(8, 6))
    plt.scatter(likes, comments, alpha=0.5)
    plt.title('Scatter Plot of Likes vs Comments')
    plt.xlabel('Likes')
    plt.ylabel('Comments')
    plt.grid(True)

    canvas = FigureCanvasTkAgg(fig, master=panel)
    canvas.draw()
    canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH)
