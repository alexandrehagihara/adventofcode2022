import os
#f = open(f"{os.path.dirname(__file__)}/example08.txt", "r")
f = open(f"{os.path.dirname(__file__)}/input08.txt", "r")

lines = f.readlines()

total_trees = len(lines) * (len(lines[0])-1)
total_visibles = total_trees - ((len(lines)-2) * (len(lines[0])-3))
highest_score = 0
for r in range(1,len(lines)-1):
    for c in range(1,len(lines[r])-2):
        score_left = 0
        # Testando todos os da esquerda, até achar alguma árvore mais alta ou igualmente alta
        for cc in range(c-1,-1,-1):
            score_left += 1
            if(lines[r][cc] >= lines[r][c]):
                break
        score_right = 0
        # Testando todos os da direita, até achar alguma árvore mais alta ou igualmente alta
        for cc in range(c+1,len(lines[r])-1):
            score_right += 1
            if(lines[r][cc] >= lines[r][c]):
                break
        score_up = 0
        # Testando todos os de cima, até achar alguma árvore mais alta ou igualmente alta
        for rr in range(r-1,-1,-1):
            score_up += 1
            if(lines[rr][c] >= lines[r][c]):
                break
        score_down = 0
        # Testando todos os de baixo, até achar alguma árvore mais alta ou igualmente alta
        if( r < len(lines)-1):
            for rr in range(r+1,len(lines)):
                score_down += 1
                if(lines[rr][c] >= lines[r][c]):
                    break
        score = score_left*score_right*score_up*score_down
        if score > highest_score:
            highest_score = score
print(highest_score)