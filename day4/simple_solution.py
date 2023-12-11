input = """YOUR INPUT HERE""".splitlines()

total = 0

cards = []
for line in input:
    # winning_numbers = []
    # numbers=[]
    card_name, card = line.split(":")
    winning, card_numbers = card.split(' | ')

    winning = [int(e) for e in winning.split()]
    numbers = [int(e) for e in card_numbers.split()]

    winning = set(winning)
    numbers = set(numbers)

    # Numbers that are in the card and also winning numbers
    winning_numbers_we_have = numbers & winning

    if len(winning_numbers_we_have):
        score = 1
        for i in range(1, len(winning_numbers_we_have)):
            score *= 2
        total += score

print(f"Part One Solution: {total}")
