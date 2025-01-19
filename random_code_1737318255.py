Here is a simple Python program that generates a random password of a specified length using lowercase letters and digits:

```python
import random
import string

def generate_password(length):
    characters = string.ascii_lowercase + string.digits
    password = ''.join(random.choice(characters) for i in range(length))
    return password

def main():
    password_length = int(input("Enter the length of the password: "))
    if password_length <= 0:
        print("Password length should be a positive integer.")
    else:
        password = generate_password(password_length)
        print(f"Generated password: {password}")

if __name__ == "__main__":
    main()
```

This program defines a function `generate_password` that takes the desired