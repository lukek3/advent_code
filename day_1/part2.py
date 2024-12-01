# --- part 2
from collections import Counter

# Read data
with open('day_1/input.txt', 'r') as fp:
    input = fp.readlines()

# List of lists for input rows
nums = [x.split() for x in input]

# Parse numbers into separate lists
nums_left = [int(left[0]) for left in nums]
nums_right = [int(right[1]) for right in nums]

# Count occurrences of each number in nums_right, only care about numbers that appear in both lists
right_counts = Counter(nums_right)

# Calculate the score
score = sum(number * right_counts.get(number, 0) for number in nums_left)

print(score)