import os
import pandas as pd
import qrcode
from cryptography.fernet import Fernet
import tkinter as tk
from tkinter import filedialog, messagebox

# Check if secret.key exists
key_file_path = 'secret.key'

output_dir = "qr_codes"
os.makedirs(output_dir,exist_ok=True)

if os.path.exists(key_file_path):
    # Load the existing key
    with open(key_file_path, 'rb') as key_file:
        key = key_file.read()
else:
    # Generate a new key
    key = Fernet.generate_key()
    with open(key_file_path, 'wb') as key_file:
        key_file.write(key)

cipher_suite = Fernet(key)

# Function to open file dialog and select Excel file
def select_file():
    root = tk.Tk()
    root.withdraw()  # Hide the root window
    file_path = filedialog.askopenfilename(
        title="Select Excel File",
        filetypes=(("Excel files", "*.xlsx"), ("All files", "*.*"))
    )
    return file_path

# Select the Excel file
def read_excel():
    excel_file_path = select_file()

    # Read the selected Excel file
    df = pd.read_excel(excel_file_path)  # Ensure you have 'nom', 'prenom', 'cnie' columns

    # Generate QR codes for each row in the Excel file
    for index, row in df.iterrows():
        data = f"{row['nom']}, {row['prenom']}, {row['cnie']}"
        encrypted_data = cipher_suite.encrypt(data.encode())
        
        # Generate QR code
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )
        qr.add_data(encrypted_data)
        qr.make(fit=True)

        img = qr.make_image(fill='black', back_color='white')
        
        output_file = os.path.join(output_dir,f"qr_{row['nom']}_{row['prenom']}_{row['cnie']}.png")
        img.save(output_file)

    messagebox.showinfo("Success", "QR codes generated and encrypted successfully!")
    
def clearAll(entries):
    for entry in entries:
        entry.delete(0, 'end')
    
