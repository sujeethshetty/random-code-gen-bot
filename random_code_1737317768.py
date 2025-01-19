Here's a simple Python program that generates a random password of a specified length using uppercase letters, lowercase letters, and numbers:

```python
import random

def generate_password(length):
    characters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
    password = ''
    for _ in range(length):
        password += random.choice(characters)
    return password

password_length = int(input("Enter the length of the password: "))
generated_password = generate_password(password_length)

print("Generated Password:", generated_password)
```

This program defines a function `generate_password` that takes a length parameter and creates a random password of that length by choosing characters randomly from a set of uppercase letters, lowercase letters, and numbers. The user is prompted to enter the desired length