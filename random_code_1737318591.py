Certainly! Here's a simple Python program that generates a random password of a specified length using uppercase letters, lowercase letters, and numbers:

```python
import random
import string

def generate_password(length):
    characters = string.ascii_letters + string.digits
    password = ''.join(random.choice(characters) for i in range(length))
    return password

def main():
    print("Welcome to Random Password Generator!")
    length = int(input("Enter the length of the password you want to generate: "))
    
    if length <= 0:
        print("Length should be a positive integer.")
    else:
        password = generate_password(length)
        print("Your random password is:", password)

if __name__ == "__main__":
    main