# --- part 2

### read data
with open("day_2/input.txt", "r") as fp:
    input = fp.readlines()

### list of lists for input rows, cast to int
reports = [[int(x) for x in row.split()] for row in input]


def is_safe_report(report):
    is_increasing = all(
        0 < (report[i + 1] - report[i]) <= 3 for i in range(len(report) - 1)
    )
    is_decreasing = all(
        0 > (report[i + 1] - report[i]) >= -3 for i in range(len(report) - 1)
    )
    return is_increasing or is_decreasing


def is_safe_with_one_removal(report):
    for i in range(len(report)):
        modified_report = report[:i] + report[i + 1 :]  # remove a level
        if is_safe_report(modified_report):  # re-use old conditions
            return True
    return False


safe_reports_count = sum(1 for report in reports if is_safe_with_one_removal(report))

print(safe_reports_count)
