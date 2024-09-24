# Encrypt_decrypt-code
This is a basic Python program that allows you to encrypt and decrypt files using the Fernet module from the cryptography library. Fernet is a symmetric encryption method, meaning the same key is used for both encryption and decryption.
Explanation:
Key Generation: The generate_key() function generates a random encryption key and saves it to a file called secret.key. This key is needed for both encryption and decryption.

Encryption: The encrypt_file() function reads the contents of the given file, encrypts the data using the previously generated key, and saves the encrypted data to a new file with the .encrypted extension.

Decryption: The decrypt_file() function reads the contents of the encrypted file, decrypts it using the key, and saves the decrypted data back to the original file format.

Usage:
Run the program:
Choose Option 1 to generate the encryption key.

Choose Option 2 to encrypt a file (e.g., sample.txt), which will create a new file called sample.txt.encrypted.

Choose Option 3 to decrypt an encrypted file (e.g., sample.txt.encrypted), restoring the original file contents.

Notes:
Key security: Ensure that the secret.key is kept secure. If you lose this key, you won’t be able to decrypt the files.
This program is suitable for small to medium-sized files, as it reads the entire file into memory. For larger files, you may want to process the file in chunks.
