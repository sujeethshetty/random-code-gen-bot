Here is a simple Python program that generates a random password of a specified length using uppercase letters, lowercase letters, and digits:

```python
import random
import string

def generate_password(length):
    characters = string.ascii_letters + string.digits
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    length = int(input("Enter the length of the password: "))
    if length < 1:
        print("Password length must be at least 1")
        return

    password = generate_password(length)
    print(f"Randomly generated password: {password}")

if __name__ == "__main__":
    main()
```

This program has a `generate_password` function