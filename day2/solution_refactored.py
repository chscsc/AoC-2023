#!/usr/bin/env python
# coding: utf-8

from math import *
import re

cs = {
    "red": 12,
    "green": 13,
    "blue": 14
}


def parseline(l):
    g, sack = re.search(
        r"Game (\d+): (.*)", l).groups()
    return int(g), [[(int(n[0]), n[1]) for n in [n.split() for n in e.split(", ")]] for e in sack.split('; ')]


inp = [parseline(line.strip()) for line in open("./input.txt").readlines()]

p1 = sum([gid for gid, bag in inp if all([all(bct <= cs[btype]
         for bct, btype in reveal) for reveal in bag])])
print(f"Part One: {p1}")


def rev2map(rev):
    m = {}
    for ct, color in rev:
        m[color] = ct
    return m


inpmap = [(gid, [rev2map(rev) for rev in bag]) for gid, bag in inp]

p2 = sum([
    prod([
        max(rev[color] if color in rev else 0 for rev in bag)
        for color in cs.keys()
    ])
    for gid, bag in inpmap
])

print(f"Part Two: {p2}")
