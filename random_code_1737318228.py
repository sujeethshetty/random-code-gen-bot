Sure! Here's a simple Python program that generates a random password consisting of letters and numbers:

```python
import random

def generate_password(length):
    password = ''
    characters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
    
    for _ in range(length):
        password += random.choice(characters)
    
    return password

password_length = int(input("Enter the length of the password: "))
random_password = generate_password(password_length)

print("Your random password is:", random_password)
```

In this program, the `generate_password` function takes a length parameter and creates a random password of that length by selecting characters randomly from a pool of letters and numbers. The user is prompted to enter the desired length of the password, and then the