Sure! Here's a simple Python program that generates a random password of a specified length:

```python
import random
import string

def generate_password(length):
    password = ''
    characters = string.ascii_letters + string.digits + string.punctuation
    for _ in range(length):
        password += random.choice(characters)
    return password

password_length = int(input("Enter the length of the password you want to generate: "))
new_password = generate_password(password_length)
print("Generated Password:", new_password)
```

This program asks the user to input the length of the password they want to generate. It then generates a random password using a combination of uppercase letters, lowercase letters, digits, and punctuation symbols. Finally, it displays the