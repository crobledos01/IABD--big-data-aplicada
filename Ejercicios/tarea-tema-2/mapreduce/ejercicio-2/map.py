import sys

for line in sys.stdin:
    words = line.split()
    print(f"lineas\t1")
    print(f"palabras\t{len(words)}")
    if words:
        max_word = max(words, key=len)
        print(f"maxword\t{max_word}:{len(max_word)}")