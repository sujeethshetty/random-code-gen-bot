Here is a simple Python program that generates a random password of a specified length:

```python
import random
import string

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

if __name__ == "__main__":
    password_length = int(input("Enter the length of the password: "))
    generated_password = generate_password(password_length)
    
    print("Generated Password: ", generated_password)
```

This program defines a function `generate_password` that takes a length parameter and generates a random password containing a mix of uppercase letters, lowercase letters, digits, and special characters. The program then prompts the