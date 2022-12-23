# Estratégia:
# Cada elfo ocupa uma posição (x,y) no mapa e armazena a direção a ser proposta na segunda metade
# Em cada rodada, vai existir um mapa de intenções de ocupação, onde a chave é a posição e o valor um conjunto de elfos que propuseram ir para esta posição 
# 

import os
# f = open(f"{os.path.dirname(__file__)}/input23.txt", "r")
f = open(f"{os.path.dirname(__file__)}/example23.txt", "r")

# Cria os elfos e inicialia a primeira sugestão
elves = {}
row = 0
for line in f.readlines():
    line = line.strip()
    for col, v in enumerate(line):
        if v == '#':
            elves[(row,col)] = 'N'
    row += 1

# Vamos às 10 rodadas
for round in range(10):
    intents = {}
    for (r,c) in elves:
        if (r-1,c-1) in elves or (r-1,c) in elves or (r-1,c+1) in elves or (r,c-1) in elves or (r, c+1) in elves or (r+1,c-1) in elves or (r+1,c) in elves or (r+1,c+1) in elves:
            if( elves[(r,c)] == 'N' ):
                intents[(r-1,c)] = True
            elif( elves[(r,c)] == 'N' ):
                