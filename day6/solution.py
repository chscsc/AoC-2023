from math import prod

numbers = [list(map(int, line.split(': ')[1].split()))
           for line in open("./input.txt").readlines()]


def race_wins(time, distance):
    wins = 0
    for t in range(time):
        t_remaining = time - t
        distance_traveled = t * t_remaining
        wins += 1 if (distance_traveled > distance) else 0
    return wins


p1 = prod([race_wins(time, dist) for time, dist in zip(*numbers)])
print(f"Part One: {p1}")

p2 = race_wins(
    int(''.join(map(str, numbers[0]))),
    int(''.join(map(str, numbers[1])))
)
print(f"Part Two: {p2}")
