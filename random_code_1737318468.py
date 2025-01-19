Here is a simple Python program that generates a random password of a specified length:

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

This program first defines a function `generate_password(length)` that takes a parameter `length` specifying the length of the password to generate. It then generates a random password using a