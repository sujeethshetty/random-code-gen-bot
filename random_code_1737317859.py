Sure! Here's a simple Python program that generates a random password for the user:

```python
import random
import string

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for i in range(length))
    return password

def main():
    print("Welcome to the Random Password Generator!")
    length = int(input("Enter the length of the password you'd like to generate: "))

    if length <= 0:
        print("Invalid length. Please enter a positive number.")
    else:
        password = generate_password(length)
        print("\nYour randomly generated password is:", password)

if __name__ == "__main__":
    main