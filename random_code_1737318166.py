Here is a simple Python program that generates a random password of a specified length:

```python
import random
import string

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for i in range(length))
    return password

password_length = int(input("Enter the length of the password: "))

if password_length <= 0:
    print("Please enter a valid password length.")
else:
    password = generate_password(password_length)
    print("Your random password is:", password)
```

In this program, the `generate_password` function generates a random password of the specified length by randomly selecting characters from the set of letters, digits, and