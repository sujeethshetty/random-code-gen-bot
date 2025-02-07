Certainly! Here's a simple Python program that generates a random password of a specified length:

```python
import random
import string

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    length = int(input("Enter the length of the password: "))
    
    if length <= 0:
        print("Length should be a positive integer.")
    else:
        password = generate_password(length)
        print("Generated password:", password)

if __name__ == "__main__":
    main()
```

This program defines a function `generate_password` that creates a random password using a combination