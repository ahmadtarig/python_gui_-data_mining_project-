import customtkinter as tk
from PIL import Image, ImageTk
import pandas as pd
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
import seaborn as sns


def get_fuzzy_panel():
    right_panel.pack_forget()
    panel = tk.CTkScrollableFrame(master=root, fg_color="#a5bcd9", corner_radius=20,
                                  bg_color="transparent", scrollbar_button_color=left_panel_color)
    panel.pack(side="left", padx=10, pady=10, fill="both", expand=True)

    image1 = Image.open(r"C:\Users\Ahmed Tarek\OneDrive\Desktop\mining_project\fuzzyVisualization\1.png")
    photo1 = ImageTk.PhotoImage(image1)

    image2 = Image.open(r"C:\Users\Ahmed Tarek\OneDrive\Desktop\mining_project\fuzzyVisualization\2.png")
    photo2 = ImageTk.PhotoImage(image2)

    image3 = Image.open(r"C:\Users\Ahmed Tarek\OneDrive\Desktop\mining_project\fuzzyVisualization\3.png")
    photo3 = ImageTk.PhotoImage(image3)

    image4 = Image.open(r"C:\Users\Ahmed Tarek\OneDrive\Desktop\mining_project\fuzzyVisualization\4.png")
    photo4 = ImageTk.PhotoImage(image4)

    image_p = Image.open(r"C:\Users\Ahmed Tarek\OneDrive\Desktop\mining_project\fuzzyVisualization\code.png")
    photo_p = ImageTk.PhotoImage(image_p)

    image5 = Image.open(r"C:\Users\Ahmed Tarek\OneDrive\Desktop\mining_project\fuzzyVisualization\5.png")
    photo5 = ImageTk.PhotoImage(image5)

    image6 = Image.open(r"C:\Users\Ahmed Tarek\OneDrive\Desktop\mining_project\fuzzyVisualization\6.png")
    photo6 = ImageTk.PhotoImage(image6)

    image7 = Image.open(r"C:\Users\Ahmed Tarek\OneDrive\Desktop\mining_project\fuzzyVisualization\7.png")
    photo7 = ImageTk.PhotoImage(image7)

    image8 = Image.open(r"C:\Users\Ahmed Tarek\OneDrive\Desktop\mining_project\fuzzyVisualization\8.png")
    photo8 = ImageTk.PhotoImage(image8)

    # Create a label and display the image
    label1 = tk.CTkLabel(panel, image=photo1, text="")
    label1.pack(side=tk.TOP, fill=tk.BOTH, pady=20)

    label2 = tk.CTkLabel(panel, image=photo2, text="")
    label2.pack(side=tk.TOP, fill=tk.BOTH, pady=20)

    label3 = tk.CTkLabel(panel, image=photo3, text="")
    label3.pack(side=tk.TOP, fill=tk.BOTH, pady=20)

    label4 = tk.CTkLabel(panel, image=photo4, text="")
    label4.pack(side=tk.TOP, fill=tk.BOTH, pady=20)

    label_p = tk.CTkLabel(panel, image=photo_p, text="")
    label_p.pack(side=tk.TOP, fill=tk.BOTH, pady=20)

    label5 = tk.CTkLabel(panel, image=photo5, text="")
    label5.pack(side=tk.TOP, fill=tk.BOTH, pady=20)

    label6 = tk.CTkLabel(panel, image=photo6, text="")
    label6.pack(side=tk.TOP, fill=tk.BOTH, pady=20)

    label7 = tk.CTkLabel(panel, image=photo7, text="")
    label7.pack(side=tk.TOP, fill=tk.BOTH, pady=20)

    label8 = tk.CTkLabel(panel, image=photo8, text="")
    label8.pack(side=tk.TOP, fill=tk.BOTH, pady=20)

    return panel

def get_cleaning_panel():
    # steps panels
    cleaning_pane = tk.CTkScrollableFrame(master=root, fg_color="#a5bcd9", corner_radius=20,
                                          bg_color="transparent", scrollbar_button_color=left_panel_color)
    cleaning_pane.pack(side="left", padx=10, pady=10, fill="both", expand=True)
    # steps panels
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


def get_k_mediod_panel():
    panel = tk.CTkScrollableFrame(master=root, fg_color="#a5bcd9", corner_radius=20,
                                  bg_color="transparent", scrollbar_button_color=left_panel_color)
    panel.pack(side="left", padx=10, pady=10, fill="both", expand=True)

    pass


def exit_function():
    exit()


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
right_panel = tk.CTkFrame(master=root, fg_color="#a5bcd9", corner_radius=20, bg_color="transparent")
right_panel.pack(side="left", padx=10, pady=10, fill="both", expand=True)

# create a loft panel
left_panel = tk.CTkFrame(master=root, fg_color=left_panel_color, width=300, corner_radius=20)
left_panel.pack(side="right", padx=10, pady=10, fill="y")

# add content to left panel
# left panel title
steps = tk.CTkLabel(master=left_panel, text="Steps", text_color=right_panel_color, font=("sanserif", 42, "bold"),
                    bg_color="transparent", fg_color="transparent", height=40, width=300, corner_radius=20)
steps.pack(padx=0, pady=30, side="top")

# cleaning button
cleaning = tk.CTkButton(master=left_panel, text="Cleaning", text_color="white", font=("sanserif", 16, "bold"),
                        border_width=0, bg_color="transparent", fg_color="transparent", hover_color="#6666ff",
                        height=40, width=300, corner_radius=10, command=get_cleaning_panel)
cleaning.place(y=100, x=0)

# fuzzy_logic button
fuzzy_logic = tk.CTkButton(master=left_panel, text="Fuzzy logic", text_color="white", font=("sanserif", 16, "bold"),
                           border_width=0, bg_color="transparent", fg_color="transparent", hover_color="#6666ff",
                           height=40, width=300, corner_radius=10, command=get_fuzzy_panel)
fuzzy_logic.place(y=145, x=0)

# k_medoid button
k_medoid = tk.CTkButton(master=left_panel, text="K-mediod", text_color="white", font=("sanserif", 16, "bold"),
                        border_width=0, bg_color="transparent", fg_color="transparent", hover_color="#6666ff",
                        height=40, width=300, corner_radius=10)
k_medoid.place(y=190, x=0)

# main loop
root.mainloop()
