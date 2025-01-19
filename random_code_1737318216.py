Here is a simple Python program that generates a random password:

```python
import random
import string

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for i in range(length))
    return password

def main():
    password_length = 12
    password = generate_password(password_length)
    print(f"Randomly generated password: {password}")

if __name__ == "__main__":
    main()
```

This program defines a function `generate_password` that takes a length as input and generates a random password consisting of letters, digits, and punctuation. The `main` function specifies the length of the password (in this case,