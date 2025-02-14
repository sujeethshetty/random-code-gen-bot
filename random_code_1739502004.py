```python
def explore_sky_castle():
    sky_castle_height = 1000
    player_position = 0

    print("Welcome to the Floating Sky Castle! Let's start exploring...")
    
    while player_position < sky_castle_height:
        move = input("Do you want to go up or down? (u/d): ")
        
        if move == 'u':
            player_position += 100
            print(f"You move up. You are now at {player_position} feet above ground.")
        elif move == 'd':
            player_position -= 50
            if player_position < 0:
                print("You fell through the clouds! Game over.")
                return
            print(f"You move down. You are now at {player_position} feet above ground.")
        else:
            print("Invalid input. Please enter 'u' to go up or 'd' to go down.")
    
    print("Congratulations! You reached the top of the Floating Sky Castle!")

explore_sky_castle()
```

This program simulates the exploration of a Floating Sky Castle where the player can move up or down to navigate through different heights. The player must reach the top of the castle to win.