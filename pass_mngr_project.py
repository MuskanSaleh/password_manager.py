from cryptography.fernet import Fernet
import os

# Function to generate and save the key
def write_key():
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)

# Function to load the existing key
def load_key():
    if not os.path.exists("key.key"):
        print("Key file not found! Generating a new one...")
        write_key()
    with open("key.key", "rb") as key_file:
        return key_file.read()

# Load the encryption key
key1 = load_key()
fer = Fernet(key1)

# Function to view stored passwords
def view():
    if not os.path.exists("passwords.txt") or os.stat("passwords.txt").st_size == 0:
        print("No passwords stored yet.")
        return

    with open('passwords.txt', 'r') as f:
        for line in f.readlines():
            if "|" not in data:
                continue  # Skip invalid lines
            user, passw = data.split("|")
            try:
                decrypted_password = fer.decrypt(passw.encode()).decode()
                print(f"User: {user} | Password: {decrypted_password}")
            except:
                print(f"Error decrypting password for {user}")

# Function to add new passwords
def add():
    name = input("Account Name: ")
    pwd = input("Password: ")
    with open('passwords.txt', 'a') as f:
        f.write(name + "|" + fer.encrypt(pwd.encode()).decode() + "\n")
    print("Password added successfully!")

# Main loop for user interaction
while True:
    mode = input("Would you like to add a new password, view, or quit (q)? ").lower()
    if mode == "q":
        print("Exiting password manager. Goodbye!")
        break
    elif mode == "add":
        add()
    elif mode == "view":
        view()
    else:
        print("Invalid mode. Please enter 'add', 'view', or 'q'.")
