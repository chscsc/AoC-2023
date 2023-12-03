import re

# Read the input
txt = [line.strip() for line in open("./input.txt").readlines()]

# Using a regular expression, find the location and value of all numbers in the input
numbers = [(row, match.span(), match.group(0)) for row in range(len(txt))
           for match in re.finditer(r'\d+', txt[row])]

# For every number, find all of the coordinated surrounding it
numbounds = [(int(num[2]), {(num[0]+o, col) for col in range(num[1][0]-1, num[1][1]+1)
              for o in [-1, 0, 1]}) for num in numbers]

# Find all of the positions of symbols in the input
symbols = {(row, col) for row in range(len(txt))
           for col in range(len(txt[0])) if txt[row][col] not in '1234567890.'}

# Find the sum of all numbers that have no symbols surrounding them, the part one answer
p1 = sum([s for s, bounds in numbounds if any(
    o in bounds for o in symbols)])

print(f"Part One: {p1}")

# Find the location of all asterisks
asterisks = {(row, col) for row, col in symbols}

# Find the numbers that touch each asterisk
ns_in_asterisks = [[n for n, b in numbounds if a in b] for a in asterisks]
# Find the sum of the products of both numbers touching each asterisk that touches 2 numbers
p2 = sum([a[0]*a[1] for a in ns_in_asterisks if len(a) == 2])

print(f"Part Two: {p2}")
