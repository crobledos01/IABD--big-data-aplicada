import sys, string

stopwords = {"el", "la", "los", "las", "de", "y", "a", "en", "es"}

for line in sys.stdin:
    line = line.lower()
    for p in string.punctuation:
        line= line.replace(p, " ")

    for word in line.split():
        if word not in stopwords:
            print(f"{word}\t1")