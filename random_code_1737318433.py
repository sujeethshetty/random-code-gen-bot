Sure! Here's a simple Python program that generates a random password of a specified length:

```python
import random
import string

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for i in range(length))
    return password

print("Welcome to the Random Password Generator!")
password_length = int(input("Enter the length of the password you'd like to generate: "))

if password_length <= 0:
    print("Please enter a valid length for the password.")
else:
    generated_password = generate_password(password_length)
    print(f"Your randomly generated password is: {generated_password}")
```

This program defines a `generate_password`