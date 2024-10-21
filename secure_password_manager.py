import json
import os
from cryptography.fernet import Fernet

# Generate a key for encryption and decryption
def generate_key():
    return Fernet.generate_key()

# Load or create a key
def load_key():
    if os.path.exists('key.key'):
        with open('key.key', 'rb') as key_file:
            return key_file.read()
    else:
        key = generate_key()
        with open('key.key', 'wb') as key_file:
            key_file.write(key)
        return key

# Encrypt the password
def encrypt_password(password, key):
    fernet = Fernet(key)
    encrypted_password = fernet.encrypt(password.encode())
    return encrypted_password

# Decrypt the password
def decrypt_password(encrypted_password, key):
    fernet = Fernet(key)
    decrypted_password = fernet.decrypt(encrypted_password).decode()
    return decrypted_password

# Load passwords from a file
def load_passwords():
    if os.path.exists('passwords.json'):
        with open('passwords.json', 'r') as file:
            return json.load(file)
    return {}

# Save passwords to a file
def save_passwords(passwords):
    with open('passwords.json', 'w') as file:
        json.dump(passwords, file, indent=4)

# Add a password
def add_password(service, username, password, key):
    passwords = load_passwords()
    encrypted_password = encrypt_password(password, key)
    passwords[service] = {'username': username, 'password': encrypted_password.decode()}
    save_passwords(passwords)
    print(f'Password for {service} added successfully.')

# View a password
def view_password(service, key):
    passwords = load_passwords()
    if service in passwords:
        username = passwords[service]['username']
        encrypted_password = passwords[service]['password'].encode()
        decrypted_password = decrypt_password(encrypted_password, key)
        print(f"Service: {service}")
        print(f"Username: {username}")
        print(f"Password: {decrypted_password}")
    else:
        print(f'No password found for {service}.')

# Delete a password
def delete_password(service):
    passwords = load_passwords()
    if service in passwords:
        del passwords[service]
        save_passwords(passwords)
        print(f'Password for {service} deleted successfully.')
    else:
        print(f'No password found for {service}.')

# Main function
def main():
    key = load_key()
    while True:
        print("\nPassword Manager")
        print("1. Add Password")
        print("2. View Password")
        print("3. Delete Password")
        print("4. Exit")
        
        choice = input("Choose an option: ")
        
        if choice == '1':
            service = input("Enter the service name: ")
            username = input("Enter the username: ")
            password = input("Enter the password: ")
            add_password(service, username, password, key)
        elif choice == '2':
            service = input("Enter the service name: ")
            view_password(service, key)
        elif choice == '3':
            service = input("Enter the service name: ")
            delete_password(service)
        elif choice == '4':
            break
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()
