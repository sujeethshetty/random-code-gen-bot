```python
# Welcome to the underwater world of salvaging with our trusty robot ROBO-TIDE!
def main():
    print("Initializing ROBO-TIDE for an underwater salvage mission...")
    dive_depth = 100  # Dive depth in meters
    salvage_items = ["treasure chest", "old anchor", "shipwreck parts", "rare artifact"]
    
    print(f"Descending to {dive_depth} meters below the surface.")
    
    # Loop through salvage items found at the seabed
    for item in salvage_items:
        retrieve_item(item)
    
    print("All items salvaged! Ascending back to the surface.")

# Function to retrieve an item from the seabed
def retrieve_item(item_name):
    print(f"ROBO-TIDE salvaging {item_name}...")
    # Simulating the retrieval process
    print(f"{item_name} successfully retrieved!")
    
if __name__ == "__main__":
    main()
```

This program simulates an underwater salvage mission with a robot named ROBO-TIDE. It descends to a specified depth, retrieves various items from the seabed, and then ascends back to the surface. The program showcases the use of functions, loops, and conditional logic to create an interactive and engaging scenario.