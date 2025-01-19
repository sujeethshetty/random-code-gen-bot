Here's a simple Python program that generates a random password of a specified length using uppercase letters, lowercase letters, and digits:

```python
import random
import string

def generate_random_password(length):
    characters = string.ascii_letters + string.digits
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    password_length = 8
    password = generate_random_password(password_length)
    
    print(f"Your random password is: {password}")

if __name__ == "__main__":
    main()
```

In this program:
- The `generate_random_password` function creates a random password of the specified length using uppercase letters, lowercase letters, and digits.
- The `main