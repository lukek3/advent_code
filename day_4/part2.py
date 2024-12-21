# --- part 2

with open("day_4/input.txt") as fp:
    puzzle = fp.read().strip().split("\n")

n = len(puzzle)
m = len(puzzle[0])

# test each direction from one point in grid
def search(i, j):
    if not (1 <= i < n - 1 and 1 <= j < m - 1):
        return False
    if puzzle[i][j] != "A":
        return False
    
    diag_1 = f"{puzzle[i-1][j-1]}{puzzle[i+1][j+1]}"
    diag_2 = f"{puzzle[i-1][j+1]}{puzzle[i+1][j-1]}"

    return diag_1 in ["MS", "SM"] and diag_2 in ["MS", "SM"]

ans = 0 
for i in range(n):
    for j in range(m):
            ans += search(i, j)

print(ans)