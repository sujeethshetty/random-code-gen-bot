Here is a simple Python program that generates a random password using lowercase letters and numbers:

```python
import random

def generate_password(length):
    characters = 'abcdefghijklmnopqrstuvwxyz0123456789'
    password = ''
    for _ in range(length):
        password += random.choice(characters)
    return password

password_length = 8
new_password = generate_password(password_length)

print(f'Your random password is: {new_password}')
```

This program defines a function `generate_password` that takes a length as input and generates a random password of that length using a combination of lowercase letters and numbers. The program then calls this function to generate an 8-character random password and prints it to the user.