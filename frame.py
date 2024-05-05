import customtkinter as tk
# btn functions


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
right_panel = tk.CTkFrame(master=root, fg_color="#a5bcd9", corner_radius=20, bg_color="transparent")
right_panel.pack(side="left", padx=10, pady=10, fill="both", expand=True)

# create a loft panel
left_panel = tk.CTkFrame(master=root, fg_color=left_panel_color, width=300, corner_radius=20)
left_panel.pack(side="right", padx=10, pady=10, fill="y")

# add content to left panel
# exit button
exit_button = tk.CTkButton(master=left_panel, text="Exit", )

# main loop
root.mainloop()
