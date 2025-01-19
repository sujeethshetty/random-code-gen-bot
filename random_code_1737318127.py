```python
# Space Exploration Adventure Game
# Explore different planets and collect space artifacts!

def space_exploration():
    planets = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']
    artifacts_collected = []

    print("Welcome, Space Explorer!")
    print("You are on a mission to explore the galaxy and collect rare artifacts.\n")

    for planet in planets:
        print(f"You have arrived at {planet}.")
        decision = input("Do you want to explore this planet? (yes/no): ")

        if decision.lower() == 'yes':
            print(f"You search {planet} and find a mysterious artifact!")
            artifacts_collected.append(f"Artifact from {planet}")
        else:
            print("You decide to continue your journey without exploring.\n")

    print("\nMission Complete! Here are the artifacts you collected:")
    for artifact in artifacts_collected:
        print(f"- {artifact}")

space_exploration()
```
This program simulates a space exploration adventure game where the player visits different planets, decides whether to explore them, and collects artifacts. The player can explore or skip each planet, and at the end, all collected artifacts are displayed.