Here is a simple Python program that generates a random password consisting of letters (both uppercase and lowercase) and numbers:

```python
import random
import string

def generate_password(length=8):
    characters = string.ascii_letters + string.digits
    password = ''.join(random.choice(characters) for i in range(length))
    return password

def main():
    password_length = int(input("Enter the length of the password: "))
    new_password = generate_password(password_length)
    print(f"Your random password is: {new_password}")

if __name__ == "__main__":
    main()
```

This program prompts the user to enter the desired length of the password, then generates a random password of that length using a combination of letters