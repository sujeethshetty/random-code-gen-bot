Here is a simple Python program that generates a random password with a specified length:

```python
import random
import string

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    password_length = 12
    password = generate_password(password_length)
    print("Randomly generated password:", password)

if __name__ == "__main__":
    main()
```

This program defines a function `generate_password` that takes a length parameter and generates a random password containing uppercase and lowercase letters, digits, and special characters. The `main` function sets the password length to 12 and