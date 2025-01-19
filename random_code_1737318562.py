Sure! Here's a simple Python program that generates a random password of a specified length:

```python
import random
import string

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for i in range(length))
    return password

def main():
    length = int(input("Enter the length of the password: "))
    
    if length <= 0:
        print("Invalid length. Please enter a positive number.")
    else:
        password = generate_password(length)
        print("Generated password: ", password)

if __name__ == "__main__":
    main()
```

This program defines a `generate_password` function that creates a random password