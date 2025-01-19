Here's a simple Python program that generates a random password of a specified length using a combination of uppercase letters, lowercase letters, and digits:

```python
import random

def generate_password(length):
    characters = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789"
    password = ""
    for _ in range(length):
        password += random.choice(characters)
    return password

# Get user input for password length
password_length = int(input("Enter the length of the password: "))

# Generate and display the random password
password = generate_password(password_length)
print("Your random password is:", password)
```

This program defines a function `generate_password` that creates a random password of the specified length by randomly selecting characters from a predefined set of uppercase