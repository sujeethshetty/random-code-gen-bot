Here is a simple Python program that generates and prints a random inspirational quote:

```python
import random

def generate_quote():
    quotes = [
        "The best way to predict the future is to create it.",
        "Believe you can and you're halfway there.",
        "Success is not the key to happiness. Happiness is the key to success.",
        "The only way to do great work is to love what you do.",
        "In the middle of every difficulty lies opportunity."
    ]
    
    return random.choice(quotes)

def main():
    quote = generate_quote()
    print("Here is your inspirational quote:")
    print(quote)

if __name__ == "__main__":
    main()
```

When you run this program