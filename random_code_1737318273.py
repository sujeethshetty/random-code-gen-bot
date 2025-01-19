Here is a simple Python program that generates a random password:

```python
import random
import string

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for i in range(length))
    return password

def main():
    length = int(input("Enter the length of the password you want to generate: "))
    password = generate_password(length)
    print("Generated Password:", password)

if __name__ == "__main__":
    main()
```

This program prompts the user to enter the desired length of the password they want to generate. It then generates a random password of the specified length using a combination of letters (both lowercase and uppercase), digits