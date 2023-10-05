import tkinter as tk
from tkinter import filedialog
from flash_detect import detect_flashing_video
def select_video_file():
    # Create a root window and hide it
    root = tk.Tk()
    root.withdraw()

    # Open a file selection dialog and get the path of the selected file
    video_path = filedialog.askopenfilename()

    return video_path

def show_warning_message():
    # Create a root window and hide it
    root = tk.Tk()
    root.withdraw()

    # Show a message box
    tk.messagebox.showinfo("Warning!", "This video contains Flashing, and could trigger Seizures in users with Photosensitivity Issues!")

def show_ok_message():
    # Create a root window and hide it
    root = tk.Tk()
    root.withdraw()

    # Show a message box
    tk.messagebox.showinfo("Okay!", "This video is safe to watch and has no sudden change in Luminance")

video = select_video_file()

if detect_flashing_video(video):
    show_warning_message()
else:
    show_ok_message()




