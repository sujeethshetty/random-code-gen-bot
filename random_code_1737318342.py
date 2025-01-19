Here is a simple Python program that generates a random password:

```python
import random

def generate_password(length):
    characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*"
    password = ""
    
    for _ in range(length):
        password += random.choice(characters)
    
    return password

password_length = 8
random_password = generate_password(password_length)

print(f"Randomly generated password with length {password_length}: {random_password}")
```

This program defines a function `generate_password` that takes a length as input and generates a random password using a mix of lowercase letters, uppercase letters, numbers, and special characters. The program then calls this function to generate a random password of length 8 and