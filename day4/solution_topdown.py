import functools

# For each line in the input, first take everything after the ':', the  split the
# winning numbers from the card (split at '|'), and finally,
# Split each set of numbers by whitespace and convert to integers
with open("input.txt") as file:
    cards = [[
        set(map(int, e.split()))
        for e in line.strip().split(': ')[1].split(' | ')
    ] for line in file.readlines()]

# Part one is the sum of all card winning values
# Card winning values are calculated by the function `0 if n == 0 else 2**(n - 1)`
# The problem states "each match after the first doubles the point value of that card"
# If you remember basic binary, 2**x is equivalent to multiplying 2 by itself `n` times
# There is also a case if there are no matches, but 2**(0-1) is 1/2,
# so we need to handle this case seperately to return 0
p1 = sum([
    0 if n == 0 else 2**(n - 1)
    for n in [len(numbers & winning) for winning, numbers in cards]
])
print(f"Part One: {p1}")


# This is a very basic solution using a technique called Dynamic Programming
# Which breaks one large problem down into smaller subproblems recursively
# The large problem is calculating how many cards each card wins
# A smaller problem is calculating how many cards each subsequent card wins
# This is a recursive "top-down" implementation of this technique
# It would normally be slow, but thanks to a technique called "memoization" (caching)
# It runs pretty fast!
@functools.cache # This automatically memoizes the function!
def p2(c):
    winning, numbers = cards[c]
    wct = len(numbers & winning)
    s = 1
    if wct != 0:
        for o in range(1, wct + 1):
            s += p2(c + o)
    return s


print(f"Part Two: {sum([p2(i) for i in range(len(cards))])}")
