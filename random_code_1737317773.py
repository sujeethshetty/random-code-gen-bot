Here's a simple Python program that generates a random password based on user input for password length:

```python
import random
import string

def generate_random_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for i in range(length))
    return password

def main():
    length = int(input("Enter the length of the password you want to generate: "))
    
    if length <= 0:
        print("Password length should be a positive integer.")
    else:
        password = generate_random_password(length)
        print(f"Your random password is: {password}")

if __name__ == "__main__":
    main()
```

This program allows the user