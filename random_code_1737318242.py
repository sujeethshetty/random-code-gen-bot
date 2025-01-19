Here's a simple Python program that generates a random password of a specified length:

```python
import random

def generate_password(length):
    characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*"
    password = ""
    
    for _ in range(length):
        password += random.choice(characters)
        
    return password

password_length = int(input("Enter the length of the password: "))
generated_password = generate_password(password_length)

print(f"Your random password is: {generated_password}")
```

This program defines a function `generate_password` that takes a length parameter and generates a random password using a combination of letters, numbers, and special characters. The user can input the desired length of the password, and the program