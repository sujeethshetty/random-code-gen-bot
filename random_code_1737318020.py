Here's a simple Python program that generates a random password of a specified length using uppercase letters, lowercase letters, and digits:

```python
import random
import string

def generate_password(length):
    characters = string.ascii_letters + string.digits
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    password_length = int(input("Enter the length of the password: "))
    password = generate_password(password_length)
    print("Your random password is:", password)

if __name__ == "__main__":
    main()
```

This program defines a function `generate_password` that creates a random password of a specified length by selecting characters randomly from uppercase letters, lowercase letters, and digits