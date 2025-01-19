Here is a simple Python program that generates a random inspirational quote each time it is run:

```python
import random

# List of inspirational quotes
quotes = [
    "Believe you can and you're halfway there.",
    "The only way to do great work is to love what you do.",
    "Success is not the key to happiness. Happiness is the key to success.",
    "The best way to predict the future is to create it.",
    "You are never too old to set another goal or to dream a new dream."
]

def generate_quote():
    return random.choice(quotes)

if __name__ == "__main__":
    print("Welcome to the Inspirational Quote Generator!")
    input("Press Enter to generate an inspirational