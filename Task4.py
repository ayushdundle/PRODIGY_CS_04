import tkinter as tk
from tkinter import messagebox
import os
from datetime import datetime

# Documents path (Windows-safe)
documents_path = os.path.join(os.environ["USERPROFILE"], "Documents")

# Project folder
folder_path = os.path.join(documents_path, "KeyLogger_Project")
os.makedirs(folder_path, exist_ok=True)

# File path
file_path = os.path.join(folder_path, "typed_text_log.txt")

def save_text():
    text = text_box.get("1.0", tk.END).strip()

    if not text:
        messagebox.showwarning("Warning", "Please type something first!")
        return

    with open(file_path, "a", encoding="utf-8") as file:
        file.write("\n------------------------\n")
        file.write(f"Saved on: {datetime.now()}\n")
        file.write(text + "\n")

    messagebox.showinfo("Success", "Text saved successfully!")
    text_box.delete("1.0", tk.END)

def clear_saved_data():
    if not os.path.exists(file_path):
        messagebox.showinfo("Info", "No saved file found to clear.")
        return

    confirm = messagebox.askyesno(
        "Confirm Delete",
        "Are you sure you want to clear ALL saved text?\nThis cannot be undone."
    )

    if confirm:
        open(file_path, "w").close()  # clears file content
        messagebox.showinfo("Cleared", "Saved data has been cleared successfully.")

# GUI window
root = tk.Tk()
root.title("GUI Text Logger (Educational)")
root.geometry("700x460")

tk.Label(
    root,
    text="GUI Based Text Logger (Ethical & Visible)",
    font=("Arial", 15, "bold")
).pack(pady=10)

tk.Label(
    root,
    text="Type in the box below.\nYou can Save or Clear the stored data anytime.",
    font=("Arial", 11),
    justify="center"
).pack()

text_box = tk.Text(root, height=12, width=80, font=("Arial", 11))
text_box.pack(pady=10)

# Buttons frame
btn_frame = tk.Frame(root)
btn_frame.pack(pady=10)

tk.Button(
    btn_frame,
    text="Save Text",
    bg="green",
    fg="white",
    font=("Arial", 11),
    width=15,
    command=save_text
).grid(row=0, column=0, padx=10)

tk.Button(
    btn_frame,
    text="Clear Saved Data",
    bg="red",
    fg="white",
    font=("Arial", 11),
    width=18,
    command=clear_saved_data
).grid(row=0, column=1, padx=10)

tk.Label(
    root,
    text=f"File location:\n{file_path}",
    font=("Arial", 9),
    fg="blue",
    wraplength=650,
    justify="center"
).pack(pady=10)

root.mainloop()
