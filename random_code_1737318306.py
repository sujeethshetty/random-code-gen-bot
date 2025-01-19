Here is a simple Python program that generates a random password of a specified length:

```python
import random
import string

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for i in range(length))
    return password

# Get user input for password length
while True:
    try:
        length = int(input("Enter the length of the password you want to generate: "))
        break
    except ValueError:
        print("Please enter a valid integer for the length.")

# Generate and display the password
password = generate_password(length)
print("Your random password is:", password)
```

This program defines a function `generate_password` that