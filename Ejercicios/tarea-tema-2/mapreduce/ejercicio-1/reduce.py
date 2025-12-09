import sys

current = None
total = 0
for line in sys.stdin:
    word, n = line.strip().split("\t")
    n = int(n)

    if word == current:
        total += n
    else:
        if current:
            print(f"{current}\t{total}")
        current = word
        total = n

if current:
    print(f"{current}\t{total}")