Sure! Here's a simple Python program that generates a random password based on the user's preferred length:

```python
import random
import string

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    print("Welcome to the Random Password Generator!")
    length = int(input("Enter the length of the password you'd like to generate: "))
    
    if length < 6:
        print("Password length should be at least 6 characters.")
    else:
        password = generate_password(length)
        print("Your random password is:", password)

if __name__ == "__main