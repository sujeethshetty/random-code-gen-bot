Certainly! Here's a simple Python program that generates a random password of a specified length:

```python
import random
import string

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for i in range(length))
    return password

if __name__ == "__main__":
    password_length = int(input("Enter the length of the password you want to generate: "))
    
    if password_length <= 0:
        print("Password length should be greater than 0.")
    else:
        generated_password = generate_password(password_length)
        print(f"Your random password of length {password_length} is: {generated_password}")
```

In this