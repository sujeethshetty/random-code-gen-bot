Here is a simple Python program that simulates a dice roll game:

```python
import random

def roll_dice():
    return random.randint(1, 6)

def main():
    player1_score = 0
    player2_score = 0

    rounds = 3
    for round_num in range(1, rounds + 1):
        input("Press Enter to roll the dice for Player 1")
        player1_roll = roll_dice()
        print(f"Player 1 rolled: {player1_roll}")
        player1_score += player1_roll

        input("Press Enter to roll the dice for Player 2")
        player2_roll = roll_dice()
        print(f"Player 2 rolled: {