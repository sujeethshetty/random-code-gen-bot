Sure! Here's a simple Python program that generates a random password of a specified length:

```python
import random
import string

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for i in range(length))
    return password

# Get user input for password length
try:
    length = int(input("Enter the length of the password: "))
    if length <= 0:
        raise ValueError("Length must be a positive integer")
except ValueError as e:
    print(f"Error: {e}")
else:
    password = generate_password(length)
    print(f"Generated password: {password}")
```

This program defines a function `