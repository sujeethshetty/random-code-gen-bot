```python
# Welcome to the Floating Sky Castle Exploration Simulator!

def explore_sky_castle():
    sky_castle_height = 500  # Height of the floating sky castle
    player_altitude = 0  # Start at ground level
    player_speed = 10  # Speed of ascending
    player_energy = 100  # Energy level

    print("You find yourself at the base of a magnificent floating sky castle. It's time to explore!")

    while player_altitude < sky_castle_height:
        print(f"You are {sky_castle_height - player_altitude} meters away from the castle.")
        action = input("Do you want to ascend? (yes/no): ")

        if action.lower() == "yes":
            if player_energy >= 10:
                player_altitude += player_speed
                player_energy -= 10
                print("You ascend further into the sky castle.")
            else:
                print("You are too exhausted to ascend. Rest and try again!")
        elif action.lower() == "no":
            print("You decide to stay on the ground and explore the surroundings.")
            break
        else:
            print("Invalid input. Please try again.")

    if player_altitude >= sky_castle_height:
        print("Congratulations! You have reached the floating sky castle.")

explore_sky_castle()
```

This program simulates the exploration of a floating sky castle. It includes a loop for ascending towards the castle and