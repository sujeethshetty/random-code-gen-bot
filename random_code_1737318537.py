Here is a simple Python program that generates a random password with a specified length using lowercase letters and numbers:

```python
import random
import string

def generate_password(length):
    characters = string.ascii_lowercase + string.digits
    password = ''.join(random.choice(characters) for i in range(length))
    return password

def main():
    length = int(input("Enter the length of the password: "))
    password = generate_password(length)
    print("Your random password is:", password)

if __name__ == "__main__":
    main()
```

This program defines a function `generate_password` that takes a parameter `length` and generates a random password of that length using lowercase letters and numbers. The `main` function prompts the