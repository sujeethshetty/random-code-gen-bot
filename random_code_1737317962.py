Here is a simple Python program that generates a random multiplication quiz for the user to solve:

```python
import random

def generate_question():
    num1 = random.randint(1, 10)
    num2 = random.randint(1, 10)
    answer = num1 * num2
    return num1, num2, answer

def check_answer(num1, num2, answer):
    user_answer = int(input(f"What is {num1} x {num2}? "))
    if user_answer == answer:
        print("Correct!")
    else:
        print(f"Wrong! The correct answer is {answer}")

def main():
    print("Welcome to the Multiplication Quiz!")
    for _ in range(5):