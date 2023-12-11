import re

WORD_TO_DIGIT_MAP = {'zero': '0',
                     'one': '1',
                     'two': '2',
                     'three': '3',
                     'four': '4',
                     'five': '5',
                     'six': '6',
                     'seven': '7',
                     'eight': '8',
                     'nine': '9'}

# --- Day 1: Trebuchet?! ---
# Part 1:
sum = 0
with open("data/day1.txt", "r") as file:
    for line in file:
        digits = [c for c in line.strip() if c.isnumeric()]
        sum += int(digits[0]+digits[-1])

print(f"Solution Day 1 Part 1: {sum}")

# Part 2:
sum = 0
with open("data/day1.txt", "r") as file:
    for string in file:

        line_digits = []
        for pattern, digit in WORD_TO_DIGIT_MAP.items():
            if pattern in string:
                line_digits.extend([(m.start(), digit)
                                   for m in re.finditer(pattern, string)])

        line_digits.extend([(i, c)
                           for i, c in enumerate(string) if c.isnumeric()])
        line_digits.sort(key=lambda x: x[0])
        sum += int(line_digits[0][1]+line_digits[-1][1])

print(f"Solution Day 1 Part 2: {sum}")
