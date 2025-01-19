Here's a simple Python program that generates a random password of a specified length:

```python
import random

def generate_random_password(length):
    characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*"
    password = ""
    
    for _ in range(length):
        password += random.choice(characters)
    
    return password

password_length = int(input("Enter the length of the password you want to generate: "))
random_password = generate_random_password(password_length)

print("Your random password is:", random_password)
```

This program defines a function `generate_random_password` that takes a length parameter and generates a random password of that length using a mix of lowercase letters, uppercase letters, numbers, and special characters. The user