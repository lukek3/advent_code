# --- part 1
import re

### read data
with open("day_3/input.txt", "r") as fp:
    input = fp.read()

### make regex
reg = re.compile(r"mul\(\d+,\d+\)")

### make iterable of results
output = reg.findall(input)

### helper function to extract digits and multiply them
def get_multiply(mul_obj):
    match = re.match(r"mul\((\d+),(\d+)\)", mul_obj)
    if match:
        num1 = int(match.group(1))
        num2 = int(match.group(2))

        results = num1 * num2

    return results


### make counter, iterate through mul objects and add to counter
data = 0
for item in output:
    data += get_multiply(item)

print(data)
