Sure! Here's a simple Python program that generates a random password of a specified length:

```python
import random
import string

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    length = int(input("Enter the length of the password: "))
    password = generate_password(length)
    print("Generated Password:", password)

if __name__ == "__main__":
    main()
```

In this program:
- We import the `random` and `string` modules to help generate a random password.
- The `generate_password` function generates a password of the specified length using