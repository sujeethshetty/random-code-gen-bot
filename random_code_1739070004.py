```python
# Welcome to the Desert Meteor Mining simulation!
# In this program, we will mine meteorites in the vast desert.

def mine_meteorites():
    meteorites_found = 0
    for day in range(1, 6):  # Mine for 5 days
        print(f"Day {day}: Searching for meteorites...")
        meteorites = day * 2  # Meteorites found increases each day
        meteorites_found += meteorites
        print(f"Found {meteorites} meteorites today!")

    return meteorites_found

def desert_meteor_mining():
    print("Welcome to Desert Meteor Mining!")
    total_meteorites = mine_meteorites()
    print("\nMining operation complete!")
    print(f"Total meteorites mined: {total_meteorites}")

desert_meteor_mining()
```

This program simulates a mining operation in the desert to collect meteorites. It includes a function to mine meteorites for 5 days, using a loop to iterate through each day. Finally, it calculates and displays the total number of meteorites mined.