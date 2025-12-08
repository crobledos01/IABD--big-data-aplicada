import sys

total_lineas = 0
total_palabras = 0
max_word = ""
max_len = 0

for line in sys.stdin:
    key, val = line.strip().split("\t")

    if key == "lineas":
        total_lineas += int(val)

    elif key == "palabras":
        total_palabras += int(val)

    elif key == "max_word":
        palabra, length = val.split(":")
        length = int(length)
        if length > max_len:
            max_len = length
            max_word = palabra

print(f"Lineas totales: {total_lineas}")
print(f"Palabras totales: {total_palabras}")
print(f"Palabra más larga: {max_word}({max_len})")
print(f"Media palabras/linea: {total_palabras/total_lineas:2f}")