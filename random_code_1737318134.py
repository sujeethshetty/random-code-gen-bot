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
    print("Generated password:", password)

if __name__ == "__main__":
    main()
```

This program defines a function `generate_password` that takes a length parameter and generates a random password using a combination of letters (both uppercase and lowercase), digits, and punctuation characters. The `