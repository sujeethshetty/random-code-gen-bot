Here's a simple Python program that generates a random inspirational quote each time it is run:

```python
import random

def get_quote():
    quotes = [
        "Believe you can and you're halfway there.",
        "The only way to do great work is to love what you do.",
        "Success is not the key to happiness. Happiness is the key to success.",
        "In the middle of every difficulty lies opportunity.",
        "You are never too old to set another goal or to dream a new dream."
    ]
    
    return random.choice(quotes)

def main():
    print("Welcome to the Inspirational Quote Generator!")
    input("Press Enter to get your inspirational quote...")
    
    quote = get_quote()
    print