import customtkinter as tk
from stepsFiles import Cleaning, Fuzzy, K_medoid, Visualization


def match_cleaning():
    cleaning_panel.pack(side="left", padx=10, pady=10, fill="both", expand=True)
    fuzzy_panel.pack_forget()
    k_medoid_panel.pack_forget()
    visualization_panel.pack_forget()


def match_fuzzy():
    cleaning_panel.pack_forget()
    fuzzy_panel.pack(side="left", padx=10, pady=10, fill="both", expand=True)
    k_medoid_panel.pack_forget()
    visualization_panel.pack_forget()


def match_kmedoid():
    cleaning_panel.pack_forget()
    fuzzy_panel.pack_forget()
    k_medoid_panel.pack(side="left", padx=10, pady=10, fill="both", expand=True)
    visualization_panel.pack_forget()


def match_visualization():
    cleaning_panel.pack_forget()
    fuzzy_panel.pack_forget()
    k_medoid_panel.pack_forget()
    visualization_panel.pack(side="left", padx=10, pady=10, fill="both", expand=True)


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
                           corner_radius=25, width=130, height=35, hover_color="#ffb3b3", command=exit)
exit_button.pack(padx=20, pady=0, side="right")
# top panel component

# create a loft panel
left_panel = tk.CTkFrame(master=root, fg_color=left_panel_color, width=300, corner_radius=20)
left_panel.pack(side="right", padx=10, pady=10, fill="y")

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
# forget the pack

# add content to left panel
# left panel title
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

# main loop
root.mainloop()
