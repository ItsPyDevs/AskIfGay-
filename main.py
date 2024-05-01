import tkinter as tk ; from PIL import Image, ImageTk ; from customtkinter import CTkButton ; import random, pygame, requests, os
if not os.path.exists("assets"): os.makedirs("assets")
resources = {"asset1": "https://i.ytimg.com/vi/K5CraDlqfFo/maxresdefault.jpg","asset2": "https://www.myinstants.com/media/sounds/investi-dune-grande-mission.mp3","asset3": "https://www.myinstants.com/media/sounds/anime-ahh.mp3"}
for key, url in resources.items():
    resource_path = f"assets/{key}" ; response = requests.get(url)
    if not os.path.exists(resource_path): 
        with open(resource_path, "wb") as f: f.write(response.content)

root = tk.Tk() ; root.title("Gay Meter :O") ; root.geometry("700x500") ; image_path = "assets/asset1" ; image = Image.open(image_path) ; image = ImageTk.PhotoImage(image) ; label_question = tk.Label(root, text="Tu es gay ?", font=("Arial", 36)) ; label_question.pack(pady=20)
def play_sound(sound_path): pygame.mixer.init() ; pygame.mixer.music.load(sound_path) ; pygame.mixer.music.play()
def display_message(message, sound_path): clear_interface() ; label_image = tk.Label(root, image=image) ; label_image.place(relx=0.5, rely=0.3, anchor="center") ; label_text = tk.Label(root, text=message, font=("Arial", 36)) ; label_text.place(relx=0.5, rely=0.5, anchor="center") ; play_sound(sound_path)
def clear_interface():
    for widget in root.winfo_children(): widget.destroy()
def reset_interface(): clear_interface() ; create_interface()
def create_interface():
    def teleport_no_button(event): x = random.randint(0, root.winfo_width() - no_button.winfo_width()) ; y = random.randint(0, root.winfo_height() - no_button.winfo_height()) ; no_button.place(x=x, y=y) ; play_sound("assets/asset3")
    yes_button = CTkButton(root, text="Oui", command=lambda: display_message("Je le savais", "assets/asset2")) ; yes_button.pack(pady=10) ; global no_button ; no_button = CTkButton(root, text="Non") ; no_button.pack(pady=10) ; no_button.bind("<Motion>", teleport_no_button)

create_interface() ; root.mainloop()