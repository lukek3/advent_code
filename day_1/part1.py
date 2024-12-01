# --- part 1

### read data
with open("day_1/input.txt", "r") as fp:
    input = fp.readlines()

### list of lists for input rows
nums = [x.split() for x in input]

### sort and cast to int
nums_left = [int(left[0]) for left in nums]
nums_right = [int(right[1]) for right in nums]

nums_left.sort()
nums_right.sort()


### find difference between sorted values
results = list()
for index in range(len(nums_left)):
    difference = abs(nums_left[index] - nums_right[index])
    results.append(difference)

print(sum(results))