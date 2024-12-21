# --- part 2

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


def simulate(grid, guard_pos, guard_dir):
    seen = set()
    current_pos = guard_pos
    current_dir = guard_dir

    while True:
        r, c = current_pos
        state = (r, c, current_dir)

        if state in seen:
            return True
        seen.add(state)

        next_r = r + direction_deltas[current_dir][0]
        next_c = c + direction_deltas[current_dir][1]

        if not (0 <= next_r < n and 0 <= next_c < m):
            return False

        if grid[next_r][next_c] == "#":
            current_dir = turn_right(current_dir)
        else:
            current_pos = (next_r, next_c)


valid_positions = []
for r in range(n):
    for c in range(m):
        if grid[r][c] == ".":
            grid_with_obstruction = [list(row) for row in grid]
            grid_with_obstruction[r][c] = "#"

            if simulate(grid_with_obstruction, guard_pos, guard_dir):
                valid_positions.append((r, c))

print(len(valid_positions))
