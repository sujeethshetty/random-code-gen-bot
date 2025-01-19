Here is a simple Python program that generates a random password of a specified length using uppercase letters and digits:

```python
import random

def generate_password(length):
    characters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
    password = ""
    for _ in range(length):
        password += random.choice(characters)
    return password

def main():
    password_length = int(input("Enter the length of the password: "))
    generated_password = generate_password(password_length)
    print("Your random password is:", generated_password)

if __name__ == "__main__":
    main()
```

This program defines a function `generate_password` that takes the desired length of the password as input and generates a random password using uppercase letters and digits. The `main`