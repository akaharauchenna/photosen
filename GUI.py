import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox

def create_root():
    # Create a root window and hide it
    root = tk.Tk()
    return root

def select_video_file(root):
    # Open a file selection dialog and get the path of the selected file
    video_path = filedialog.askopenfilename()
    return video_path

def show_warning_message(root):
    # Show a message box
    messagebox.showinfo("Warning!", "This video may contain Flashing and/or camera movement, and could trigger symptoms in users with Photosensitivity Issues!")

def show_ok_message(root):
    # Show a message box
    messagebox.showinfo("Okay!", "Looks like this video is safe to view.")

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

def create_slider(root):
    # Create a slider (also known as a scale in tkinter)
    slider = tk.Scale(root, from_=0, to=100, orient=tk.HORIZONTAL)

    # Create a button that prints the current value of the slider when clicked
    button = tk.Button(root, text="Set Value", command=lambda: get_slider_value(slider, root))

    # Pack the slider and the button
    slider.pack()
    button.pack()

    # Start the main loop
    # root.mainloop()
    return root

