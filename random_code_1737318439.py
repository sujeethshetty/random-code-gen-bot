Sure! Here is a simple Python program that generates a random number guessing game. The program will ask the user to guess a number between 1 and 10 until they guess correctly.

```python
import random

def guess_number():
    target_number = random.randint(1, 10)
    guessed = False
    
    while not guessed:
        guess = int(input("Guess a number between 1 and 10: "))
        
        if guess == target_number:
            print("Congratulations! You guessed the correct number.")
            guessed = True
        else:
            print("Try again!")

guess_number()
```

In this program, we use the `random` module to generate a random number between 1 and 10. The `