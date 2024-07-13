# QR-Code Attendance Checker & Decoder

This project allows you to generate encrypted QR codes from an Excel file containing user data, and then scan and decode these QR codes to automatically fill out user details in a Tkinter interface.

## Features

- Generate QR codes from an Excel file containing user data (`nom`, `prenom`, `cnie`).
- Encrypt QR codes using a private key.
- Scan QR codes using a webcam.
- Automatically fill out user details in a Tkinter interface after decoding the QR code.

## Setup

### Prerequisites

Ensure you have Python installed. You will also need the following Python packages:

- `pandas`
- `qrcode`
- `cryptography`
- `openpyxl`
- `tkinter`
- `opencv-python`
- `pyzbar`

You can install the required packages using pip:

```bash
pip install pandas qrcode cryptography openpyxl tkinter opencv-python pyzbar
