```python
def discover_magic_forest():
    magic_tree_count = 10
    magic_ponds = ['Enchanted Lake', 'Whispering Falls', 'Glowing Springs']
    
    print("Welcome to the Fantasy Forest!")
    print("You embark on a journey to discover its secrets...\n")
    
    for tree in range(1, magic_tree_count + 1):
        print(f"You encounter a magical tree #{tree} with shimmering leaves.")
    
    print("\nAs you wander deeper, you find yourself at the edge of mystical ponds:")
    for pond in magic_ponds:
        print(f"- {pond}")
    
    print("\nYou feel the forest whispering its ancient secrets to you.")
    
# Explore the magic forest
discover_magic_forest()
```

This program creates a magical forest setting where the user embarks on a journey to discover enchanted trees and mystical ponds. It showcases the use of a function for exploring the forest and loops for encountering magical elements. The forest's atmosphere is brought to life with descriptive text output.