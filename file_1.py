inp = input()

print(inp)

letters = 0
digits = 0

for ch in inp:
    if ch.isnumeric():
        digits += 1
    elif ch.isalpha():
        letters += 1

print(f"letters: {letters} \ndigits: {digits}")
