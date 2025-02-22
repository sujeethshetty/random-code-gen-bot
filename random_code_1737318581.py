Sure! Here is a simple Python program that generates a random password based on user input for the length of the password:

```python
import random
import string

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for i in range(length))
    return password

def main():
    print("Welcome to the Random Password Generator!")
    length = int(input("Enter the length of the password you want to generate: "))
    
    if length < 8:
        print("Password length should be at least 8 characters.")
    else:
        password = generate_password(length)
        print("Your random password is: ", password)

if __name__