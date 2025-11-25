import sys

current_name = None
current_sum = 0.0
current_count = 0

for line in sys.stdin:
    line = line.strip()
    if not line:
        continue
    name, value = line.split('\t', 1)
    value = float(value)
    if name == current_name:
        current_sum += value
        current_count += 1
    else:
        if current_name is not None:
            avg = current_sum / current_count
            print(f"{current_name}\t{avg:.2f}")
        current_name = name
        current_sum = value
        current_count = 1

if current_name is not None:
    avg = current_sum / current_count
    print(f"{current_name}\t{avg:.2f}")