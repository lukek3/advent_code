# --- part 1

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

for i, update in enumerate(updates):
    if check_rules(update):
        valid.append((i + 1, update))


middle_sums = 0

for _, update in valid:
    if len(update) % 2 == 1:
        middle = update[len(update) // 2]
        middle_sums += middle


print(middle_sums)
