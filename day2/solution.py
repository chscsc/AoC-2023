#!/usr/bin/env python
# coding: utf-8

from math import *
from collections import defaultdict

cs = {
    "red": 12,
    "green": 13,
    "blue": 14
}


def parseline(l):
    g, s = l.split(': ')
    s = s.split('; ')
    return int(g.split(' ')[1]), [[(int(n[0]), n[1]) for n in [n.split() for n in e.split(", ")]] for e in s]


inp = [parseline(line.strip()) for line in open("./input.txt").readlines()]
inp

pbags = 0
for gid, bag in inp:
    if all([all(bct <= cs[btype] for bct, btype in reveal) for reveal in bag]):
        pbags += gid

print(f"Part One: {pbags}")

s = 0
for gid, bag in inp:
    bc = defaultdict(int)
    for color in cs.keys():
        for rev in bag:
            for bct, bty in rev:
                if bty == color:
                    bc[color] = max(bc[color], bct)
    s += (bc["red"] * bc['blue'] * bc["green"])
print(f"Part Two: {s}")
