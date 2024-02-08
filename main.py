import os
from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image

class MyCarousel:
    def __init__(self, root) -> None:
        self.root = root
        self.counter = 0
        self.update_images()
        self.imageLabel = ttk.Label(self.root, image=self.image_list[0], anchor="center")
        self.imageLabel.grid(row=0, column=0, sticky="NWSE")
        self.change_image()

    def update_images(self):
        self.image_list = [ImageTk.PhotoImage(Image.open(f"media/{f}").resize((1280, 720))) for f 
              in os.listdir("media") if os.path.isfile(f"media/{f}") 
                and f.endswith(".jpg") or f.endswith(".jpeg") or f.endswith(".png")]

    def change_image(self):
        self.counter += 1
        if self.counter >= len(self.image_list):
            self.counter = 0
        self.imageLabel["image"] = self.image_list[self.counter]
        self.root.after(5_000, self.change_image)

root = Tk()
root.attributes('-fullscreen', True)
root.geometry("1280x720")
root.rowconfigure(0, weight=1)
root.columnconfigure(0, weight=1)
carousel = MyCarousel(root)

# run the main loop
root.mainloop()