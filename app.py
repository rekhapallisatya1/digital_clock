import tkinter as tk
import time

root = tk.Tk()
root.title("Digital Clock")

def display_livetime():
    livetime = time.strftime("%H:%M:%S")
    label.config(text=livetime)
    label.after(1000, display_livetime)

label = tk.Label(root, font=("Arial", 50), bg="black", fg="white")
label.pack()

display_livetime()
root.mainloop()
