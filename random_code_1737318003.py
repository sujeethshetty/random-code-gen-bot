Here is a simple Python program that generates a random password with a specified length using uppercase letters, lowercase letters, and digits:

```python
import random
import string

def generate_password(length):
    characters = string.ascii_letters + string.digits
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    password_length = 10
    password = generate_password(password_length)
    
    print("Randomly generated password:", password)

if __name__ == "__main__":
    main()
```

This program defines a function `generate_password` that takes a parameter `length` specifying the desired length of the password. The function generates a random password by choosing characters from uppercase letters, lowercase