blocks = {
    "A": (4, 3),
    "B": (3, 2),
    "C": (5, 2),
    "D": (2, 4),
    "E": (3, 3),
    "F": (2, 2)
}

def hierarchical_floorplan(modules, x=0, y=0):
    # Base case
    if len(modules) == 1:
        m = modules[0]
        return {m: (x, y)}, blocks[m][0], blocks[m][1]

    # Divide
    mid = len(modules) // 2
    left = modules[:mid]
    right = modules[mid:]

    # Solve recursively
    place_left, w1, h1 = hierarchical_floorplan(left, x, y)
    place_right, w2, h2 = hierarchical_floorplan(right, x + w1, y)

    # Merge side by side
    placements = {}
    placements.update(place_left)
    placements.update(place_right)

    total_w = w1 + w2
    total_h = max(h1, h2)

    return placements, total_w, total_h


mods = list(blocks.keys())
placements, W, H = hierarchical_floorplan(mods)

print("Hierarchical Floorplan:")
print("Chip Width =", W)
print("Chip Height =", H)

for b in placements:
    print(b, "->", placements[b])