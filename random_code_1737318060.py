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
        length = int(input("Enter the length of the password: "))
        if length <= 0:
            print("Please enter a positive integer for the length of the password.")
        else:
            password = generate_password(length)
            print(f"Generated password: {password}")
    except ValueError:
        print("Invalid input. Please enter a valid integer for the