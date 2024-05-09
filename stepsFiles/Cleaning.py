import customtkinter as tk
from path import project_path
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import seaborn as sns

def get_cleaning_panel(root, right_panel_color):
    df = pd.read_csv(project_path + "\\dataSet.csv")
    # steps panels
    cleaning_pane = tk.CTkScrollableFrame(master=root, fg_color="#a5bcd9", corner_radius=20,
                                          bg_color="transparent", scrollbar_button_color="blue")
    cleaning_pane.pack(side="left", padx=10, pady=10, fill="both", expand=True)
    # steps panels

    columns_of_interest = ['Likes', 'Comments', 'Shares']
    fig = plt.figure(figsize=(10, 6), facecolor=right_panel_color)
    plt.subplot(2, 3, 1)
    sns.boxplot(data=df[columns_of_interest], color='blue')
    plt.title('Likes VS Comment VS Shares')

    plt.subplot(2, 3, 2)
    columns_of_interest = ['Audience Age']
    sns.boxplot(data=df[columns_of_interest], color='blue')
    plt.title('Audience Age')

    plt.subplot(2, 3, 3)
    columns_of_interest = ['Reach', 'Impressions']
    sns.boxplot(data=df[columns_of_interest], color='blue')
    plt.title('Reach VS Impressions')

    # Visualize the distribution
    plt.subplot(2, 2, 3)
    sns.histplot(data=df, x='Likes', bins=10)
    plt.title('Likes')
    plt.xlabel('')

    plt.subplot(2, 2, 4)
    sns.histplot(data=df, x='Comments', bins=10)
    plt.title('Comments')
    plt.xlabel('')
    plt.ylabel('')

    plt.subplots_adjust(wspace=0.7, hspace=0.8)
    canvas = FigureCanvasTkAgg(fig, master=cleaning_pane)
    canvas.draw()
    canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH)

    fig = plt.figure(figsize=(10, 6), facecolor=right_panel_color)
    plt.subplot(2, 3, 1)
    sns.histplot(data=df, x='Shares', bins=10)
    plt.title('Shares')
    # Remove x-label and y-label
    plt.xlabel('')
    plt.ylabel('')

    plt.subplot(2, 3, 2)
    sns.histplot(data=df, x='Reach', bins=10)
    plt.title('Reach')
    plt.xlabel('')
    plt.ylabel('')

    plt.subplot(2, 3, 3)
    sns.histplot(data=df, x='Impressions', bins=10)
    plt.title('Impressions')
    plt.xlabel('')
    plt.ylabel('')

    plt.subplot(2, 1, 2)
    correlation_matrix = df[['Likes', 'Comments', 'Shares', 'Impressions', 'Reach']].corr()
    sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm')
    plt.title('Correlation Matrix')

    plt.subplots_adjust(wspace=0.7, hspace=0.8)
    canvas = FigureCanvasTkAgg(fig, master=cleaning_pane)
    canvas.draw()
    canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH)

    fig = plt.figure(figsize=(10, 6), facecolor=right_panel_color)
    sns.scatterplot(data=df, x='Likes', y='Impressions', sizes=1)
    plt.title('Likes vs. Impressions')

    plt.subplots_adjust(wspace=0.7, hspace=0.8)
    canvas = FigureCanvasTkAgg(fig, master=cleaning_pane)
    canvas.draw()
    canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH)
    return cleaning_pane
