import os
#f = open(f"{os.path.dirname(__file__)}/example09.txt", "r")
f = open(f"{os.path.dirname(__file__)}/input09.txt", "r")

# Posições atuais. Agora vamos chamar tudo de nó mesmo.
x = [0 for i in range(10)]
y = [0 for i in range(10)]

# Mapa em que as chaves são as coordenadas visitadas pelo último nó (cauda)
visited = {}
visited[(x[9],y[9])] = 1

def propagate_movement():
    # Agora vamos avaliar o restante, mas ó faz se houve uma movimentação entre os 2 últimos nós
    for i in range(1,10):
        diffy = y[i-1]-y[i]
        diffx = x[i-1]-x[i]
        if( diffy > 1 ):
            # Movimento diagonal se necessário
            if( diffx > 0 ):
                x[i] += 1
            elif( diffx < 0 ):
                x[i] -= 1
            # Subindo o nó
            y[i] += 1
        elif( diffy < -1 ):
            # Movimento diagonal se necessário
            if( diffx > 0 ):
                x[i] += 1
            elif( diffx < 0 ):
                x[i] -= 1
            # Descendo o nó
            y[i] -= 1
        elif( diffx > 1 ):
            # Movimento diagonal se necessário
            if( diffy > 0 ):
                y[i] += 1
            elif( diffy < 0 ):
                y[i] -= 1
            # Movendo nó para direita
            x[i] += 1
        elif( diffx < -1 ):
            # Movimento diagonal se necessário
            if( diffy > 0 ):
                y[i] += 1
            elif( diffy < 0 ):
                y[i] -= 1
            # Movendo nó para esquerda
            x[i] -= 1

for line in f.readlines():
    movement,steps = line.split()
    steps = int(steps)
    # Subindo...
    if movement == "U":
        for s in range(steps):
            # Sobe a cabeça
            y[0] -= 1
            propagate_movement()
            # Marca posição do último nó, se não estava marcada antes
            visited[(x[9],y[9])] = 1
    # Descendo
    elif movement == "D":
        for s in range(steps):
            # Desce a cabeça
            y[0] += 1
            propagate_movement()
            # Marca posição do último nó, se não estava marcada antes
            visited[(x[9],y[9])] = 1
    # Indo pra esquerda
    elif movement == "L":
        for s in range(steps):
            # Movimenta a cabeça pra esquerda
            x[0] -= 1
            propagate_movement()
            # Marca posição do último nó, se não estava marcada antes
            visited[(x[9],y[9])] = 1
    # Indo pra direita
    elif movement == "R":
        for s in range(steps):
            # Movimenta a cabeça pra direita
            x[0] += 1
            propagate_movement()
            # Marca posição do último nó, se não estava marcada antes
            visited[(x[9],y[9])] = 1

# Agora é só imprimir a quantidade de posições visitadas
print(len(visited))
# print([k for k in zip(x,y)])