import qrcode
from qrcode.constants import ERROR_CORRECT_H
import tkinter as tk
from tkinter import ttk, messagebox
from tkinter import PhotoImage
import os


def generate_qr():
    """Handles QR creation when the button is pressed."""
    user_data = data_entry.get().strip()

    if not user_data:
        messagebox.showerror("Error", "Please enter some data (URL / text / UPI / WhatsApp).")
        return

    file_name = "generated_qr.png"

    # QR Configuration
    qr = qrcode.QRCode(
        version=1,                 # 1–40
        error_correction=ERROR_CORRECT_H,
        box_size=10,
        border=4,
    )

    qr.add_data(user_data)
    qr.make(fit=True)

    # Generate QR Image
    img = qr.make_image(fill_color="black", back_color="white")
    img.save(file_name)

    messagebox.showinfo("Success", f"QR generated successfully as: {file_name}")

    # -------- DISPLAY QR IN GUI WITHOUT PIL -------- #
    # Tkinter can read PNG directly using PhotoImage.
    if os.path.exists(file_name):
        qr_display_img = PhotoImage(file=file_name)
        qr_label.config(image=qr_display_img)
        qr_label.image = qr_display_img   # prevent garbage collection


# ---------------- GUI SETUP ---------------- #

root = tk.Tk()
root.title("Dynamic QR Code Generator")
root.geometry("800x850")
root.resizable(False, False)

title = ttk.Label(root, text="QR Code Generator", font=("Arial", 18, "bold"))
title.pack(pady=20)

label = ttk.Label(root, text="Enter URL / Text / UPI / WhatsApp:")
label.pack()

data_entry = ttk.Entry(root, width=50)
data_entry.pack(pady=10)

generate_btn = ttk.Button(root, text="Generate QR", command=generate_qr)
generate_btn.pack(pady=15)

qr_label = ttk.Label(root)
qr_label.pack(pady=20)

root.mainloop()
