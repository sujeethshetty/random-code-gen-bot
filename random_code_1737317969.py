Here is a simple Python program that generates a random password of a specified length using alphanumeric characters:

```python
import random
import string

def generate_password(length):
    characters = string.ascii_letters + string.digits
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    password_length = int(input("Enter the length of the password: "))
    if password_length <= 0:
        print("Invalid password length. Please enter a positive number.")
    else:
        password = generate_password(password_length)
        print(f"Generated Password: {password}")

if __name__ == "__main__":
    main()
```

This program defines a function `generate_password` that takes a length