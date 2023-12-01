# Array of lines in the input file
lines = []

with open("./input.txt") as f:
    # readlines() returns a list of lines
    lines = f.readlines()

numbers = [
    "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"
]

# Initialize the total to 0
total = 0

for line in lines:
    digits = []
    for i in range(len(line)):
        # This is called "slicing", line[i:] means
        # "the array with everything in `line` after the index `i`"
        line_after_i = line[i:]

        # if the first character in the slice (line[i]) is a digit, add it to the array
        if line_after_i[0].isdigit():
            digits.append(int(line_after_i[0]))
        else:
            # Check every number
            for n in range(len(numbers)):
                # See if the sliced line starts with the number text, if it does,
                # convert it and add it to the digits array
                if line_after_i.startswith(numbers[n]):
                    # n+1 because "one" is at index 0 in `numbers`
                    digits.append(n + 1)

    total += digits[0] * 10 + digits[-1]

print(f"Part Two: {total}")
