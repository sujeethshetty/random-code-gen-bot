Sure! Here's a simple Python program that generates a random password with a specified length:

```python
import random
import string

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    password_length = int(input("Enter the length of the password you want to generate: "))
    password = generate_password(password_length)
    print(f"Generated password: {password}")

if __name__ == "__main__":
    main()
```

This program defines a function `generate_password(length)` that uses the `random` module to generate a random password of the specified length. The main function