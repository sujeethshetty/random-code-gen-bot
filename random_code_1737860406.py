```python
# Welcome to the Haunted Mansion Adventure Game!
# Explore the mysterious mansion and uncover its secrets.

def enter_haunted_mansion():
    print("You stand in front of a spooky mansion on a dark, foggy night...")
    print("Do you dare to enter?")
    
    while True:
        choice = input("Enter 'yes' or 'no': ").lower()
        
        if choice == 'yes':
            print("You push open the creaky door and step inside...")
            explore_mansion()
            break
        elif choice == 'no':
            print("You turn and run away in fear...")
            break
        else:
            print("Invalid choice. Try again.")

def explore_mansion():
    print("\nYou find yourself in a dimly lit hallway...")
    print("You hear strange noises coming from different rooms.")
    
    while True:
        action = input("Do you want to go 'left', 'right', or 'upstairs'? ").lower()
        
        if action == 'left':
            print("You enter the dusty library and find an old book with a cryptic message.")
        elif action == 'right':
            print("You enter the eerie dining room with a long table set for a banquet.")
        elif action == 'upstairs':
            print("You climb the creaky stairs and reach a dark corridor with flickering candles.")
        else:
            print("Invalid direction. Choose again.")

# Start the adventure