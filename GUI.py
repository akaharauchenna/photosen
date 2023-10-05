import tkinter as tk
from tkinter import filedialog

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

def get_slider_value(slider, root):
    # Get the current value of the slider
    global val
    
    value = slider.get()

    # Print the value
    val = int(value)

    # Close GUI
    root.destroy()

def get_val():
    return val

def create_slider():
    # Create a root window
    root = tk.Tk()

    # Create a slider (also known as a scale in tkinter)
    slider = tk.Scale(root, from_=0, to=100, orient=tk.HORIZONTAL)

    # Create a button that prints the current value of the slider when clicked
    button = tk.Button(root, text="Set Value", command=lambda: get_slider_value(slider, root))

    # Pack the slider and the button
    slider.pack()
    button.pack()

    # Start the main loop
    root.mainloop()
