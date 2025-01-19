Sure! Here's a simple Python program that generates a random password of a specified length:

```python
import random
import string

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for i in range(length))
    return password

def main():
    length = int(input("Enter the length of the password you want to generate: "))
    
    password = generate_password(length)
    print("Generated Password:", password)

if __name__ == "__main__":
    main()
```

This program prompts the user to input the desired length of the password, then generates a random password consisting of uppercase letters, lowercase letters, digits, and special characters.