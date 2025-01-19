Certainly! Here's a simple Python program that generates a random password of a specified length:

```python
import random
import string

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

password_length = 12
random_password = generate_password(password_length)

print(f"Randomly generated password of length {password_length}: {random_password}")
```

This program defines a function `generate_password` that takes a length parameter and generates a random password of that length using a combination of letters (both upper and lower case), digits, and special characters. The generated password is then printed to the console.