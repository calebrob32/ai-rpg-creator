import random
import numpy as np
import matplotlib.pyplot as plt

# Define world size
WORLD_SIZE = (50, 50)  # 50x50 tile grid

# Define terrain types
terrain_types = {
    0: "water",
    1: "grass",
    2: "forest",
    3: "mountain",
    4: "desert"
}

# Generate terrain using a weighted random choice for distribution
def generate_world(size):
    world = np.random.choice(list(terrain_types.keys()), size=size, p=[0.1, 0.5, 0.2, 0.1, 0.1])
    return world

# Function to display the world as a map
def display_world(world):
    color_map = {
        0: "blue",    # Water
        1: "green",   # Grass
        2: "darkgreen",  # Forest
        3: "gray",    # Mountain
        4: "yellow"   # Desert
    }

    plt.figure(figsize=(10,10))
    plt.imshow(world, cmap='terrain', interpolation='nearest')
    plt.colorbar(label="Terrain Type")
    plt.title("AI-Generated RPG World")
    plt.show()

# Generate and display the world
world = generate_world(WORLD_SIZE)  # <- This should now be correctly defined
display_world(world)

# Ensure the figure window appears
plt.show()
