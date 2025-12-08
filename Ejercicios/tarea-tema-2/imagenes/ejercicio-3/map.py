import sys

for line in sys.stdin:
    parts = line.split()
    if len(parts) < 8:
        continue

    ip = parts[0]
    code = parts[-2]

    print(f"code_{code}\t1")
    print(f"ip_{ip}\t1")