import customtkinter as tk
from path import project_path
from stepsFiles import Cleaning, Fuzzy, K_medoid, Visualization
from PIL import Image, ImageTk


def predict_fun():
    try:
        f_likes = int(l_likes.get())
        f_comments = int(l_comments.get())
        f_shares = int(l_shares.get())
    except:
        return

    # !/usr/bin/env python
    import numpy as np
    import pandas as pd
    import skfuzzy as fuzz
    from skfuzzy import control as ctrl
    import warnings

    warnings.filterwarnings('ignore')
    df = pd.read_csv(project_path  + "\\dataSet.csv")
    # Define linguistic variables for likes
    likes = ctrl.Antecedent(np.arange(0, 1001, 1), 'likes')
    likes['low'] = fuzz.trimf(likes.universe, [0, 0, 500])
    likes['medium'] = fuzz.trimf(likes.universe, [250, 500, 750])
    likes['high'] = fuzz.trimf(likes.universe, [500, 1000, 1000])

    # Define linguistic variables for shares
    shares = ctrl.Antecedent(np.arange(0, 201, 1), 'shares')
    shares['low'] = fuzz.trimf(shares.universe, [0, 0, 100])
    shares['medium'] = fuzz.trimf(shares.universe, [50, 100, 150])
    shares['high'] = fuzz.trimf(shares.universe, [100, 200, 200])

    # Define linguistic variables for comments
    comments = ctrl.Antecedent(np.arange(0, 501, 1), 'comments')
    comments['low'] = fuzz.trimf(comments.universe, [0, 0, 250])
    comments['medium'] = fuzz.trimf(comments.universe, [125, 250, 375])
    comments['high'] = fuzz.trimf(comments.universe, [250, 500, 500])

    # Define linguistic variables for reach
    reach = ctrl.Consequent(np.arange(500, 5001, 1), 'reach')
    reach['very_low'] = fuzz.trimf(reach.universe, [500, 500, 1500])
    reach['low'] = fuzz.trimf(reach.universe, [1000, 1500, 2500])
    reach['medium'] = fuzz.trimf(reach.universe, [2000, 2500, 3500])
    reach['high'] = fuzz.trimf(reach.universe, [3000, 3500, 4500])
    reach['very_high'] = fuzz.trimf(reach.universe, [4000, 4500, 5000])

    import warnings
    warnings.filterwarnings('ignore', category=UserWarning)

    # Inference Rules
    # Define fuzzy rules to infer membership of data points in clusters
    # Rule 1 when low likes
    rule1 = ctrl.Rule(likes['low'] & shares['low'] & comments['low'], reach['very_low'])
    # Rule 2
    rule2 = ctrl.Rule(likes['low'] & shares['low'] & comments['medium'], reach['low'])
    # Rule 3
    rule3 = ctrl.Rule(likes['low'] & shares['low'] & comments['high'], reach['medium'])
    # Rule 4
    rule4 = ctrl.Rule(likes['low'] & shares['medium'] & comments['low'], reach['low'])
    # Rule 5
    rule5 = ctrl.Rule(likes['low'] & shares['medium'] & comments['medium'], reach['medium'])
    # Rule 6
    rule6 = ctrl.Rule(likes['low'] & shares['medium'] & comments['high'], reach['high'])
    # Rule 7
    rule7 = ctrl.Rule(likes['low'] & shares['high'] & comments['low'], reach['medium'])
    # Rule 8
    rule8 = ctrl.Rule(likes['low'] & shares['high'] & comments['medium'], reach['high'])
    # Rule 9
    rule9 = ctrl.Rule(likes['low'] & shares['high'] & comments['high'], reach['very_high'])
    # Rule 10
    rule10 = ctrl.Rule(likes['medium'] & shares['low'] & comments['low'], reach['low'])
    # Rule 11
    rule11 = ctrl.Rule(likes['medium'] & shares['low'] & comments['medium'], reach['medium'])
    # Rule 12
    rule12 = ctrl.Rule(likes['medium'] & shares['low'] & comments['high'], reach['high'])
    # Rule 13
    rule13 = ctrl.Rule(likes['medium'] & shares['medium'] & comments['low'], reach['medium'])
    # Rule 14
    rule14 = ctrl.Rule(likes['medium'] & shares['medium'] & comments['medium'], reach['high'])
    # Rule 15
    rule15 = ctrl.Rule(likes['medium'] & shares['medium'] & comments['high'], reach['very_high'])
    # Rule 16
    rule16 = ctrl.Rule(likes['medium'] & shares['high'] & comments['low'], reach['high'])
    # Rule 17
    rule17 = ctrl.Rule(likes['medium'] & shares['high'] & comments['medium'], reach['very_high'])
    # Rule 18
    rule18 = ctrl.Rule(likes['medium'] & shares['high'] & comments['high'], reach['very_high'])
    # Rule 19
    rule19 = ctrl.Rule(likes['high'] & shares['low'] & comments['low'], reach['medium'])
    # Rule 20
    rule20 = ctrl.Rule(likes['high'] & shares['low'] & comments['medium'], reach['high'])
    # Rule 21
    rule21 = ctrl.Rule(likes['high'] & shares['low'] & comments['high'], reach['very_high'])
    # Rule 22
    rule22 = ctrl.Rule(likes['high'] & shares['medium'] & comments['low'], reach['high'])
    # Rule 23
    rule23 = ctrl.Rule(likes['high'] & shares['medium'] & comments['medium'], reach['very_high'])
    # Rule 24
    rule24 = ctrl.Rule(likes['high'] & shares['medium'] & comments['high'], reach['very_high'])
    # Rule 25
    rule25 = ctrl.Rule(likes['high'] & shares['high'] & comments['low'], reach['very_high'])
    # Rule 26
    rule26 = ctrl.Rule(likes['high'] & shares['high'] & comments['medium'], reach['very_high'])
    # Rule 27
    rule27 = ctrl.Rule(likes['high'] & shares['high'] & comments['high'], reach['very_high'])

    social_media_system = ctrl.ControlSystem(
        [rule1, rule2, rule3, rule4, rule5, rule6, rule7, rule8, rule9, rule10, rule11, rule12, rule13, rule14, rule15,
         rule16, rule17, rule18, rule19, rule20, rule21, rule22, rule23, rule24, rule25, rule26, rule27])

    # Create fuzzy simulator
    social_media_simulator = ctrl.ControlSystemSimulation(social_media_system)

    # Select a random sample of 100 rows from the DataFrame
    sample_df = df[['Likes', 'Shares', 'Comments', 'Reach']].sample(n=100, random_state=42)

    predicted_reach = []
    reach_classification = []
    for index, row in sample_df.iterrows():
        # Input values for the fuzzy logic model
        likes_val = row['Likes']
        shares_val = row['Shares']
        comments_val = row['Comments']

        # Reset the control system simulation for each iteration
        social_media_simulator.reset()

        # Set input values
        social_media_simulator.input['likes'] = likes_val
        social_media_simulator.input['shares'] = shares_val
        social_media_simulator.input['comments'] = comments_val

        # Compute the result
        social_media_simulator.compute()

        # Get the predicted reach
        predicted_reach_val = social_media_simulator.output['reach']
        # Classify predicted reach
        reach_class = np.argmax([fuzz.interp_membership(reach.universe, reach['very_low'].mf, predicted_reach_val),
                                 fuzz.interp_membership(reach.universe, reach['low'].mf, predicted_reach_val),
                                 fuzz.interp_membership(reach.universe, reach['medium'].mf, predicted_reach_val),
                                 fuzz.interp_membership(reach.universe, reach['high'].mf, predicted_reach_val),
                                 fuzz.interp_membership(reach.universe, reach['very_high'].mf, predicted_reach_val)])
        predicted_reach.append(predicted_reach_val)
        reach_classification.append(['very_low', 'low', 'medium', 'high', 'very_high'][reach_class])

    # Step 3: Add the predicted reach values as a new column to the sample DataFrame
    sample_df['predicted_reach'] = predicted_reach
    sample_df['reach_classification'] = reach_classification

    # The Algorithm on one example
    social_media_simulator.input['likes'] = f_likes
    social_media_simulator.input['shares'] = f_shares
    social_media_simulator.input['comments'] = f_comments
    social_media_simulator.compute()
    predicted_reach_val = social_media_simulator.output['reach']
    # Set text to the entry widget
    output.configure(text=f"The predicted reach is {predicted_reach_val}")


def match_cleaning():
    cleaning_panel.pack(side="left", padx=10, pady=10, fill="both", expand=True)
    fuzzy_panel.pack_forget()
    k_medoid_panel.pack_forget()
    visualization_panel.pack_forget()
    prediction_panel.pack_forget()


def match_fuzzy():
    cleaning_panel.pack_forget()
    fuzzy_panel.pack(side="left", padx=10, pady=10, fill="both", expand=True)
    k_medoid_panel.pack_forget()
    visualization_panel.pack_forget()
    prediction_panel.pack_forget()


def match_kmedoid():
    cleaning_panel.pack_forget()
    fuzzy_panel.pack_forget()
    k_medoid_panel.pack(side="left", padx=10, pady=10, fill="both", expand=True)
    visualization_panel.pack_forget()
    prediction_panel.pack_forget()


def match_visualization():
    cleaning_panel.pack_forget()
    fuzzy_panel.pack_forget()
    k_medoid_panel.pack_forget()
    visualization_panel.pack(side="left", padx=10, pady=10, fill="both", expand=True)
    prediction_panel.pack_forget()


def match_prediction():
    cleaning_panel.pack_forget()
    fuzzy_panel.pack_forget()
    k_medoid_panel.pack_forget()
    visualization_panel.pack_forget()
    prediction_panel.pack(side="left", padx=10, pady=10, fill="both", expand=True)


# set mode
tk.set_appearance_mode("light")

root = tk.CTk()
root.geometry(f"1000x600+{(root.winfo_screenwidth() - 1000)//2}+{(root.winfo_screenheight() - 650)//2}")

cover = tk.CTkFrame(master=root, fg_color="skyblue", corner_radius=0, width=1000, height=600,)
cover.pack(padx=0, pady=0, fill=tk.BOTH, expand=True)


image = Image.open(project_path + "\\fuzzyVisualization\\background.png")
photo = ImageTk.PhotoImage(image)

# Create a canvas to place the background image
canvas = tk.CTkCanvas(cover, width=40, height=60)
canvas.place(x=0, y=0, relwidth=0.4, relheight=1)

# Place the background image on the canvas
canvas.create_image(0, 0, anchor="n", image=photo)
# Make sure to keep a reference to the image object
canvas.image = photo

title1 = tk.CTkLabel(master=cover, text="Data Mining Project", text_color="skyblue", bg_color="transparent",
                     fg_color="white", width=650, font=("sanserif", 64, "bold"))

title1.pack(pady=50, padx=0)

title2 = tk.CTkLabel(master=cover, text="social media engagement", text_color="#a5bcd9", fg_color="transparent",
                     bg_color="white", width=400, font=("sanserif", 32, "bold"))
title2.pack(pady=0, padx=0)

started_button = tk.CTkButton(master=cover, text="Get Started", text_color="white", fg_color="blue", border_width=0,
                              bg_color="transparent", font=("sanserif", 20, "bold"), corner_radius=30,
                              command=root.destroy, width=100, height=50)
started_button.pack(pady=150, padx=0, side="top")

root.mainloop()

# create frame
root = tk.CTk()
root.attributes("-fullscreen", True)

# colors
top_panel_color = "white"
left_panel_color = "blue"
right_panel_color = "#a5bcd9"
# colors

# create a top prediction_panel
top_panel = tk.CTkFrame(master=root, fg_color="white", height=70, corner_radius=10, bg_color="transparent")
top_panel.pack(side="top", padx=10, pady=0, fill="x")

# top prediction_panel component
# title label
title = tk.CTkLabel(master=top_panel, text="Data Mining Project", text_color="#6e8091",
                    font=("sanserif", 28, "bold"), bg_color="transparent")
title.pack(padx=20, pady=20, side="left")

# exit button
exit_button = tk.CTkButton(master=top_panel, text="Exit", font=("Sanserif", 14, "bold"), text_color="red",
                           bg_color="transparent", fg_color="transparent", border_color="red", border_width=3,
                           corner_radius=25, width=130, height=35, hover_color="#ffb3b3", command=exit)
exit_button.pack(padx=20, pady=0, side="right")
# top prediction_panel component

# create a loft prediction_panel
left_panel = tk.CTkFrame(master=root, fg_color=left_panel_color, width=300, corner_radius=20)
left_panel.pack(side="right", padx=10, pady=10, fill="y")

prediction_panel = tk.CTkScrollableFrame(master=root, fg_color="#a5bcd9", corner_radius=20,
                                         bg_color="transparent", scrollbar_button_color="blue")
prediction_panel.pack(side="left", padx=10, pady=10, fill="both", expand=True)

label = tk.CTkLabel(master=prediction_panel, bg_color="transparent", fg_color="transparent", text="Prediction",
                    text_color="white", font=("sanserif", 64, "bold"))
label.pack(pady=50)

l_likes = tk.CTkEntry(master=prediction_panel, width=360, placeholder_text="likes...", fg_color="white",
                      text_color="blue", corner_radius=10, height=40)
l_likes.pack(pady=10)

l_comments = tk.CTkEntry(master=prediction_panel, width=360, placeholder_text="comments...", fg_color="white",
                         text_color="blue", corner_radius=10, height=40)
l_comments.pack(pady=10)

l_shares = tk.CTkEntry(master=prediction_panel, width=360, placeholder_text="shares...", fg_color="white",
                       text_color="blue", corner_radius=10, height=40)
l_shares.pack(pady=10)

output = tk.CTkLabel(master=prediction_panel, bg_color="transparent", fg_color="transparent", text="",
                     text_color="blue", font=("sanserif", 18, "bold"))

predict = tk.CTkButton(master=prediction_panel, width=200, text="Predict", fg_color="blue",
                       text_color="white", corner_radius=25, height=50, font=("sanserif", 18, "bold"),
                       command= predict_fun)
predict.pack(pady=80)

output.pack(pady=50)


#  ## prediction
# side panels
cleaning_panel = Cleaning.get_cleaning_panel(root=root, right_panel_color=right_panel_color)
fuzzy_panel = Fuzzy.get_fuzzy_panel(root)
k_medoid_panel = K_medoid.get_kmedoid_panel(root)
visualization_panel = Visualization.get_visualization_panel(root)
# side panels

# forget the pack
fuzzy_panel.pack_forget()
k_medoid_panel.pack_forget()
visualization_panel.pack_forget()
prediction_panel.pack_forget()
# forget the pack

# add content to left prediction_panel
# left prediction_panel title
steps = tk.CTkLabel(master=left_panel, text="Steps", text_color=right_panel_color, font=("sanserif", 42, "bold"),
                    bg_color="transparent", fg_color="transparent", height=40, width=300, corner_radius=20)
steps.pack(padx=0, pady=30, side="top")

# cleaning button
cleaning = tk.CTkButton(master=left_panel, text="Cleaning", text_color="white", font=("sanserif", 16, "bold"),
                        border_width=0, bg_color="transparent", fg_color="transparent", hover_color="#6666ff",
                        height=40, width=300, corner_radius=10, command=match_cleaning)
cleaning.place(y=100, x=0)

# fuzzy_logic button
fuzzy_logic = tk.CTkButton(master=left_panel, text="Fuzzy logic", text_color="white", font=("sanserif", 16, "bold"),
                           border_width=0, bg_color="transparent", fg_color="transparent", hover_color="#6666ff",
                           height=40, width=300, corner_radius=10, command=match_fuzzy)
fuzzy_logic.place(y=145, x=0)

# k_medoid button
k_medoid = tk.CTkButton(master=left_panel, text="K-mediod", text_color="white", font=("sanserif", 16, "bold"),
                        border_width=0, bg_color="transparent", fg_color="transparent", hover_color="#6666ff",
                        height=40, width=300, corner_radius=10, command=match_kmedoid)
k_medoid.place(y=190, x=0)

# visualization button
visualization = tk.CTkButton(master=left_panel, text="Visualization", text_color="white", font=("sanserif", 16, "bold"),
                             border_width=0, bg_color="transparent", fg_color="transparent", hover_color="#6666ff",
                             height=40, width=300, corner_radius=10, command=match_visualization)
visualization.place(y=235, x=0)

# visualization button
prediction = tk.CTkButton(master=left_panel, text="Prediction", text_color="blue", font=("sanserif", 16, "bold"),
                          border_width=0, bg_color="transparent", fg_color="white", hover_color="lightblue",
                          height=40, width=120, corner_radius=50, command=match_prediction)
prediction.pack(side="bottom", pady=130)
# main loop
root.mainloop()
