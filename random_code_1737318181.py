Sure! Here is a simple Python program that generates a random password of a specified length:

```python
import random
import string

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for i in range(length))
    return password

def main():
    password_length = int(input("Enter the length of the password you want to generate: "))
    
    if password_length <= 0:
        print("Password length should be a positive integer.")
    else:
        password = generate_password(password_length)
        print("Your random password is:", password)

if __name__ == "__main__":
    main()
```

This program first prompts the user to