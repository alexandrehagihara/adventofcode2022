f = open("input03.txt", "r")

# Lista de caracteres em posição de prioridade
priorities = " abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

sum = 0
# Lendo cada mochila
for line in f.readlines():
    line = line.replace("\n", "")
    # Dividindo em 2 compartimentos
    llen = len(line)//2
    # print(llen)
    half1 = line[:llen]
    half2 = line[llen:]
    # Varrendo cada item do 1º compartimento
    for c in half1:
        # Se tem no 2º compartimento, acumula a prioridade
        if( c in half2 ):
            #print(f"{c}: {priorities.index(c)}")
            sum += priorities.index(c)
            break
    #print("-")

print(f"{sum}")