Here is a simple Python program that generates and prints a random password of a specified length:

```python
import random
import string

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for i in range(length))
    return password

def main():
    password_length = int(input("Enter the length of the password: "))
    password = generate_password(password_length)
    print("Generated Password:", password)

if __name__ == "__main__":
    main()
```

This program defines two functions - `generate_password` that generates a random password based on the specified length and `main` that takes user input for the password length and then prints the