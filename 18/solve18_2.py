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

x = [d[0] for d in droplets]
y = [d[1] for d in droplets]
z = [d[2] for d in droplets]
print(min(x), max(x), min(y), max(y), min(z), max(z))

for xx in range(min(x)+1,max(x)):
    for yy in range(min(y)+1,max(y)):
        for zz in range(min(z)+1,max(z)):
            # Verifica se é um cubo vazio
            if not [xx,yy,zz] in droplets:
                # Define quais são os possíveis vizinhos
                neighbours = [
                    [xx,yy,zz+1],
                    [xx,yy,zz-1],
                    [xx,yy+1,zz],
                    [xx,yy-1,zz],
                    [xx+1,yy,zz],
                    [xx-1,yy,zz]
                ]
                total_neighbours = 0
                # Conta a quantidade de vizinhos que são cubos normais
                for n in neighbours:
                    if( n in droplets ):
                        total_neighbours += 1
                
                # Se todos os vizinhos são cubos normais, desconta 6 lados.
                # Não é só isso, já que a minha resposta 3250 não deu certo. Temos que ver se é possível combinar cubos vazios
                if( total_neighbours == 6 ):
                    total_area -= 6

print(total_area)
    