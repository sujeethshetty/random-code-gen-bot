Sure! Here's a simple Python program that generates a random password with a specified length:

```python
import random
import string

def generate_random_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for i in range(length))
    return password

length = int(input("Enter the length of the password you want to generate: "))
random_password = generate_random_password(length)

print("Your random password is:", random_password)
```

This program defines a function `generate_random_password` that takes a length parameter and generates a random password with the specified length using a combination of letters, digits, and special characters. The program then prompts the user to enter the