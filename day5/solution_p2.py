input = [[l.strip() for l in g.splitlines()]
         for g in open("./input.txt").read().split("\n\n")]

seeds = list(map(int, input[0][0].split("seeds: ")[1].split()))
seedranges = list(zip(seeds[::2], map(sum, zip(seeds[::2], seeds[1::2]))))

# Converting the lines of three numbers into actual numbers
mappings = [[tuple(map(int, l.split())) for l in g[1:]] for g in input[1:]]

# Start out with our seeds
ranges = seedranges.copy()

# It just so happens that the conversions in our input are in order
# eg. seed-to-soil is followed by soil-to-fertilizer and so on, so we can just go through them in order
for m in mappings:
    # Keep track of the numbers that have changed
    translated = set()
    # And what they changed to
    translated_to = set()

    for r in ranges:
        start, end = r
        for dest, src, length in m:
            srcend = src + length

            inside = (max(start, src), min(end, srcend))

            # Check if the seed range intersects with the range of the conversion
            if (inside[0] < inside[1]):
                translated.add(r)
                translated_to.add(
                    (inside[0] - src + dest, inside[1] - src + dest))

                # Now that we've translated what's in the conversion
                # We need to check if there is anything before or after that still needs to be converted
                # If so, we add it back onto `ranges`, the list of things that need converting
                before = (start, src)
                after = (srcend, end)
                if (before[0] < before[1]):
                    ranges.append(before)
                if (after[0] < after[1]):
                    ranges.append(after)

        # Set the current values for the next "round" of conversions
    ranges = list(translated_to) + [v for v in ranges if v not in translated]

print(f"Part Two: {min(r[0] for r in ranges)}")
