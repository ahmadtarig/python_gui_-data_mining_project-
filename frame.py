import customtkinter as tk
# set mode
tk.set_appearance_mode("light")

# create frame
root = tk.CTk()
root.attributes("-fullscreen", True)

# create a loft panel
left_panel = tk.CTkFrame(master=root, fg_color="blue", width=200, corner_radius=0)
left_panel.pack(side="right", padx=0, pady=0, fill="y")

# main loop
root.mainloop()
