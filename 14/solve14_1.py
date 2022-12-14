import os
# f = open(f"{os.path.dirname(__file__)}/example14.txt", "r")
f = open(f"{os.path.dirname(__file__)}/input14.txt", "r")

cavemap = {}
maxy = 0 # Usamos esta informação para saber quando termina o chão e começa o abismo
 
# Vamos popular o mapa da caverna com as linhas
for line in f.readlines():
    steps = line.strip().split("->")
    (x1,y1) = [int(c) for c in steps[0].split(",")]
    maxy = max(maxy, y1)
    for s in steps[1:]:
        (x2,y2) = [int(c) for c in s.split(",")]
        maxy = max(maxy, y2)
        if( x1 == x2 ):
            starty = min(y1,y2)
            endy = max(y1,y2)
            for y in range(starty, endy+1):
                cavemap[(x1, y)] = "#"
        elif( y1 == y2 ):
            startx = min(x1,x2)
            endx = max(x1,x2)
            for x in range(startx, endx+1):
                cavemap[(x, y1)] = "#"
        else:
            print(x1,y1,x2,y2)
        (x1,y1) = (x2,y2)

count_sands = 0
# Não sabemos quantos grãos teremos, vai iterando...
while(True):
    # Posição inicial do grão de areia
    sx,sy = (500,0)
    # Vai simulando a queda deste grão
    while(True):
        # Se na posição abaixo não existe nada, desce uma posição
        if( not (sx, sy+1) in cavemap ):
            sy = sy+1
        # Testando diagonal pra esquerda...
        elif( not (sx-1, sy+1) in cavemap ):
            (sx,sy) = (sx-1,sy+1)
        # Testando diagonal pra direita...
        elif( not (sx+1, sy+1) in cavemap ):
            (sx,sy) = (sx+1,sy+1)
        # OK, não tem como descer mais. Coloca o grão aqui.
        else:
            cavemap[(sx,sy)] = "o"
            count_sands += 1
            break
        # Se caiu no abismo...
        if( sy >= maxy ):
            break
    # Se último grão caiu no abismo
    if( sy >= maxy ):
        break

print(count_sands)        