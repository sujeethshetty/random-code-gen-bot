Here is a simple Python program that generates a random password of a specific length:

```python
import random
import string

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    password_length = int(input("Enter the length of the password: "))
    password = generate_password(password_length)
    print("Your random password is:", password)

if __name__ == "__main__":
    main()
```

This program first defines a function `generate_password` that takes the desired length of the password as an argument and generates a random password using a combination of letters, digits, and punctuation