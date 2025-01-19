Here is a simple Python program that generates a random password for the user based on their desired length:

```python
import random
import string

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for i in range(length))
    return password

def main():
    print("Welcome to the Random Password Generator!")
    length = int(input("Please enter the length of the password you want to generate: "))

    if length <= 0:
        print("Invalid input. Please enter a positive number.")
    else:
        password = generate_password(length)
        print("Your random password is:", password)

if __name__ == "__main__":