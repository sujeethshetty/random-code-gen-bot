Here's a simple Python program that generates a random password:

```python
import random

def generate_password(length):
    characters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*'
    password = ''
    for _ in range(length):
        password += random.choice(characters)
    return password

password_length = 10
generated_password = generate_password(password_length)

print(f'Generated Password: {generated_password}')
```

This program defines a function `generate_password` that takes a length parameter and generates a random password of that length using a combination of letters, numbers, and special characters. It then generates a password of length 10 and prints it to the console.