Here's a simple Python program that generates a random password for the user:

```python
import random
import string

def generate_password(length=8):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for i in range(length))
    return password

def main():
    print("Welcome to the Random Password Generator!")
    password_length = int(input("Enter the length of the password you want to generate: "))
    
    if password_length < 1:
        print("Password length should be at least 1.")
    else:
        password = generate_password(password_length)
        print(f"Your random password is: {password}")

if __name__ == "__main__":