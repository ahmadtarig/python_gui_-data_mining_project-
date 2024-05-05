import customtkinter as tk
# set mode
tk.set_appearance_mode("light")

# create frame
root = tk.CTk()
root.attributes("-fullscreen", True)

# create a top panel
top_panel = tk.CTkFrame(master=root, fg_color="white", height=70, corner_radius=10, bg_color="transparent")
top_panel.pack(side="top", padx=10, pady=0, fill="x")

# create a right panel
right_panel = tk.CTkFrame(master=root, fg_color="#a5bcd9", corner_radius=20, bg_color="transparent")
right_panel.pack(side="left", padx=10, pady=10, fill="both", expand=True)

# create a loft panel
left_panel = tk.CTkFrame(master=root, fg_color="blue", width=300, corner_radius=20)
left_panel.pack(side="right", padx=10, pady=10, fill="y")

# add content to left panel
# exit button
exit_button = tk.CTkButton(master=left_panel, text="Exit", )

# main loop
root.mainloop()
