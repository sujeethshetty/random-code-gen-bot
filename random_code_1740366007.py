```python
# Welcome to the Haunted Mansion adventure game.
# Explore the rooms, find the key, and escape the mansion before it's too late!

def explore_mansion():
    rooms = ['Foyer', 'Kitchen', 'Library', 'Bedroom', 'Dungeon']
    key_location = 'Library'
    found_key = False

    for room in rooms:
        print("You are in the", room)
        if room == key_location:
            print("You found the key in the", room, "!")
            found_key = True
            break
        else:
            print("This room seems eerie...")

    if found_key:
        print("Congratulations! You found the key and escaped the Haunted Mansion!")
    else:
        print("Oh no! You couldn't find the key in time. The Haunted Mansion has claimed another victim...")

explore_mansion()
```

This whimsical program simulates an adventure game where the player explores rooms in a haunted mansion to find a key and escape before it's too late. The loop iterates through different rooms, and if the key is found, the player escapes successfully. Otherwise, a spooky message is displayed.