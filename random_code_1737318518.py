Sure! Here's a simple Python program that generates a random password based on the user's desired length:

```python
import random

def generate_password(length):
    characters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*'
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    length = int(input("Enter the length of the password you want to generate: "))
    password = generate_password(length)
    print("Generated Password:", password)

if __name__ == "__main__":
    main()
```

This program defines a function `generate_password` that takes a length as input and generates a random password using a combination of lowercase letters, uppercase letters, numbers,