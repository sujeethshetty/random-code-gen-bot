Here is a simple Python program that generates a random password consisting of letters and numbers:

```python
import random
import string

def generate_password(length):
    characters = string.ascii_letters + string.digits
    password = ''.join(random.choice(characters) for i in range(length))
    return password

def main():
    password_length = 8
    password = generate_password(password_length)
    print("Randomly generated password:", password)

if __name__ == "__main__":
    main()
```

This program defines a `generate_password` function that takes a length parameter and generates a random password of the specified length using uppercase letters, lowercase letters, and digits. The `main` function then calls `generate_password` with a default