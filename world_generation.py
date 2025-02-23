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

# Generate terrain using Perlin noise for smoother transitions
def generate_world(size):
    world = np.zeros(size, dtype=int)
    for x in range(size[0]):
        for y in range(size[1]):
            noise_value = random.uniform(0, 1)
            if noise_value < 0.1:
                world[x, y] = 0  # Water
            elif noise_value < 0.5:
                world[x, y] = 1  # Grass
            elif noise_value < 0.7:
                world[x, y] = 2  # Forest
            elif noise_value < 0.85:
                world[x, y] = 3  # Mountain
            else:
                world[x, y] = 4  # Desert
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
world = generate_world(WORLD_SIZE)
display_world(world)

# Ensure the figure window appears
plt.show()
