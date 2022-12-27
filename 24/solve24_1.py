import os
# f = open(f"{os.path.dirname(__file__)}/example24.txt", "r")
f = open(f"{os.path.dirname(__file__)}/input24.txt", "r")

left = []
right = []
up = []
down = []
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
    
while( True ):
    # Movimenta todos os blizzards
    for p, (r,c) in enumerate(left):
        left[p] = (r, c - 1 if c > 1 else 100)
    for p, (r,c) in enumerate(right):
        right[p] = (r, c + 1 if c < 100 else 1)
    for p, (r,c) in enumerate(up):
        right[p] = (r-1 if r > 1 else 36, c)
    for p, (r,c) in enumerate(down):
        right[p] = (r+1 if r < 36 else 1, c)
    
    