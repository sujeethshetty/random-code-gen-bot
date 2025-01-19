Here is a simple Python program that generates a random motivational quote each time it is run:

```python
import random

def get_random_quote():
    quotes = [
        "Believe you can and you're halfway there.",
        "You are never too old to set another goal or to dream a new dream.",
        "The only way to do great work is to love what you do.",
        "Success is not the key to happiness. Happiness is the key to success.",
        "The best preparation for tomorrow is doing your best today."
    ]
    
    return random.choice(quotes)

def main():
    print("Welcome to the Random Quote Generator!")
    input("Press Enter to get a motivational quote...")
    
    quote = get_random_quote