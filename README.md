# common-utils

## File compression utility
Run the script from the command line, passing the directory and output ZIP file name as parameters: 

``python compress.py path/to/your/directory compressed_files.zip``

This will compress the specified directory into the provided ZIP file name.

## Secure password manager
Simple password manager demonstrates how to securely store passwords and retrieve them when needed.

Features
Add Password: Store a new password in an encrypted format.
View Password: Retrieve and decrypt a password for a specific service.
Delete Password: Remove a stored password from the manager.

Run the script from the command line:

``python secure_password_manager.py``

Important Note
This implementation generates a key for encryption and stores it in a file named key.key. Make sure to keep this key secure, as it's needed for decrypting your passwords. For real-world applications, consider using additional security measures, such as master passwords or more advanced encryption techniques.
