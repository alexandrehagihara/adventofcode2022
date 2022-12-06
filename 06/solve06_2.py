import os
f = open(f"{os.path.dirname(__file__)}/input06.txt", "r")

data = f.readline()
data = data.strip()

# Só faz sentido a partir do 14º caracter...
for i in range(13,len(data)):
    has_repeat = False
    # Tem que fazer uma varredura completa agora, não é viável escrever todas as combinações (C(14,2) = 91)
    for j in range(i-13, i):
        for k in range(j+1, i+1):
            if data[j] == data[k]:
                has_repeat = True
                break
        if has_repeat:
            break
    if not has_repeat:
        print(i+1)
        # print(data[i-13:i+1])
        break
    