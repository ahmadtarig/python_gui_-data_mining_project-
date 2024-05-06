import customtkinter as tk
from PIL import Image, ImageTk


def get_fuzzy_panel(root):
    panel = tk.CTkScrollableFrame(master=root, fg_color="#a5bcd9", corner_radius=20,
                                  bg_color="transparent", scrollbar_button_color="blue")
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
