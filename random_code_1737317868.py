Here's a simple Python program that generates a random password based on the user's preferences:

```python
import random
import string

def generate_password(length, include_numbers=False, include_symbols=False):
    characters = string.ascii_letters
    if include_numbers:
        characters += string.digits
    if include_symbols:
        characters += string.punctuation
    
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    print("Random Password Generator\n")
    
    length = int(input("Enter the length of the password: "))
    include_numbers = input("Include numbers? (y/n): ").lower() == 'y'
    include_symbols = input("Include symbols? (y/n):