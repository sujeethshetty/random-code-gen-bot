Sure! Here's a simple Python program that generates a random password based on user-specified length:

```python
import random
import string

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for i in range(length))
    return password

def main():
    length = int(input("Enter the length of the password: "))
    if length <= 0:
        print("Password length should be greater than 0.")
    else:
        password = generate_password(length)
        print(f"Generated password: {password}")

if __name__ == "__main__":
    main()
```

This program defines a function `generate_password` that takes a