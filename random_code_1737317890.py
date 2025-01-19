Here is a simple Python program that generates a random password of a specified length using uppercase letters, lowercase letters, and digits. It includes functions, variables, loops, and basic Python features:

```python
import random

def generate_password(length):
    characters = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789"
    password = ""
    for _ in range(length):
        password += random.choice(characters)
    return password

def main():
    length = int(input("Enter the length of the password you want to generate: "))
    password = generate_password(length)
    print("Your random password is:", password)

if __name__ == "__main__":
    main()
```

This program prompts the user to enter the length of the password they want to generate