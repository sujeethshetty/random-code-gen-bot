Here is a simple Python program that generates a random number between 1 and 10 and asks the user to guess the number. It then checks if the user's guess is correct:

```python
import random

def guess_the_number():
    number_to_guess = random.randint(1, 10)
    
    while True:
        user_guess = int(input("Guess the number (between 1 and 10): "))
        
        if user_guess == number_to_guess:
            print("Congratulations! You guessed the correct number.")
            break
        else:
            print("Sorry, that's not the correct number. Try again.")

if __name__ == "__main__":
    print("Welcome to the Guess the Number game!")
    guess_the_number