Sure! Here is a simple Python program that generates a random password based on the user's preferences for length and complexity:

```python
import random
import string

def generate_password(length, include_numbers, include_symbols):
    characters = string.ascii_letters
    if include_numbers:
        characters += string.digits
    if include_symbols:
        characters += string.punctuation

    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    print("Welcome to the Random Password Generator!")
    length = int(input("Enter the length of the password: "))
    include_numbers = input("Include numbers? (y/n): ").lower() == 'y'
    include_symbols = input("Include symbols