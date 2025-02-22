Here is a simple Python program that generates a random password for the user:

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
    
    if length < 1:
        print("Invalid length. Please enter a number greater than 0.")
    else:
        password = generate_password(length)
        print(f"Your random password is: {password}")

if __name__ == "__main__":