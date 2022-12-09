import os
#f = open(f"{os.path.dirname(__file__)}/example09.txt", "r")
f = open(f"{os.path.dirname(__file__)}/input09.txt", "r")

# Posições atuais
xh,yh = 0,0
xt,yt = 0,0

# Mapa em que as chaves são as coordenadas visitadas pela cauda
visited = {}
visited[(xt,yt)] = 1

for line in f.readlines():
    movement,steps = line.split()
    steps = int(steps)
    # Subindo...
    if movement == "U":
        for s in range(steps):
            # Sobe a cabeça
            yh -= 1
            # Opa, deu diferença aqui
            if( abs(yh-yt) > 1 ):
                # Movimento diagonal se necessário
                if( xh != xt ):
                    xt = xh
                # Subindo a cauda
                yt -= 1
                # Marca posição, se não estava marcada antes
                visited[(xt,yt)] = 1
    # Descendo
    elif movement == "D":
        for s in range(steps):
            # Desce a cabeça
            yh += 1
            # Opa, deu diferença aqui
            if( abs(yh-yt) > 1 ):
                # Movimento diagonal se necessário
                if( xh != xt ):
                    xt = xh
                # Descendo a cauda
                yt += 1
                # Marca posição, se não estava marcada antes
                visited[(xt,yt)] = 1
    # Indo pra esquerda
    elif movement == "L":
        for s in range(steps):
            # Movimenta a cabeça pra esquerda
            xh -= 1
            # Opa, deu diferença aqui
            if( abs(xh-xt) > 1 ):
                # Movimento diagonal se necessário
                if( yh != yt ):
                    yt = yh
                # Movimenta a cauda pra esquerda
                xt -= 1
                # Marca posição, se não estava marcada antes
                visited[(xt,yt)] = 1
    # Indo pra direita
    elif movement == "R":
        for s in range(steps):
            # Movimenta a cabeça pra direita
            xh += 1
            # Opa, deu diferença aqui
            if( abs(xh-xt) > 1 ):
                # Movimento diagonal se necessário
                if( yh != yt ):
                    yt = yh
                # Movimenta a cauda pra direita
                xt += 1
                # Marca posição, se não estava marcada antes
                visited[(xt,yt)] = 1

# Agora é só imprimir a quantidade de posições visitadas
print(len(visited))