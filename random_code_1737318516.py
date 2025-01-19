Here's a simple Python program that generates a random password with a specified length:

```python
import random
import string

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for i in range(length))
    return password

def main():
    length = int(input("Enter the length of the password: "))
    password = generate_password(length)
    print(f"Generated password: {password}")

if __name__ == "__main__":
    main()
```

This program defines a function `generate_password` that takes a length parameter and generates a random password consisting of letters (both uppercase and lowercase), digits, and punctuation marks. The `main`