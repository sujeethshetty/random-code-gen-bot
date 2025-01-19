Here's a simple Python program that generates a random password of a specified length using lowercase letters and digits:

```python
import random
import string

def generate_password(length):
    characters = string.ascii_lowercase + string.digits
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    password_length = int(input("Enter the length of the password: "))
    
    if password_length <= 0:
        print("Password length should be a positive integer.")
    else:
        password = generate_password(password_length)
        print("Your random password is:", password)

if __name__ == "__main__":
    main()
```

This program defines a `generate_password` function that creates a