Here is a simple Python program that generates a random password of a specified length:

```python
import random

def generate_password(length):
    characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*"
    password = ""
    for _ in range(length):
        password += random.choice(characters)
    return password

password_length = 12
random_password = generate_password(password_length)

print(f"Randomly generated password of length {password_length}: {random_password}")
```

This program defines a function `generate_password` that takes a length parameter and generates a random password using a combination of letters, numbers, and special characters. The program then calls this function to create a random password of length 12 and prints it to