Certainly! Here's a simple Python program that generates a random password:

```python
import random

def generate_password(length):
    characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()"
    password = ""
    
    for _ in range(length):
        password += random.choice(characters)
    
    return password

password_length = 12
random_password = generate_password(password_length)

print(f"Generated Password: {random_password}")
```

In this program, we have a function `generate_password` that takes a parameter `length` to determine the length of the password. The function creates a random password using a combination of lowercase letters, uppercase letters, numbers, and special characters. The generated password is then printed to the