import sys

def read_lines_to_list(file_name="input"):
    try:
        with open(file_name, "r", encoding="utf-8") as file:
            return [line.strip() for line in file]

def calculate_wins(time, record):
    return sum(1 for i in range(time + 1) if i * (time - i) > record)

def part_one():
    try:
        lines = read_lines_to_list(sys.argv[1] if len(sys.argv) > 1 else "input")
        times, records = map(int, lines[0].split(":")[1].strip().split()), map(int, lines[1].split(":")[1].strip().split())
        num_ways = [calculate_wins(time, record) for time, record in zip(times, records)]
        result = reduce(lambda x, y: x * y, num_ways, 1)
        print(f"Part 1: {result}")

def part_two():
    try:
        lines = read_lines_to_list(sys.argv[1] if len(sys.argv) > 1 else "input")
        time, record = map(int, "".join(lines[0].split(":")[1].strip().split())), map(int, "".join(lines[1].split(":")[1].strip().split()))
        wins = calculate_wins(time, record)
        print(f"Part 2: {wins}")

if __name__ == "__main__":
    part_one()
    part_two()
