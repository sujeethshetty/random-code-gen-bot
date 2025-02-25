```python
def explore_sky_castle():
    print("Welcome to the floating sky castle!")
    castle_rooms = ["Observatory", "Library", "Garden", "Bedroom", "Throne Room"]
    visited_rooms = []

    while len(visited_rooms) < len(castle_rooms):
        current_room = castle_rooms[len(visited_rooms)]
        print(f"You are now in the {current_room}.")
        visited_rooms.append(current_room)

    print("You have explored all the rooms in the sky castle. What a magical adventure!")

explore_sky_castle()
```

This program simulates the exploration of a floating sky castle with different rooms to discover. It uses a while loop to iterate through each room until all rooms have been visited. The castle_rooms list stores the names of the rooms, while visited_rooms keeps track of the rooms already visited. The function explore_sky_castle() is called to start the exploration journey.