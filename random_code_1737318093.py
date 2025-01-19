Here's a simple Python program that generates a random password based on the user's input for the length of the password:

```python
import random
import string

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    try:
        length = int(input("Enter the length of the password you want to generate: "))
        if length <= 0:
            print("Please enter a positive number for the password length.")
        else:
            password = generate_password(length)
            print(f"Your random password of length {length} is: {password}")
    except ValueError:
        print