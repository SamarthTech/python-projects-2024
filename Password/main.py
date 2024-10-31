from cryptography.fernet import Fernet

# Generate a key for encryption
def generate_key():
    return Fernet.generate_key()

# Save key to a file
def save_key(key, filename="key.key"):
    with open(filename, "wb") as file:
        file.write(key)

# Load the key from a file
def load_key(filename="key.key"):
    with open(filename, "rb") as file:
        return file.read()

# Encrypt a password
def encrypt_password(password, key):
    f = Fernet(key)
    return f.encrypt(password.encode())

# Decrypt a password
def decrypt_password(encrypted_password, key):
    f = Fernet(key)
    return f.decrypt(encrypted_password).decode()

# Sample usage
key = generate_key()
save_key(key)
key = load_key()

encrypted = encrypt_password("mysecretpassword", key)
print("Encrypted:", encrypted)

decrypted = decrypt_password(encrypted, key)
print("Decrypted:", decrypted)
