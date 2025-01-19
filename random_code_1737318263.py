Here is a simple Python program that generates a random password of a specified length:

```python
import random
import string

def generate_random_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    password_length = int(input("Enter the length of the password: "))
    random_password = generate_random_password(password_length)
    
    print("Randomly generated password:", random_password)

if __name__ == "__main__":
    main()
```

This program first defines a function `generate_random_password` that takes a length parameter and generates a random password using a combination of letters, digits, and punctuation