import sys, string

stopwords = {"el","la","los","las","de","y","a","en","es","me","muy","lo","que","por"}

for line in sys.stdin:
    line = line.strip()

    parts = line.split(",", 1)
    if len(parts) != 2:
        continue

    usuario = parts[0].strip()
    comentario = parts[1].lower().strip()

    for p in string.punctuation:
        comentario = comentario.replace(p, " ")

    palabras = comentario.split()

    for word in palabras:
        if word not in stopwords:
            print(f"word_{word}\t1")

    print("comentarios\t1")

    n = len(palabras)
    if n < 5:
        print("len_corta\t1")
    elif n < 12:
        print("len_media\t1")
    else:
        print("len_larga\t1")

    print(f"user_{usuario}\t1")
