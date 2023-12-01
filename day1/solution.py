#!/usr/bin/env python

m = [
    "one",
    "two",
    "three",
    "four",
    "five",
    "six",
    "seven",
    "eight",
    "nine"
]

lines = [line.strip() for line in open("./input.txt").readlines()]


def parseline(l):
    l = [c for c in l if not c.isalpha()]
    return int(l[0] + l[-1])


inp = [parseline(l) for l in lines]
print(f"Part Two: {sum(inp)}")


def parseline2(l):
    for i, v in enumerate(m):
        l = l.replace(v, v[0] + str(i+1) + v[-1])

    l = [c for c in l if not c.isalpha()]
    # Needs the first and second characters, because they could be "involved" in another number-word!
    return int(l[0] + l[-1])


inp = [parseline2(l) for l in lines]
print(f"Part Two: {sum(inp)}")
