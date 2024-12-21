import itertools

with open("day_7/inputs.txt", "r") as fp:
    lines = fp.read().strip().split("\n")

    test_items = dict()
    for entry in lines:
        key, values = entry.split(":")
        test_items[int(key)] = [int(x) for x in values.strip().split()]

    ans = 0
    for target, values in test_items.items():
        for ops in itertools.product(["+", "*", "||"], repeat=len(values) - 1):
            result = values[0]
            for i in range(len(ops)):
                if ops[i] == "+":
                    result += values[i + 1]
                elif ops[i] == "*":
                    result *= values[i + 1]
                else:
                    result = int(str(result) + str(values[i + 1]))
            if result == target:
                ans += target
                break

print(ans)