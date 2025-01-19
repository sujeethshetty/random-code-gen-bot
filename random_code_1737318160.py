Here is a simple Python program that generates and prints a random quote each time you run it:

```python
import random

def get_random_quote():
    quotes = [
        "The only way to do great work is to love what you do. - Steve Jobs",
        "Innovation distinguishes between a leader and a follower. - Steve Jobs",
        "Stay hungry, stay foolish. - Steve Jobs",
        "Your time is limited, don't waste it living someone else's life. - Steve Jobs",
        "Don't let the noise of others' opinions drown out your own inner voice. - Steve Jobs"
    ]
    
    return random.choice(quotes)

def main():
    quote = get_random_quote()
    print("Random