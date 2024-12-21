# --- part 1

with open("day_4/input.txt") as fp:
    puzzle = fp.read().strip().split("\n")

n = len(puzzle)
m = len(puzzle[0])

# make list of directions for grid search
directions = []
for dx in range(-1, 2):
    for dy in range(-1, 2):
        if dx !=0 or dy != 0:
            directions.append((dx, dy))

# test each direction from one point in grid
def search(i, j, d):
    """
    d: starting coordinate direction
    i, j starting location
    """
    dx, dy = d
    for k, x in enumerate("XMAS"):
        ii = i + k * dx
        jj = j + k * dy
        if not (0 <= ii < n and 0 <= jj < m):
            return False
        if puzzle[ii][jj] != x:
            return False
    return True

ans = 0 
for i in range(n):
    for j in range(m):
        for d in directions:
            ans += search(i, j, d)

print(ans)