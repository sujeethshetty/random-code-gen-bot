Here is a simple Python program that generates a random password for the user:

```python
import random

def generate_password(length):
    characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*"
    password = ""
    for _ in range(length):
        password += random.choice(characters)
    return password

if __name__ == "__main__":
    password_length = 12
    password = generate_password(password_length)
    print(f"Your random password is: {password}")
```

This program defines a function `generate_password` that takes a length parameter and generates a random password of that length using a combination of lowercase and uppercase letters, numbers, and special characters. The program then calls this function with a default password