Here is a simple Python program that generates a random password based on user input for the length of the password:

```python
import random
import string

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for i in range(length))
    return password

def main():
    length = int(input("Enter the length of the password: "))
    password = generate_password(length)
    print(f"Generated password: {password}")

if __name__ == "__main__":
    main()
```

This program first defines a function `generate_password` that takes the length of the password as an argument and generates a random password using a combination of letters, digits