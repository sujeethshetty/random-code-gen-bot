```python
# Welcome to the Haunted Toy Workshop!
# Watch out for mischievous toys coming to life!

def haunted_toy_workshop():
    toys = ['creepy doll', 'haunted teddy bear', 'possessed toy train', 'spooky jack-in-the-box']
    
    print("In the dimly lit workshop, you see a collection of eerie toys:")
    for toy in toys:
        print(f"- {toy}")
    
    print("\nSuddenly, the toys start moving on their own!")
    print("You need to quickly capture them before they cause havoc!")

    captured_toys = []
    while len(captured_toys) < len(toys):
        action = input("\nEnter a toy to capture: ").lower()

        if action in toys and action not in captured_toys:
            print(f"You bravely capture the {action}!")
            captured_toys.append(action)
        else:
            print("Beware! The toy slips away or it's already captured.")

    print("\nPhew! You've successfully captured all the haunted toys.")
    print("The workshop is safe once again... for now.")

# Start the spooky adventure
haunted_toy_workshop()
```

This program creates a spooky atmosphere of a haunted toy workshop where the player captures mischievous toys before they cause trouble. It utilizes a loop to capture toys and a function to encapsulate the haunted workshop experience.