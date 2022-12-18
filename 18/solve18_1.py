import os
f = open(f"{os.path.dirname(__file__)}/input18.txt", "r")

droplets = []

for line in f.readlines():
    droplets.append([int(c) for c in line.strip().split(",")])

# Esta é a área inicial, sem considerar as áreas desconsideradas por estarem em contato
total_area = 6*len(droplets)

# Agora pega cada "gota"
for d in droplets:
    # Define quais são os possíveis vizinhos
    neighbours = [
        [d[0],d[1],d[2]+1],
        [d[0],d[1],d[2]-1],
        [d[0],d[1]+1,d[2]],
        [d[0],d[1]-1,d[2]],
        [d[0]+1,d[1],d[2]],
        [d[0]-1,d[1],d[2]]
    ]
    # Remove 1 lado para cada vizinho
    for n in neighbours:
        if( n in droplets ):
            total_area -= 1

print(total_area)
    