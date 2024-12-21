# --- part 1

with open("day_6/input.txt", "r") as fp:
    grid = fp.read().strip().split("\n")

n = len(grid)
m = len(grid[0])

directions = ["^", ">", "v", "<"]
direction_deltas = {"^": (-1, 0), ">": (0, 1), "v": (1, 0), "<": (0, -1)}

guard_pos = None
guard_dir = None
for r, row in enumerate(grid):
    for c, cell in enumerate(row):
        if cell in directions:
            guard_pos = (r, c)
            guard_dir = cell
            break
    if guard_pos:
        break


def turn_right(current_direction):
    index = directions.index(current_direction)
    next_item = (index + 1) % 4
    return directions[next_item]


seen = set()
while True:
    r, c = guard_pos
    seen.add(guard_pos)

    next_r = r + direction_deltas[guard_dir][0]
    next_c = c + direction_deltas[guard_dir][1]

    if not (0 <= next_r < n and 0 <= next_c < m):
        break

    if grid[next_r][next_c] == "#":
        guard_dir = turn_right(guard_dir)
    else:
        guard_pos = (next_r, next_c)

print(len(seen))
