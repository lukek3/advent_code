# --- part 2

with open("day_5/input.txt", "r") as fp:
    raw_rules, updates = fp.read().strip().split("\n\n")

    rules = []
    for line in raw_rules.split("\n"):
        a, b = line.split("|")
        rules.append((int(a), int(b)))

    updates = [list(map(int, line.split(","))) for line in updates.split("\n")]


def check_rules(update):
    for a, b in rules:
        if a in update and b in update:
            if update.index(a) > update.index(b):
                return False

    return True


valid = []
invalid = []

for i, update in enumerate(updates):
    if check_rules(update):
        valid.append((i + 1, update))
    else:
        invalid.append((i + 1, update))


def compare_pages(a, b):
    for x, y in rules:
        if x == a and y == b:
            return -1
        if x == b and y == a:
            return 1
    return 0


middle_sums = 0

for _, update in invalid:
    reorder = sorted(update, key=lambda x: [compare_pages(x, y) for y in update])
    if len(reorder) % 2 == 1:
        middle = reorder[len(reorder) // 2]
        middle_sums += middle


print(middle_sums)
