Here is a simple Python program that generates a random password of a specified length:

```python
import random
import string

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for i in range(length))
    return password

def main():
    password_length = int(input("Enter the length of the password: "))
    password = generate_password(password_length)
    print("Generated Password:", password)

if __name__ == "__main__":
    main()
```

This program first defines a function `generate_password(length)` that generates a random password of the specified length by combining uppercase and lowercase letters, digits, and punctuation characters. The `main()` function