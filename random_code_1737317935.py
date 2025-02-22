Here's a simple Python program that generates a random password of a specified length:

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
    print("Your random password is:", password)

if __name__ == "__main__":
    main()
```

This program defines a `generate_password` function that takes a length parameter and generates a random password consisting of letters, digits, and punctuation marks. The `main