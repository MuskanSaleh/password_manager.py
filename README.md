🔐 Password Manager

A simple Password Manager built with Python using the cryptography library to securely store and retrieve passwords. This project encrypts passwords before saving them and decrypts them when viewed.

🚀 Features

✅ Encrypts passwords before storing them

✅ Secure key-based encryption using Fernet (AES-128)

✅ View stored passwords in decrypted format

✅ User-friendly command-line interface

✅ Handles missing files and errors gracefully

📌 How It Works

First-time setup: Generates a secret key (key.key).

Adding passwords: Encrypts and stores them in passwords.txt.

Viewing passwords: Decrypts and displays them.

Secure storage: Only accessible with the correct encryption key.

🛠 Technologies Used

Python 3.13

cryptography module (Fernet encryption)

File handling (passwords.txt for storage)
