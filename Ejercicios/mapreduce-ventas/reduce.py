import sys

current_name = None
current_sum = 0

for line in sys.stdin:
    line = line.strip()
    if not line:
        continue
    name, value = line.split('\t', 1)
    value = int(value)
    if name == current_name:
        current_sum += value
    else:
        if current_name is not None:
            print(f"{current_name}\t{value}")
        current_name = name
        current_sum = value

if current_name is not None:
    print(f"{current_name}\t{current_sum}")