import random
import string

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

# User input
try:
    length = int(input("Enter the desired password length: "))
    if length < 1:
        print("Password length must be at least 1.")
    else:
        print("Generated Password:", generate_password(length))
except ValueError:
    print("Please enter a valid number.")
