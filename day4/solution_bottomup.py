with open("input.txt") as file:
    cards = [[
        set(map(int, e.split()))
        for e in line.strip().split(': ')[1].split(' | ')
    ] for line in file.readlines()]

# We have one of each card
number_of_each_card = [1 for i in range(len(cards))]

# Strangely enough, this solves the same problem as `solution_topdown.py` but without recursion!
# Even more interestingly, it also finds the solution to small subproblems, but
# as opposed to the top-down approach, this bottom-up approach finds the solution to
# smaller subproblems first, then uses them to constitute the answer to the larger problem
for card_index, card in enumerate(cards):
    matches = len(card[0] & card[1])
    for n in range(matches):
        # If we have n copies of `card`, we get n copies of each subsequent card won
        number_of_each_card[card_index + n +
                            1] += number_of_each_card[card_index]
# The answer is the total number of cards
print(f"Part Two: {sum(number_of_each_card)}")