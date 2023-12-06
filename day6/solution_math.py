from math import prod, sqrt, floor

numbers = [list(map(int, line.split(': ')[1].split()))
           for line in open("./input.txt").readlines()]


# ♫ x equals negative b
# plus or minus the square root
# of b squared minus 4ac
# all over 2a ♫
def quadratic_formula(a, b, c):
    desc = b**2 - 4*a*c
    # Sort it so it returns the lowest root first
    return sorted([(-b - sqrt(desc)) / (2*a), (-b + sqrt(desc)) / (2*a)])


# Let's make a variable, `x`, that is the time we spend charging the boat (pressing the button)
# If you hold the button for `x` amount of time, the boat will go at `x` distance/time
# The race must take `time` time, so the amount of time the boat is moving must be `time-x`
# Thanks to basic physics, we know that distance = speed*time
# So the distance the boat will travel is `x * (time - x)`
# Our goal is to find when the boat exceeds the record distance `distance`
# Or: `x * (time - x) > distance`
# If we multiply out the equation we get `-x^2 + time*x > distance`
# Thanks to math, we know that to solve this we need to find where `-x^2 + time*x` is equal to `distance`
# Or: `x * (time - x) - distance = 0`
# To do this, we can use the quadratic formula!
# If we get two zeros (roots), we know, at least with this equation, that all `x` between the zeros produce a value > `distance`
def race_wins(time, distance):
    # -x^2 + time*x - distance
    first_root, second_root = quadratic_formula(-1, time, -distance)
    # The puzzle tells us that only integers are valid, so we round down (floor)
    return floor(second_root) - floor(first_root)


p1 = prod([race_wins(time, dist) for time, dist in zip(*numbers)])
print(f"Part One: {p1}")

p2 = race_wins(
    int(''.join(map(str, numbers[0]))),
    int(''.join(map(str, numbers[1])))
)
print(f"Part Two: {p2}")
