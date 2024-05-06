import customtkinter as tk

import frame


def predict_fun():
    try:
        f_likes = int(frame.l_likes.get())
        f_comments = int(frame.l_comments.get())
        f_shares = int(frame.l_shares.get())
    except:
        return

    print(f_likes)
    print(f_comments)
    print(f_shares)
    # !/usr/bin/env python
    import numpy as np
    import pandas as pd
    import skfuzzy as fuzz
    from skfuzzy import control as ctrl
    import warnings

    warnings.filterwarnings('ignore')
    df = pd.read_csv(r"C:\Users\Ahmed Tarek\OneDrive\Desktop\mining_project\dataSet.csv")
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
    frame.output.configure(text=f"The predicted reach is {predicted_reach_val}")
