Here is a simple Python program that generates a random password of a specified length using uppercase letters, lowercase letters, and numbers:

```python
import random
import string

def generate_password(length):
    characters = string.ascii_letters + string.digits
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    try:
        length = int(input("Enter the length of the password you want to generate: "))
        if length <= 0:
            print("Please enter a positive length.")
        else:
            password = generate_password(length)
            print("Your random password is:", password)
    except ValueError:
        print("Invalid input. Please enter a valid number.")

if __name__