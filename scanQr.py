import cv2
from pyzbar.pyzbar import decode
from cryptography.fernet import Fernet
import tkinter as tk
from tkinter import messagebox

# Load the key
with open('secret.key', 'rb') as key_file:
    key = key_file.read()

cipher_suite = Fernet(key)

# Function to decode QR code
def decode_qr(frame):
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    decoded_objects = decode(gray)
    
    for obj in decoded_objects:
        encrypted_data = obj.data
        try:
            decrypted_data = cipher_suite.decrypt(encrypted_data).decode()
            print(f"Decrypted data: {decrypted_data}")
            
            return decrypted_data, True
        except Exception as e:
            messagebox.showinfo("iNFO", f"Error decrypting data: {e}")    
    return None, False

# Function to start the QR code scanning process
def start_scanning(entries):
    cap = cv2.VideoCapture(0)
    detected = False

    while not detected:
        ret, frame = cap.read()
        if not ret:
            break

        data, detected = decode_qr(frame)
        if detected:
            print(f"QR code detected and camera closing...")
            fill_entries(entries,data)
            break

        cv2.imshow('QR Code Scanner', frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

# Function to fill Tkinter entry fields with decrypted data
def fill_entries(entries,data):
    entry_1, entry_2 , entry_3 = entries
    nom, prenom, cnie = data.split(', ')
    entry_1.insert(0, nom)
    entry_2.insert(0, prenom)
    entry_3.insert(0, cnie)


