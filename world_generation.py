import random
import numpy as np
import matplotlib.pyplot as plt
from scipy.ndimage import gaussian_filter

# Define world size
WORLD_SIZE = (50, 50)  # 50x50 tile grid

# Define terrain types
terrain_types = {
    0: "water",
    1: "grass",
    2: "forest",
    3: "mountain",
    4: "desert",
    5: "village",
    6: "ruins",
    7: "dungeon"
}

# Generate structured biome placement using Perlin-like noise
def generate_world(size):
    world = np.random.rand(size[0], size[1])  # Generate noise map
    world = gaussian_filter(world, sigma=5)  # Smooth the noise for natural transitions
    
    terrain_map = np.zeros(size, dtype=int)
    for x in range(size[0]):
        for y in range(size[1]):
            noise_value = world[x, y]
            if noise_value < 0.2:
                terrain_map[x, y] = 0  # Water
            elif noise_value < 0.5:
                terrain_map[x, y] = 1  # Grass
            elif noise_value < 0.7:
                terrain_map[x, y] = 2  # Forest
            elif noise_value < 0.85:
                terrain_map[x, y] = 3  # Mountain
            else:
                terrain_map[x, y] = 4  # Desert
    
    return terrain_map

# Add AI-generated points of interest (villages, ruins, dungeons)
def add_landmarks(world, num_villages=3, num_ruins=2, num_dungeons=2):
    size_x, size_y = world.shape
    for _ in range(num_villages):
        x, y = random.randint(0, size_x - 1), random.randint(0, size_y - 1)
        if world[x, y] in [1, 2]:  # Villages appear on grass or forest
            world[x, y] = 5
    
    for _ in range(num_ruins):
        x, y = random.randint(0, size_x - 1), random.randint(0, size_y - 1)
        if world[x, y] in [1, 2, 3]:  # Ruins appear on land
            world[x, y] = 6
    
    for _ in range(num_dungeons):
        x, y = random.randint(0, size_x - 1), random.randint(0, size_y - 1)
        if world[x, y] in [2, 3]:  # Dungeons appear in forests or mountains
            world[x, y] = 7
    
    return world

# Function to display the world as a map
def display_world(world):
    color_map = {
        0: "blue",    # Water
        1: "green",   # Grass
        2: "darkgreen",  # Forest
        3: "gray",    # Mountain
        4: "yellow",   # Desert
        5: "brown",    # Village
        6: "purple",   # Ruins
        7: "black"     # Dungeon
    }

    plt.figure(figsize=(10,10))
    plt.imshow(world, cmap='terrain', interpolation='nearest')
    plt.colorbar(label="Terrain Type")
    plt.title("AI-Generated RPG World with Landmarks")
    plt.show()

# Generate and display the world
world = generate_world(WORLD_SIZE)
world = add_landmarks(world)
display_world(world)

# Ensure the figure window appears
plt.show()
