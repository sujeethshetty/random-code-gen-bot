Sure! Here's a simple Python program that generates a random password based on the user's desired length:

```python
import random

def generate_password(length):
    characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*"
    password = ""
    for _ in range(length):
        password += random.choice(characters)
    return password

password_length = int(input("Enter the length of the password: "))
random_password = generate_password(password_length)

print("Your random password is:", random_password)
```

This program prompts the user to enter the desired length of the password, then generates a random password consisting of letters (both uppercase and lowercase), numbers, and special characters. Finally, it displays the generated password to the user