Here's a simple Python program that generates a random password for the user:

```python
import random
import string

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for i in range(length))
    return password

def main():
    print("Welcome to the Random Password Generator!")
    
    while True:
        try:
            password_length = int(input("Enter the length of the password you want to generate: "))
            if password_length <= 0:
                print("Please enter a positive integer for the password length.")
            else:
                break
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

    password =