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
    
    if length < 6:
        print("Password length should be at least 6 characters.")
    else:
        password = generate_password(length)
        print("Your random password is:", password)

if __name__ == "__main__":
    main()
```

In this program, the `generate_password