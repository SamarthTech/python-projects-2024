import random
import string

def generate_password(length=12, use_upper=True, use_digits=True, use_special=True):
    characters = string.ascii_lowercase
    if use_upper:
        characters += string.ascii_uppercase
    if use_digits:
        characters += string.digits
    if use_special:
        characters += string.punctuation

    password = ''.join(random.choice(characters) for _ in range(length))
    return password

print("Welcome to the Password Generator!")
length = int(input("Enter desired password length: "))
use_upper = input("Include uppercase letters? (y/n): ").lower() == 'y'
use_digits = input("Include digits? (y/n): ").lower() == 'y'
use_special = input("Include special characters? (y/n): ").lower() == 'y'

print(f"Generated Password: {generate_password(length, use_upper, use_digits, use_special)}")
