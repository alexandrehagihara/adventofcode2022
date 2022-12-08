import os
#f = open(f"{os.path.dirname(__file__)}/example08.txt", "r")
f = open(f"{os.path.dirname(__file__)}/input08.txt", "r")

lines = f.readlines()

total_trees = len(lines) * (len(lines[0])-1)
total_visibles = total_trees - ((len(lines)-2) * (len(lines[0])-3))
#print(total_visibles)
for r in range(1,len(lines)-1):
    for c in range(1,len(lines[r])-2):
        #print(lines[r][c])
        # Testando todos os da esquerda
        left_ok = True
        for cc in range(c-1,-1,-1):
            if(lines[r][cc] >= lines[r][c]):
                left_ok = False
                break
        if left_ok:
            total_visibles += 1
            continue
        # Testando todos os da direita
        right_ok = True
        for cc in range(c+1,len(lines[r])-1):
            if(lines[r][cc] >= lines[r][c]):
                right_ok = False
                break
        if right_ok:
            total_visibles += 1
            continue
        # Testando todos os de cima
        up_ok = True
        for rr in range(r-1,-1,-1):
            if(lines[rr][c] >= lines[r][c]):
                up_ok = False
                break
        if up_ok:
            total_visibles += 1
            continue
        # Testando todos os de baixo
        down_ok = True
        for rr in range(r+1,len(lines)):
            if(lines[rr][c] >= lines[r][c]):
                down_ok = False
                break
        if down_ok:
            total_visibles += 1
            continue
print(total_visibles)