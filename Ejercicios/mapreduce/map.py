#!/usr/bin/env python3
import sys

for line in sys.stdin:
    parts = line.strip().split()
    name = parts[0]
    for score in parts[1:]:
        int(score)
        print(f"{name}\t{score}")