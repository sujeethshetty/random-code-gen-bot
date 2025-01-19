Sure! Here's a simple Python program that generates a random password for the user:

```python
import random

def generate_password(length):
    characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*"
    password = ""
    for _ in range(length):
        password += random.choice(characters)
    return password

def main():
    print("Welcome to the Random Password Generator!")
    length = int(input("Enter the length of the password you want to generate: "))
    
    if length <= 0:
        print("Please enter a valid length for the password.")
    else:
        password = generate_password(length)
        print(f"Your random password is: {password}")

if __name__ == "__main__":