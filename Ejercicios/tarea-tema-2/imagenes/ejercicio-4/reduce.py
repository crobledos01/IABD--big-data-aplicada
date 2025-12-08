import sys

wordcount = {}
users = {}
lens = {"len_corta": 0, "len_media": 0, "len_larga": 0}
total_comentarios = 0

for line in sys.stdin:
    key, val = line.strip().split("\t")
    val = int(val)

    if key.startswith("word_"):
        w = key[5:]
        wordcount[w] = wordcount.get(w, 0) + val

    elif key.startswith("user_"):
        u = key[5:]
        users[u] = users.get(u, 0) + val

    elif key in lens:
        lens[key] += val

    elif key == "comentarios":
        total_comentarios += val

print("---- Número total de comentarios ----")
print(total_comentarios)

print("\n---- Clasificación por longitud ----")
for k, v in lens.items():
    print(k, v)

print("\n---- Top 10 palabras ----")
for w, c in sorted(wordcount.items(), key=lambda x: x[1], reverse=True)[:10]:
    print(w, c)

print("\n---- Ranking de usuarios más activos ----")
for u, c in sorted(users.items(), key=lambda x: x[1], reverse=True):
    print(u, c)
