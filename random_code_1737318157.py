Here is a simple Python program that generates and prints a random password:

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
    print("Generated Password:", password)

if __name__ == "__main__":
    main()
```

This program defines a function `generate_password(length)` that creates a random password of the specified length using a combination of letters, digits, and punctuation marks. The `main()` function prompts the user to enter the