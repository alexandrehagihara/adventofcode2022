import os
# f = open(f"{os.path.dirname(__file__)}/example24.txt", "r")
f = open(f"{os.path.dirname(__file__)}/input24.txt", "r")

left = []
right = []
up = []
down = []
free = []
pos = (0,1)

row = 0
for l in f.readlines():
    for col, v in enumerate(l.strip()):
        if( v == '<' ):
            left.append((row,col))
        elif( v == '>'):
            right.append((row,col))
        elif( v == '^'):
            up.append((row,col))
        elif( v == 'v'):
            down.append((row,col))
        elif( v == '.'):
            free.append((row,col))
    row += 1

# Análise:
# Existem 36 linhas e 100 colunas, logo 3600 posições
# Mas os blizzards estão sempre seguindo, eles irão repetir um ciclo a cada MMC(36,100) = 900 passos
# A quantidade de posições livres inicial de blizzards é de 348
# Podemos pensar em todos os casos da linha 1 em que há um buraco e a partir daí verificar quantas rotas viáveis
# podem existir levando em conta as movimentações dos blizzards

# Outra forma a se pensar é criar uma matriz tridimensional com 36x100x900 = 3240000 pontos em que procuraremos uma rota desde o ponto (1,1,X) até o ponto (36,100,Y)
# Ao fazer a contagem, vi que existem cerca de 1300~1400 pontos vazios por ciclo, ou seja, menos de 1260000 pontos vazios, sendo que entre pontos de 3ª
# coordenada diferentes, podem existir até 5 conexões possíveis (cima, baixo, esquerda, direita, parado)
count11 = 0
for step in range(900):
    prohibited = {}
    # Movimenta todos os blizzards
    for p, (r,c) in enumerate(left):
        left[p] = (r, c - 1 if c > 1 else 100)
        prohibited[left[p]] = 1
    for p, (r,c) in enumerate(right):
        right[p] = (r, c + 1 if c < 100 else 1)
        prohibited[right[p]] = 1
    for p, (r,c) in enumerate(up):
        up[p] = (r-1 if r > 1 else 36, c)
        prohibited[up[p]] = 1
    for p, (r,c) in enumerate(down):
        down[p] = (r+1 if r < 36 else 1, c)
        prohibited[down[p]] = 1
    # print(f"step: {step}, pos: {36*100-len(prohibited)}")
    if( not (1,1) in prohibited ):
        count11 += 1

print(count11)