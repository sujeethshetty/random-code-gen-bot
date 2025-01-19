Here's a simple Python program that generates a random password based on user input for the desired length:

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
            length = int(input("Enter the desired length of the password: "))
            if length <= 0:
                print("Please enter a positive number.")
            else:
                password = generate_password(length)
                print(f"Your random password is: {password}")
                break
        except ValueError: