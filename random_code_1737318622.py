Here is a simple Python program that generates a random password for the user:

```python
import random

def generate_password(length):
    characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*"
    password = ""
    for _ in range(length):
        password += random.choice(characters)
    return password

password_length = int(input("Enter the length of the password you want to generate: "))
generated_password = generate_password(password_length)

print("Generated Password:", generated_password)
```

This program defines a function `generate_password` that takes a length parameter and generates a random password of that length using a combination of lowercase letters, uppercase letters, numbers, and special characters. The user can input the desired length of the password