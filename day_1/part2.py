# --- part 2
from collections import Counter

# read data
with open('day_1/input.txt', 'r') as fp:
    input = fp.readlines()

# list of lists for input rows
nums = [x.split() for x in input]

# parse numbers into separate lists
nums_left = [int(left[0]) for left in nums]
nums_right = [int(right[1]) for right in nums]

# count occurrences of each number in nums_right, only care about numbers that appear in both lists
right_counts = Counter(nums_right)

# calculate the score
score = sum(number * right_counts.get(number, 0) for number in nums_left)

print(score)