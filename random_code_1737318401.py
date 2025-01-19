Here is a simple Python program that generates a random password for the user:

```python
import random

def generate_password(length):
    characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*"
    password = ""
    
    for _ in range(length):
        password += random.choice(characters)
    
    return password

# Main program
password_length = 12
random_password = generate_password(password_length)

print(f"Randomly generated password of length {password_length}: {random_password}")
```

In this program, we define a function `generate_password` that takes a length as an argument and generates a random password of that length using a set of characters. We then call this function to generate a random password of length