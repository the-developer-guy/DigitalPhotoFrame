import os
from tkinter import ttk
from PIL import ImageTk, Image


def create_image(file_path: str,
                 width: int, height: int) -> ImageTk.PhotoImage:
    image = Image.open(file_path).resize((width, height))
    return ImageTk.PhotoImage(image)


def is_media_file(file_path: str) -> bool:
    supported_types = [".jpg", ".jpeg", ".png"]
    if os.path.isfile(file_path):
        for supported_type in supported_types:
            if file_path.endswith(supported_type) is True:
                return True
    return False


class MyCarousel:
    def __init__(self, root, monitor_width, monitor_height) -> None:
        self.root = root
        self.counter = 0
        self.monitor_width = monitor_width
        self.monitor_height = monitor_height
        self.update_images(self.monitor_width, self.monitor_height)
        self.imageLabel = ttk.Label(self.root,
                                    image=self.image_list[0],
                                    anchor="center")
        self.imageLabel.grid(row=0, column=0, sticky="NWSE")
        self.change_image()

    def update_images(self, width, height):

        self.image_list = [create_image(f"media/{f}", width, height)
                           for f
                           in os.listdir("media")
                           if is_media_file(f"media/{f}")]

    def change_image(self):
        self.counter += 1
        if self.counter >= len(self.image_list):
            self.counter = 0
        self.imageLabel["image"] = self.image_list[self.counter]
        self.root.after(5_000, self.change_image)
