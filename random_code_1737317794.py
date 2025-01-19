Here's a simple Python program that generates a random password of a specified length:

```python
import random
import string

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for i in range(length))
    return password

if __name__ == '__main__':
    password_length = 12
    generated_password = generate_password(password_length)
    print(f"Your random password of length {password_length} is: {generated_password}")
```

This program defines a function `generate_password` that takes a length parameter and creates a random password of that length using a combination of letters, digits, and punctuation. The main block of the program generates