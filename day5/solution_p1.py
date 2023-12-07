input = [[l.strip() for l in g.splitlines()]
         for g in open("./input.txt").read().split("\n\n")]

seeds = list(map(int, input[0][0].split("seeds: ")[1].split()))

# Converting the lines of three numbers into actual numbers
mappings = [[tuple(map(int, l.split())) for l in g[1:]] for g in input[1:]]

# Start out with our seeds
values = set(seeds.copy())

# It just so happens that the conversions in our input are in order
# eg. seed-to-soil is followed by soil-to-fertilizer and so on, so we can just go through them in order
for m in mappings:
    # Keep track of the numbers that have changed
    translated = set()
    # And what they changed to
    translated_to = set()

    for number in values:
        for dest, src, length in m:
            # Check if the seed is inside the range of the conversion
            if number > src and number <= (src + length):
                translated.add(number)
                translated_to.add(dest + number - src)
            # Otherwise, the number stays the same

        # Set the current values for the next "round" of conversions
    values = translated_to | {v for v in values if v not in translated}

print(f"Part One: {min(values)}")
