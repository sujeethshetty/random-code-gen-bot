Sure! Here's a simple Python program that generates a random password based on user input for the length of the password:

```python
import random
import string

def generate_random_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    print("Welcome to the Random Password Generator!")
    length = int(input("Enter the length of the password you want to generate: "))

    if length <= 0:
        print("Length should be greater than 0. Please try again.")
    else:
        password = generate_random_password(length)
        print("Your random password is: ", password)