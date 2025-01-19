Here is a simple Python program that generates a random password of a specified length using lowercase letters and digits:

```python
import random

def generate_password(length):
    characters = 'abcdefghijklmnopqrstuvwxyz0123456789'
    password = ''
    for _ in range(length):
        password += random.choice(characters)
    return password

password_length = int(input("Enter the length of the password: "))
random_password = generate_password(password_length)

print(f"Randomly generated password: {random_password}")
```

This program defines a function `generate_password` that takes a parameter `length` and creates a random password of that length using lowercase letters and digits. The program then takes user input for the desired password length, generates the random password, and displays