Here is a simple Python program that generates a random password based on user input for the length of the password:

```python
import random
import string

def generate_password(length):
    password = ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(length))
    return password

def main():
    print("Welcome to the Random Password Generator!")
    length = int(input("Enter the length of the password you'd like to generate: "))

    if length <= 0:
        print("Invalid length. Please enter a positive number.")
    else:
        password = generate_password(length)
        print("Your random password is:", password)

if __name__ == "__main__":
    main()
```

In this program,