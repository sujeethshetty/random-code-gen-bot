Here is a simple Python program that generates a random password with a specified length:

```python
import random
import string

def generate_random_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for i in range(length))
    return password

def main():
    password_length = int(input("Enter the length of the password you want to generate: "))
    random_password = generate_random_password(password_length)
    print("Your random password is:", random_password)

if __name__ == "__main__":
    main()
```

This program prompts the user to enter the length of the password they want to generate. It then generates a random password of that length using a