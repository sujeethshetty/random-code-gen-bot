Here is a simple Python program that generates a random password based on user input for the length of the password:

```python
import random
import string

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for i in range(length))
    return password

def main():
    try:
        length = int(input("Enter the length of the password you want to generate: "))
        if length < 1:
            print("Please enter a valid length (greater than 0).")
        else:
            password = generate_password(length)
            print("Generated password:", password)
    except ValueError:
        print("Invalid input. Please enter a valid number