Here is a simple Python program that generates a random password for the user:

```python
import random

def generate_password(length):
    characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*"
    password = ""
    for _ in range(length):
        password += random.choice(characters)
    return password

def main():
    print("Welcome to the Random Password Generator!")
    length = int(input("Enter the length of the password you want to generate: "))
    
    password = generate_password(length)
    print("Your random password is:", password)

if __name__ == "__main__":
    main()
```

This program defines a function `generate_password` that takes a length as an argument and generates a random password of