import os
f = open(f"{os.path.dirname(__file__)}/input03.txt", "r")

# Lista de caracteres em posição de prioridade
priorities = " abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

sum = 0
# Lendo cada 3 mochilas
lines = f.readlines()
for i in range(len(lines)//3):
    rucksack1 = lines[3*i].replace("\n","")
    rucksack2 = lines[3*i+1].replace("\n","")
    rucksack3 = lines[3*i+2].replace("\n","")
    # Varre cada item da mochila 1
    for c in rucksack1:
        # Se tem nas outras 2 mochilas, acumula a prioridade
        if( c in rucksack2 and c in rucksack3 ):
            #print(f"{c}: {priorities.index(c)}")
            sum += priorities.index(c)
            break
            
    #print("-")

print(f"{sum}")