from cryptography.fernet import Fernet

# Function to generate and save the encryption key
def generate_key():
    key = Fernet.generate_key()
    with open("secret.key", "wb") as key_file:
        key_file.write(key)
    print("Key generated and saved as 'secret.key'")

# Function to load the previously generated key
def load_key():
    return open("secret.key", "rb").read()

# Function to encrypt a file
def encrypt_file(filename):
    key = load_key()
    fernet = Fernet(key)
    
    with open(filename, "rb") as file:
        file_data = file.read()
    
    encrypted_data = fernet.encrypt(file_data)
    
    with open(filename + ".encrypted", "wb") as file:
        file.write(encrypted_data)
    
    print(f"File '{filename}' encrypted successfully.")

# Function to decrypt a file
def decrypt_file(encrypted_filename):
    key = load_key()
    fernet = Fernet(key)
    
    with open(encrypted_filename, "rb") as file:
        encrypted_data = file.read()
    
    decrypted_data = fernet.decrypt(encrypted_data)
    
    decrypted_filename = encrypted_filename.replace(".encrypted", "")
    with open(decrypted_filename, "wb") as file:
        file.write(decrypted_data)
    
    print(f"File '{encrypted_filename}' decrypted successfully.")

# Main program to select operation
if __name__ == "__main__":
    print("1. Generate encryption key")
    print("2. Encrypt a file")
    print("3. Decrypt a file")
    choice = input("Choose an option (1, 2, or 3): ")

    if choice == "1":
        generate_key()
    elif choice == "2":
        filename = input("Enter the filename to encrypt: ")
        encrypt_file(filename)
    elif choice == "3":
        encrypted_filename = input("Enter the encrypted filename to decrypt: ")
        decrypt_file(encrypted_filename)
    else:
        print("Invalid choice")
