Certainly! Here's a program that simulates a mysterious time travel adventure where the user encounters a series of portals leading to different eras:

```python
def time_travel_adventure():
    portals = ["Ancient Rome", "Medieval Europe", "Wild West", "Future Space"]
    
    print("Welcome, Time Traveler! You are about to embark on a mysterious journey through time.")
    print("You will encounter different portals leading to various eras. Choose wisely!\n")
    
    for portal in portals:
        print(f"You approach a shimmering portal to {portal}.")
        choice = input("Do you wish to step through the portal? (yes/no): ")
        
        if choice.lower() == "yes":
            print(f"You've entered {portal}! What wonders and dangers await you?")
        else:
            print("You decide not to enter the portal and continue your journey.")
    
    print("\nYour mysterious time travel adventure comes to an end. Thank you for playing!")

time_travel_adventure()
```

In this whimsical program, the user encounters portals to different eras and decides whether to travel through them. The function, loop, and user input create an interactive and entertaining experience.