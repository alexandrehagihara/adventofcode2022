import os
f = open(f"{os.path.dirname(__file__)}/input05.txt", "r")

# Entrada manual
stacks = {}
stacks[1] = "HCR"
stacks[2] = "BJHLSF"
stacks[3] = "RMDHJTQ"
stacks[4] = "SGRHZBJ"
stacks[5] = "RPFZTDCB"
stacks[6] = "THCG"
stacks[7] = "SNVZBPWL"
stacks[8] = "RJQGC"
stacks[9] = "LDTRHPFS"

# Descartando as 10 primeiras linhas porque entramos diretamente os valores nas pilhas via código
for i in range(10):
    f.readline()

# Varre cada comand
for line in f.readlines():
    # Separação por espaços "move x from y to z"
    tokens = line.split()
    moves = int(tokens[1])
    i_from = int(tokens[3])
    i_to = int(tokens[5])
    # Pequena garantia caso venha linhas que movem de uma pilha para ela mesma
    if i_from != i_to:
        # Extraindo os {moves} últimos itens da origem
        to_move = stacks[i_from][-moves:]
        # Deixando o restante
        new_from = stacks[i_from][:-moves]
        # Adicionando no destino sem inverter a ordem
        new_to = stacks[i_to] + to_move
        # Atualizando pilhas
        stacks[i_from] = new_from
        stacks[i_to] = new_to

#print(stacks)
for i in range(1,10):
    print(f"{stacks[i][-1:]}",end='')
print()
