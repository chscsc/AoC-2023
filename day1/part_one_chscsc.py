# Array of lines in the input file
lines = []

with open("./input.txt") as f:
    # readlines() returns a list of lines
    lines = f.readlines()

# Initialize the total to 0
total = 0

for line in lines:
    # This is called a list comprehension, it's a python thing
    # We can use it to "filter" values:
    # This specific list comprehension creates a list of items, `digits`, from another list of
    # items, `line`, (which is string, a list of characters) only containing the
    # items that meet a certain criteria (c.isdigit())
    # This is equivalent to:
    #
    # digits = []
    # for c in line:
    #     if c.isdigit():
    #         digits.append(c)
    #
    digits = [c for c in line if c.isdigit()]
    # In python, using the index `-1` returns the last item in a list/array
    total += int(digits[0] + digits[-1])

print(f"Part One: {total}")
