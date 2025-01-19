Sure! Here's a simple Python program that generates a random password of a specified length using alphanumeric characters:

```python
import random
import string

def generate_password(length):
    characters = string.ascii_letters + string.digits
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
- We import the `random` and `string` modules to use their functions for generating random characters.
- The `generate_password` function takes a length parameter and generates a