Here is a simple Python program that generates a random password based on the user's choice of length:

```python
import random
import string

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for i in range(length))
    return password

def main():
    print("Welcome to the Random Password Generator!")
    
    try:
        length = int(input("Enter the length of the password you want to generate: "))
        if length <= 0:
            print("Please enter a positive integer for the length.")
            return
    except ValueError:
        print("Invalid input. Please enter a valid integer for the length.")
        return

    password