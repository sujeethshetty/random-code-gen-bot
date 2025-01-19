Sure! Here's a simple Python program that generates a random password of a specified length using lowercase letters and numbers:

```python
import random
import string

def generate_password(length):
    characters = string.ascii_lowercase + string.digits
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    length = int(input("Enter the length of the password: "))
    password = generate_password(length)
    print("Your random password is:", password)

if __name__ == "__main__":
    main()
```

This program defines a function `generate_password()` that takes a length parameter and generates a random password using lowercase letters and numbers. The `main()` function prompts the user to enter