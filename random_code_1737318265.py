Here's a simple Python program that generates a random password of a specified length using lowercase letters and digits:

```python
import random
import string

def generate_password(length):
    characters = string.ascii_lowercase + string.digits
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

password_length = 8
random_password = generate_password(password_length)

print(f"Randomly generated password: {random_password}")
```

In this program:
- We import the `random` and `string` modules to generate random characters and access string constants.
- We define a function `generate_password` that takes a length parameter and returns a password consisting of lowercase letters and digits of that length.
- We generate