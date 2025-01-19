Here's a simple Python program that generates a random password of a specified length:

```python
import random

def generate_password(length):
    characters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*'
    password = ''
    for _ in range(length):
        password += random.choice(characters)
    return password

if __name__ == "__main__":
    password_length = 8
    random_password = generate_password(password_length)
    print(f"Randomly generated password of length {password_length}: {random_password}")
```

This program defines a function `generate_password` that takes a parameter `length` specifying the length of the password to generate. It then generates a random password using a combination of lowercase letters, uppercase