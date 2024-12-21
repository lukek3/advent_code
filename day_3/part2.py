# --- part 2
import re


### read data
with open("day_3/input.txt", "r") as fp:
    input = fp.read()

### make regex
new_instructions = re.compile(r"(do\(\)|don't\(\))")
mul_regex = re.compile(r"mul\((\d+),(\d+)\)")

tokens = re.split(r"(do\(\)|don't\(\)|mul\(\d+,\d+\))", input)

# Initialize variables
enabled = True  # `mul` is enabled initially
results = []  # To store results of valid multiplications

# Process each token
for token in tokens:
    if not token.strip():
        continue  # Skip empty tokens

    # Check for instructions
    if new_instructions.fullmatch(token):
        if token == "do()":
            enabled = True
        elif token == "don't()":
            enabled = False
    # Check for valid mul(...) operations
    elif mul_regex.fullmatch(token):
        if enabled:
            # Extract numbers and perform multiplication
            match = mul_regex.match(token)
            num1, num2 = int(match.group(1)), int(match.group(2))
            results.append(num1 * num2)

sums = sum(results)
print(sums)
