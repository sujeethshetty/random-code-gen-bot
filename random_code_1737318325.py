Here is a simple Python program that generates a random number between 1 and 10 and asks the user to guess the number. It provides feedback on whether the guess is correct or not:

```python
import random

def guess_number():
    number_to_guess = random.randint(1, 10)
    
    while True:
        user_guess = int(input("Guess a number between 1 and 10: "))
        
        if user_guess == number_to_guess:
            print("Congratulations! You guessed the correct number.")
            break
        else:
            print("Sorry, that's not the correct number. Try again.")

guess_number()
```

You can run this program in your Python environment to interactively guess the random number.