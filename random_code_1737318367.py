Here's a simple Python program that generates a random password of a specified length:

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
    print("Randomly generated password:", password)

if __name__ == "__main__":
    main()
```

In this program:
- The `generate_password` function creates a random password of the specified length using a combination of letters, digits, and punctuation characters.
- The `main` function takes