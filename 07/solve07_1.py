import os
f = open(f"{os.path.dirname(__file__)}/input07.txt", "r")

dir_list = {}
# Cada diretório é um list com os seguintes valores:
# [caminho_anterior, tamanho]
current_dir = "/"
dir_list[current_dir] = ["/", 0] # A chave é o caminho atual

for line in f.readlines():
    line = line.strip()
    tokens = line.split()
    # print(tokens)
    # Se é um comando...
    if tokens[0] == "$":
        # Listar diretorio atual
        if tokens[1] == "ls":
            listing = True
        # Trocar diretório atual
        elif tokens[1] == "cd":
            # Ir para raiz
            if tokens[2] == "/":
                current_dir = "/"
            # Ir para um diretório acima
            elif tokens[2] == "..":
                # Contabiliando o tamanho do diretório atual
                d_size = dir_list[current_dir][1]
                # Trocando de diretório
                current_dir = dir_list[current_dir][0]
                # Atualizando o novo diretório com o tamanho do diretório anterior
                dir_list[current_dir][1] += d_size
            # Ir para um diretório abaixo
            else:
                # Trocando para novo caminho
                current_dir = current_dir + tokens[2] + "/"

    # Se não é comando e estávamos listando (o que é o mais provável de acontecer mesmo...)
    elif listing:
        # Se é um diretório...
        if tokens[0] == "dir":
            # Montando novo caminho
            new_dir = current_dir + tokens[1] + "/"
            # Criando diretório vazio caso não exista
            if not new_dir in dir_list:
                dir_list[new_dir] = [current_dir, 0]
        # Se é um arquivo...
        else:
            # Extraindo tamanho do arquivo
            f_size = int(tokens[0])
            # Acrescentando o tamanho do arquivo no diretório atual
            dir_list[current_dir][1] += f_size

# Agora retornaremos até o diretório raiz de forma suave, emulando vários "cd .."
while current_dir != "/":
    # Contabiliando o tamanho do diretório atual
    d_size = dir_list[current_dir][1]
    # Trocando de diretório
    current_dir = dir_list[current_dir][0]
    # Atualizando o novo diretório com o tamanho do diretório anterior
    dir_list[current_dir][1] += d_size

total = 0
for i in dir_list:
    #print(i, dir_list[i])
    if( dir_list[i][1] <= 100000 ):
        total += dir_list[i][1]

print(total)