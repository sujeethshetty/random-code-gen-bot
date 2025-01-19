Here's a simple Python program that generates a random password based on user-defined length:

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
            print("Length should be a positive integer.")
        else:
            password = generate_password(length)
            print(f"Generated password: {password}")
    except ValueError:
        print("Invalid input. Please enter a valid positive integer.")

if __name__ == "__