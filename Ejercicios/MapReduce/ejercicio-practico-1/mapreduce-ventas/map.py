import sys

for index, line in enumerate(sys.stdin):
    if index != 0:
        parts = line.strip().split(',')
        product = parts[1]
        quantity = int(parts[3])
        price = int(parts[4])
        total = quantity * price
        print(f"{product}\t{total}")
