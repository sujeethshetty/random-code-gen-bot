Here's a simple Python program that generates a random password of a specified length:

```python
import random

def generate_password(length):
    characters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*'
    password = ''
    for _ in range(length):
        password += random.choice(characters)
    return password

password_length = int(input("Enter the length of the password: "))
random_password = generate_password(password_length)

print("Generated Password:", random_password)
```

This program defines a function called `generate_password` that takes a length parameter and generates a random password using a combination of lowercase letters, uppercase letters, numbers, and special characters. The program then prompts the user to enter the desired length of the password and