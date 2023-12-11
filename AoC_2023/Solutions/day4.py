import re

test_input = """Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19
Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1
Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83
Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36
Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11"""


def calc_score(match_count):
    """Calculate the score of a card based on the number of matches.
    the first match is worth 1 point and each match after the first doubles the point value of that card"""
    if match_count == 0:
        return 0
    else:
        score = 1
        for i in range(1, match_count):
            score *= 2
        return score


def count_matches(test_inputs):
    card_matches = {}
    regex_pattern = r"Card\s+(\d+): ([\d\s]+) \| ([\d\s]+)"
    for line in test_inputs.split("\n"):
        card, left, right = re.match(regex_pattern, line).groups()
        left, right = set(map(int, left.split())), set(map(int, right.split()))
        matches = left.intersection(right)
        card_matches[int(card)] = len(matches)
    return card_matches


# card_matches = count_matches(test_input)
with open("data/day4.txt", "r") as file:
    card_matches = count_matches(file.read())


# Part 1:
card_scores_p1 = {card: calc_score(match_count)
                  for card, match_count in card_matches.items()}
print(f"The result of part one is: {sum(card_scores_p1.values())}\n\n")


# Part 2:
card_count_p2 = {card: 1 for card in card_matches.keys()}
for card, match_count in card_matches.items():
    span = (card+1, card+match_count)
    print(card, match_count, span)
    for c_i in range(span[0], span[1]+1):
        if c_i in card_count_p2:
            card_count_p2[c_i] += card_count_p2[card]
        else:
            card_count_p2[c_i] = 1

print(f"The result of part two is: {sum(card_count_p2.values())}\n")
