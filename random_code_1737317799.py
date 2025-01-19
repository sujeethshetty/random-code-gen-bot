Here is a simple Python program that generates a random password of a specified length using uppercase letters, lowercase letters, and digits:

```python
import random

def generate_password(length):
    characters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789'
    password = ''
    for _ in range(length):
        password += random.choice(characters)
    return password

password_length = 12
random_password = generate_password(password_length)

print(f"Randomly generated password of length {password_length}: {random_password}")
```

This program defines a `generate_password` function that takes a length parameter and generates a random password of the specified length using a combination of uppercase letters, lowercase letters, and digits. The `random.choice` function is used to select a