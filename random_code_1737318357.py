Here is a simple Python program that generates a random password of a specified length:

```python
import random
import string

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    length = int(input("Enter the length of the password: "))
    
    if length <= 0:
        print("Please enter a valid length for the password.")
    else:
        password = generate_password(length)
        print(f"Your random password is: {password}")

if __name__ == "__main__":
    main()
```

This program defines a `generate_password` function that takes a length