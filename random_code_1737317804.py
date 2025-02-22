Here is a simple Python program that generates a random password of a specified length:

```python
import random
import string

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    print("Welcome to the Random Password Generator!")
    length = int(input("Enter the length of the password you want to generate: "))
    
    password = generate_password(length)
    print(f"Your random password is: {password}")

if __name__ == "__main__":
    main()
```

This program defines a function `generate_password` that creates a random password by selecting characters from the combination of