import sys
from tkinter import Tk
from carousel import MyCarousel

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