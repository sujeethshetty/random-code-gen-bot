Sure! Here's a simple Python program that generates a random password of a specified length using uppercase letters, lowercase letters, and numbers:

```python
import random
import string

def generate_password(length):
    characters = string.ascii_letters + string.digits
    password = ''.join(random.choice(characters) for i in range(length))
    return password

def main():
    password_length = int(input("Enter the length of the password you want to generate: "))
    password = generate_password(password_length)
    print("Your random password is:", password)

if __name__ == "__main__":
    main()
```

This program prompts the user to enter the desired length of the password, generates a random password of that length, and then displays