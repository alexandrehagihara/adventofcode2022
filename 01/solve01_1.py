# Aqui a idéia é pegar a lista de cada Elfo, somar as calorias e armazenar a maior soma de todos

f = open("input1.txt", "r")

total = 0
greatest = 0
# Varrendo as linhas
for line in f.readlines():
    line = line.replace("\n", "")
    # Linha não vazia é quantidade de calorias do elfo atual
    if len(line) > 0:
        value = int(line)
        total += value
    # Linha vazia é separador de listas de um elfo
    else:
        # Agora avalia a quantidade de calorias acumuladas
        if total > greatest:
            greatest = total
        total = 0

if total > greatest:
    greatest = total

print(f"{greatest}")