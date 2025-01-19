Here is a simple Python program that generates a random password and checks if it meets certain criteria (e.g., minimum length, containing both letters and numbers):

```python
import random
import string

def generate_random_password(length):
    characters = string.ascii_letters + string.digits
    password = ''.join(random.choice(characters) for i in range(length))
    return password

def is_valid_password(password):
    has_letter = any(char.isalpha() for char in password)
    has_number = any(char.isdigit() for char in password)
    return has_letter and has_number

password_length = 8

while True:
    password = generate_random_password(password_length)
    if is_valid_password(password):
        break

print("Random Password