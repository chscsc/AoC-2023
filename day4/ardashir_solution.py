def process_line(line):
    win_nums, my_nums = line.split(':')[1].split('|')
    win_nums = set(map(int, win_nums.split()))
    my_nums = set(map(int, my_nums.split()))
    return sum(2 ** i for i in range(len(win_nums) + 1) if win_nums & my_nums)

def part1_and_part2(file_path):
    total_part1 = 0
    total_part2 = 0
    card_to_counts = {}

    with open(file_path) as f:
        for idx, line in enumerate(f, start=1):
            total_part1 += process_line(line)

            win_nums, my_nums = line.split(':')[1].split('|')
            win_nums = set(map(int, win_nums.split()))
            my_nums = set(map(int, my_nums.split()))

            count = sum(1 for num in win_nums if num in my_nums)
            total_part2 += count

            for i in range(count):
                card_to_counts[idx + i + 1] = card_to_counts.get(idx + i + 1, 0) + card_to_counts.get(idx, 1)

    print('Part 1:')
    print(total_part1)
    print('\nPart 2:')
    print(sum(card_to_counts.values()))

file_path = 'input.txt'
part1_and_part2(file_path)
