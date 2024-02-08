import os
import sys
from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image

def create_image(file_path: str, width: int, height: int) -> ImageTk.PhotoImage:
    image = Image.open(file_path).resize((width, height))
    return ImageTk.PhotoImage(image)

class MyCarousel:
    def __init__(self, root, monitor_width, monitor_height) -> None:
        self.root = root
        self.counter = 0
        self.monitor_width = monitor_width
        self.monitor_height = monitor_height
        self.update_images(self.monitor_width, self.monitor_height)
        self.imageLabel = ttk.Label(self.root, image=self.image_list[0], anchor="center")
        self.imageLabel.grid(row=0, column=0, sticky="NWSE")
        self.change_image()

    def update_images(self, width, height):
        self.image_list = [create_image(f"media/{f}", width, height)
                            for f 
                            in os.listdir("media") 
                            if os.path.isfile(f"media/{f}") 
                            and f.endswith(".jpg") 
                            or f.endswith(".jpeg") 
                            or f.endswith(".png")]

    def change_image(self):
        self.counter += 1
        if self.counter >= len(self.image_list):
            self.counter = 0
        self.imageLabel["image"] = self.image_list[self.counter]
        self.root.after(5_000, self.change_image)

root = Tk()

if len(sys.argv) > 1 and sys.argv[1] == "debug":
    root.attributes('-fullscreen', False)
    monitor_width, monitor_height = 960, 540
else:
    root.attributes('-fullscreen', True)
    try:
        monitor_width, monitor_height = int(sys.argv[1]), int(sys.argv[2])
    except:
        monitor_width, monitor_height = 1920, 1080

root.geometry(f"{monitor_width}x{monitor_height}")
root.rowconfigure(0, weight=1)
root.columnconfigure(0, weight=1)
carousel = MyCarousel(root, monitor_width, monitor_height)

# run the main loop
root.mainloop()