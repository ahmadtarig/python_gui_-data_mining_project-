import customtkinter as tk
from stepsFiles import Cleaning, Fuzzy, K_medoid, Visualization, predection
from PIL import Image, ImageTk


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
    prediction_panel.pack(side="left", padx=10, pady=10, fill="both", expand=True)


# set mode
tk.set_appearance_mode("light")

root = tk.CTk()
root.geometry(f"1000x600+{(root.winfo_screenwidth() - 1000)//2}+{(root.winfo_screenheight() - 650)//2}")

cover = tk.CTkFrame(master=root, fg_color="skyblue", corner_radius=0, width=1000, height=600,)
cover.pack(padx=0, pady=0, fill=tk.BOTH, expand=True)


image = Image.open(r"C:\Users\Ahmed Tarek\OneDrive\Desktop\mining_project\fuzzyVisualization\background.png")
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

output = tk.CTkLabel(master=prediction_panel, bg_color="transparent", fg_color="transparent", text="dfdf",
                     text_color="blue", font=("sanserif", 18, "bold"))

predict = tk.CTkButton(master=prediction_panel, width=200, text="Predict", fg_color="blue",
                       text_color="white", corner_radius=25, height=50, font=("sanserif", 18, "bold"),
                       command=predection.predict_fun)
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
