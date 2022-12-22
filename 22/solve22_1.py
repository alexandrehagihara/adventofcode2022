import os
# f = open(f"{os.path.dirname(__file__)}/input22.txt", "r")
f = open(f"{os.path.dirname(__file__)}/example22.txt", "r")

# Estratégia: criar um dicionário cuja chave é um par ordenado de coordenadas (x,y) e o valor é um conjunto de 4 pares ordenados (x,y) com as coordenadas dos vizinhos
# de cima, baixo, esquerda e direita.
# Quando existe uma parede '#' em alguma direção, o vizinho é ele mesmo.
# Ao popular a lista, se uma posição não tiver vizinhos, ele pode não ser utilizada
# Pensar em como fazer o 'warping' deste mapa estilo pac-man
# Com isso, podemos ir movendo em qualquer direção simplesmente saltando para a próxima coordenada usando ela como chave
# Existem 13510 elementos tipo '.' no arquivo de entrada, esse é o nosso caso limite de entradas no dicionário
fullmap = {} # Mapa completo, sem distinção de espaços andáveis ou paredes
rows = 0
cols = 0
initpos = None
for l in f.readlines():
    l = l.rstrip()
    if( '.' in l ):
        for col, v in enumerate(l):
            if( v == "." or v == '#' ):
                fullmap[(rows,col)] = v
                # leftmost open tile
                if( initpos is None and v == '.'):
                    initpos = (rows, col)
        rows = rows + 1
        cols = max(cols, len(l))
    elif len(l) > 0:
        path = l

walkablemap = {}
for (row,col) in fullmap:
    v = fullmap[(row,col)]
    if( v == '.' ):
        # Procura a coordenada de cima, de baixo, da esquerda e da direita. Aqui também é feito o warping.
        u = 1
        while( not ((row - u + rows) % rows,col) in fullmap ):
            u += 1
        up = ((row - u + rows) % rows, col)
        d = 1
        while( not ((row + d) % rows,col) in fullmap ):
            d += 1
        down = ((row + d) % rows, col)
        l = 1
        while( not (row, (col - l + cols) % cols) in fullmap ):
            l += 1
        left = (row, (col - l + cols) % cols)
        r = 1
        while( not (row, (col + r) % cols) in fullmap ):
            r += 1
        right = (row, (col + r) % cols)
        
        # Se tiver uma parede, não dá para movimentar para lá, logo a próxima posição é a atual mesmo
        if( fullmap[up] == '#' ):
            up = (row, col)
        if( fullmap[down] == '#' ):
            down = (row, col)
        if( fullmap[left] == '#' ):
            left = (row, col)
        if( fullmap[right] == '#' ):
            right = (row, col)
        
        walkablemap[(row,col)] = [right, down, left, up]

print(len(walkablemap)) # precisa ser 13510

direction = 0 # right
pos = initpos

walked = True
to_walk = 0
for v in path:
    if( v in ['0','1','2','3','4','5','6','7','8','9']):
        to_walk = 10*to_walk + int(v)
    else:
        for _ in range(to_walk):
            pos = walkablemap[pos][direction]
        if v == 'R':
            direction = (direction + 1) % 4
            to_walk = 0
        elif v == 'L':
            direction = (direction - 1 + 4) % 4
            to_walk = 0        

for _ in range(to_walk):
    pos = walkablemap[pos][direction]

print(pos, direction)
print((pos[0] + 1) * 1000 + (pos[1]+1)*4 + direction)
