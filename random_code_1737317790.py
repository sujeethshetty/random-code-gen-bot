Here is a simple Python program that generates a random quote from a list of quotes when executed:

```python
import random

def get_random_quote():
    quotes = [
        "The only way to do great work is to love what you do. - Steve Jobs",
        "In the middle of difficulty lies opportunity. - Albert Einstein",
        "Success is not the key to happiness. Happiness is the key to success. - Albert Schweitzer",
        "The best way to predict the future is to create it. - Peter Drucker",
        "It does not matter how slowly you go as long as you do not stop. - Confucius"
    ]
    
    return random.choice(quotes)

if __name__ == "__main__":