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

# Apply random world events
def apply_world_events(world):
    events = [
        "A new ruin has been discovered in the mountains!",
        "A village has expanded, adding more homes.",
        "A rare comet passes by, bringing strange energy to the land.",
        "Heavy storms have flooded part of the grasslands.",
        "A mysterious traveler arrives, sharing secrets of the past."
    ]
    
    event = random.choice(events)  # Pick a random event
    print(f"🌍 World Event: {event}")  # Display event in terminal

    if "ruin" in event:
        x, y = random.randint(0, WORLD_SIZE[0]-1), random.randint(0, WORLD_SIZE[1]-1)
        world[x, y] = 6  # Add a new ruin
    
    return world

# Add AI-generated world lore
def generate_world_lore():
    world_lore = [
        "Legends speak of an ancient war that shaped this land...",
        "Many say a hidden artifact lies beneath the shifting sands of the desert.",
        "The villagers believe the mountains hold the key to an age-old prophecy.",
        "A forbidden spellbook was once buried in the ruins, waiting to be found.",
        "The forests whisper stories of a lost kingdom, hidden from time."
    ]
    return random.choice(world_lore)

# Add NPCs with movement, quests, tracking, and trading
def add_npcs(world):
    size_x, size_y = world.shape
    npc_list = []
    active_quests = {}
    completed_quests = {}
    npc_trading = {}
    npc_positions = {}
    
    dialogues = {
        "Villager": ["Welcome to our village!", "Can you bring me some herbs?", "The fields are bountiful this season."],
        "Wanderer": ["These ruins hold many secrets...", "I seek a lost artifact, can you help?", "Beware of the dungeons ahead."],
        "Dungeon Guardian": ["Turn back now, or face your doom!", "Defeat the monster within, and you shall be rewarded.", "Only the strong survive here."]
    }
    
    quests = {
        "Villager": {"task": "Gather 5 healing herbs", "reward": "10 gold"},
        "Wanderer": {"task": "Find an ancient artifact in the ruins", "reward": "Mystical Scroll"},
        "Dungeon Guardian": {"task": "Defeat the dungeon monster", "reward": "Legendary Sword"}
    }
    
    trading_items = {
        "Villager": {"item": "Healing Potion", "price": 5},
        "Wanderer": {"item": "Ancient Map", "price": 15},
        "Dungeon Guardian": {"item": "Enchanted Armor", "price": 50}
    }
    
    for x in range(size_x):
        for y in range(size_y):
            if world[x, y] in [5, 6, 7]:
                npc_type = "Villager" if world[x, y] == 5 else "Wanderer" if world[x, y] == 6 else "Dungeon Guardian"
                npc_list.append((x, y, npc_type, random.choice(dialogues[npc_type]), quests[npc_type]))
                active_quests[(x, y)] = quests[npc_type]
                npc_trading[(x, y)] = trading_items[npc_type]
                npc_positions[(x, y)] = (x, y)  # Initial NPC position
    
    return npc_list, active_quests, completed_quests, npc_trading, npc_positions

# Move NPCs randomly within a limited area
def move_npcs(npc_positions, world):
    new_positions = {}
    for (x, y), pos in npc_positions.items():
        new_x, new_y = max(0, min(WORLD_SIZE[0]-1, x + random.choice([-1, 0, 1]))), max(0, min(WORLD_SIZE[1]-1, y + random.choice([-1, 0, 1])))
        if world[new_x, new_y] not in [0]:  # Avoid water
            new_positions[(new_x, new_y)] = pos
        else:
            new_positions[(x, y)] = pos  # Stay in place if water is ahead
    return new_positions

# Generate and display the world
world = generate_world(WORLD_SIZE)
world = apply_world_events(world)
npcs, active_quests, completed_quests, npc_trading, npc_positions = add_npcs(world)
npc_positions = move_npcs(npc_positions, world)
lore = generate_world_lore()

# Display lore and event in terminal
print(f"📖 World Lore: {lore}")
print(f"🚶 NPCs have moved: {npc_positions}")

# Ensure the figure window appears
plt.show()
