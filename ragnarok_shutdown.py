import sys
import os
from PIL import Image, ImageTk
import tkinter as tk
from tkinter import messagebox


def resource_path(relative_path):
    """
    Get absolute path to resource, works for dev and for PyInstaller
    """
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)


def create_radiobutton_with_image(frame, image_path, text, value):
    rb_image = None
    if image_path:
        full_path = resource_path(
            image_path
        )
        img = Image.open(full_path)
        img = img.resize((50, 50), Image.Resampling.LANCZOS)
        rb_image = ImageTk.PhotoImage(img)
        images.append(rb_image)

    radiobutton = tk.Radiobutton(
        frame,
        image=rb_image,
        variable=candy_var,
        value=value,
        compound="left",
        text=text,
    )
    radiobutton.pack(anchor="w")


def shutdown(minutes, multiplier):
    seconds = int(minutes) * 60 // multiplier
    os.system(f"shutdown -s -f -t {seconds}")


def cancel_shutdown():
    os.system("shutdown -a")
    messagebox.showinfo(
        "Shutdown Cancelled", "The scheduled shutdown has been cancelled."
    )


def on_submit():
    try:
        minutes = int(minutes_entry.get())
        if minutes < 3:
            messagebox.showwarning(
                "Warning", "Please enter a value of 3 minutes or more."
            )
            return
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid number.")
        return

    multiplier = candy_var.get()
    shutdown(minutes, multiplier)
    messagebox.showinfo(
        "Shutdown Scheduled",
        f"Your computer will shutdown in {int(minutes) // multiplier} minutes.",
    )


root = tk.Tk()
root.title("Shutdown Timer")

minutes_label = tk.Label(
    root, text="Enter the shutdown time in minutes (3 minutes or more):"
)
minutes_label.pack()

minutes_entry = tk.Entry(root)
minutes_entry.pack()

candy_var = tk.IntVar(value=1)

images = []

options_frame = tk.Frame(root)
options_frame.pack()

tk.Radiobutton(options_frame, text="No candy", variable=candy_var, value=1).pack(
    anchor="w"
)

create_radiobutton_with_image(
    options_frame, "assets/resized_blue_candy.png", "Blue candy (2x)", 2
)
create_radiobutton_with_image(
    options_frame, "assets/resized_purple_candy.png", "Purple candy (3x)", 3
)
create_radiobutton_with_image(
    options_frame, "assets/resized_orange_candy.png", "Orange candy (6x)", 6
)

submit_button = tk.Button(root, text="Submit", command=on_submit)
submit_button.pack()

cancel_button = tk.Button(root, text="Cancel Shutdown", command=cancel_shutdown)
cancel_button.pack()

created_by_label = tk.Label(root, text="Created by CuTGuArDiAn")
created_by_label.pack()

root.mainloop()
