from string import whitespace

import customtkinter as tk
import pandas as pd
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
# mport numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# import data set

# btn functions


def cleaning1_functions():
    df = pd.read_csv(r"C:\Users\Ahmed Tarek\OneDrive\Desktop\mining_project\dataSet.csv")
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
    canvas = FigureCanvasTkAgg(fig, master=right_panel)
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
    canvas = FigureCanvasTkAgg(fig, master=right_panel)
    canvas.draw()
    canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH)

    fig = plt.figure(figsize=(10, 6), facecolor=right_panel_color)
    sns.scatterplot(data=df, x='Likes', y='Impressions')
    plt.title('Likes vs. Impressions')

    plt.subplots_adjust(wspace=0.7, hspace=0.8)
    canvas = FigureCanvasTkAgg(fig, master=right_panel)
    canvas.draw()
    canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH)


def exit_function():
    root.destroy()


# btn functions

# set mode
tk.set_appearance_mode("light")

# create frame
root = tk.CTk()
root.attributes("-fullscreen", True)

# colors
top_panel_color = "white"
left_panel_color = "blue"
right_panel_color = "#a5bcd9"
# colors

# create a top panel
top_panel = tk.CTkFrame(master=root, fg_color="white", height=70, corner_radius=10, bg_color="transparent")
top_panel.pack(side="top", padx=10, pady=0, fill="x")

# top panel component
# title label
title = tk.CTkLabel(master=top_panel, text="Data Mining Project", text_color="#6e8091",
                    font=("sanserif", 28, "bold"), bg_color="transparent")
title.pack(padx=20, pady=20, side="left")

# exit button
exit_button = tk.CTkButton(master=top_panel, text="Exit", font=("Sanserif", 14, "bold"), text_color="red",
                           bg_color="transparent", fg_color="transparent", border_color="red", border_width=3,
                           corner_radius=25, width=130, height=35, hover_color="#ffb3b3", command=exit_function)
exit_button.pack(padx=20, pady=0, side="right")
# top panel component

# create a right panel
right_panel = tk.CTkScrollableFrame(master=root, fg_color="#a5bcd9", corner_radius=20,
                                    bg_color="transparent", scrollbar_button_color=left_panel_color)
right_panel.pack(side="left", padx=10, pady=10, fill="both", expand=True)

# create a loft panel
left_panel = tk.CTkFrame(master=root, fg_color=left_panel_color, width=300, corner_radius=20)
left_panel.pack(side="right", padx=10, pady=10, fill="y")

# add content to left panel
# left panel title
steps = tk.CTkLabel(master=left_panel, text="Steps", text_color=right_panel_color, font=("sanserif", 42, "bold"),
                    bg_color="transparent", fg_color="transparent", height=40, width=300, corner_radius=20)
steps.pack(padx=0, pady=30, side="top")

# cleaning1 button
cleaning1 = tk.CTkButton(master=left_panel, text="Cleaning 1", text_color="white", font=("sanserif", 16, "bold"),
                         border_width=0, bg_color="transparent", fg_color="transparent", hover_color="#6666ff",
                         height=40, width=300, corner_radius=10, command=cleaning1_functions)
cleaning1.place(y=100, x=0)

# cleaning2 button
cleaning2 = tk.CTkButton(master=left_panel, text="Cleaning 2", text_color="white", font=("sanserif", 16, "bold"),
                         border_width=0, bg_color="transparent", fg_color="transparent", hover_color="#6666ff",
                         height=40, width=300, corner_radius=10)
cleaning2.place(y=145, x=0)

# fuzzy_logic button
fuzzy_logic = tk.CTkButton(master=left_panel, text="Fuzzy logic", text_color="white", font=("sanserif", 16, "bold"),
                           border_width=0, bg_color="transparent", fg_color="transparent", hover_color="#6666ff",
                           height=40, width=300, corner_radius=10)
fuzzy_logic.place(y=190, x=0)

# k_medoid button
k_medoid = tk.CTkButton(master=left_panel, text="K-mediod", text_color="white", font=("sanserif", 16, "bold"),
                        border_width=0, bg_color="transparent", fg_color="transparent", hover_color="#6666ff",
                        height=40, width=300, corner_radius=10)
k_medoid.place(y=235, x=0)

# main loop
root.mainloop()
