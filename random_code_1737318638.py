Here is a simple Python program that generates and prints a random password:

```python
import random
import string

def generate_password(length=8):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    password_length = int(input("Enter the length of the password you want to generate: "))
    password = generate_password(password_length)
    
    print("Generated Password:", password)

if __name__ == "__main__":
    main()
```

This program defines a function `generate_password` that creates a random password of a specified length. The main function takes user input for the desired password length and then generates