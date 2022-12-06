import os
f = open(f"{os.path.dirname(__file__)}/input06.txt", "r")

data = f.readline()
data = data.strip()

# Só faz sentido a partir do 4º caracter...
for i in range(3,len(data)):
    # Se todos os 4 últimos forem diferentes...
    if not ( data[i-3] == data[i-2] or data[i-3] == data[i-1] or data[i-3] == data[i] or data[i-2] == data[i-1] or data[i-2] == data[i] or data[i-1] == data[i]):
        # Imprime o índice + 1, representando a quantidade de caracteres lidos até aqui
        print(i+1)
        break