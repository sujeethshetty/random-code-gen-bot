Here's a simple Python program that generates a random password of a specified length:

```python
import random
import string

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for i in range(length))
    return password

if __name__ == "__main__":
    password_length = 12
    password = generate_password(password_length)
    print(f"Randomly generated password with length {password_length}: {password}")
```

This program defines a function `generate_password` that takes the length of the password as an argument and generates a random password using a combination of letters, digits, and punctuation characters. The `random.choice` function is