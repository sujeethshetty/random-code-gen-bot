Here is a simple Python program that generates a random password based on user input for the length of the password:

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
    
    if length <= 0:
        print("Length should be a positive integer.")
        return
    
    password = generate_password(length)
    
    print("Your randomly generated password is:", password)

if __name__ == "__main__":