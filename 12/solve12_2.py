import os
# f = open(f"{os.path.dirname(__file__)}/example12.txt", "r")
f = open(f"{os.path.dirname(__file__)}/input12.txt", "r")

# Transformando as strings em números (a-z) -> (1-26)
data = []
for line in f.readlines():
    data_line = [ord(v)-ord('a')+1 for v in line.replace("\n","")]
    data.append(data_line)

nrows = len(data)
ncols = len(data[0])

# print(data) # Conferência

# Localizando os pontos de início (S) e de fim (E)
S = ord('S') - ord('a') + 1
E = ord('E') - ord('a') + 1
start_node = None
end_node = None
for r in range(nrows):
    for c in range(ncols):
        if start_node == None and data[r][c] == S:
            start_node = (r,c)
            data[r][c] = 1
        if end_node == None and data[r][c] == E:
            end_node = (r,c)
            data[r][c] = 26
    # Achou os 2? Sai do loop.
    if start_node != None and end_node != None:
        break

# print(start_node, end_node)

# Cada valor da matriz data é uma altitude absoluta que vai de 1 a 26. A gente vai criar agora uma lista
# de caminhos possíveis entre cada nó, a depender da diferença de alturas.
neighbour_set = {}
for r in range(nrows):
    for c in range(ncols):
        # Lista de vizinhos do nó atual inicialmente vazia. Só considera que existe um caminho quando
        # a altitude é no máximo 1 unidade acima da altitude atual
        neighbours = []
        max_height = data[r][c] + 1
        if( (r,c) != end_node ):
            if r > 0 and data[r-1][c] <= max_height:
                neighbours.append((r-1,c,1))
            if c > 0 and data[r][c-1] <= max_height:
                neighbours.append((r,c-1,1))
            if r < (nrows-1) and data[r+1][c] <= max_height:
                neighbours.append((r+1,c,1))
            if c < (ncols-1) and data[r][c+1] <= max_height:
                neighbours.append((r,c+1,1))
             
        neighbour_set[(r,c)] = neighbours
        


# O que entendo do algoritmo:
# A gente parte do nó de origem e calcula o custo para ir para os nós vizinhos
# Colocamos esses nóz vizinhos na lista de "a visitar"
# Avaliamos sempre os nós da lista "a visitar" daquele com menor custo até o de maior custo
# Quando um nó vai adicionar outro na lista de "a visitar", se este nó já está na lista de "a visitar",
# avalia se o custo passando pelo nó atual será menor, e caso positivo, substitui na lista de "a visitar"

# O primeiro ponto a ser visitado é o ponto inicial, mas agora vamos variar este ponto inicial

shortest_path = nrows*ncols
for r in range(nrows):
    # Observando meu conjunto de dados, existem letras 'b' somente na segunda coluna, então só faz
    # sentido testarmos posição inicial a partir de todos os valores iniciando na primeira coluna
    new_start_node = (r,0)
    visited_set = {}
    tovisit_set = {new_start_node:[None,0]}
    # O critério de parada é quando terminamos todos os nós
    while(len(visited_set) < nrows*ncols):
        # Vamos pegar o nó com menor custo da lista de "a visitar"
        current_node = None
        for tv in tovisit_set:
            if( current_node == None or tovisit_set[tv][1] < tovisit_set[current_node][1] ):
                current_node = tv

        # Agora usa ele para adicionar os vizinhos dele na lista de "a visitar"
        neighbors = neighbour_set[current_node]
        current_cost = tovisit_set[current_node][1]
        for n in neighbors:
            node = (n[0],n[1])
            cost = n[2] + current_cost
            tovisit = [node, cost]
            # Não pode revisitar um nó já visitado
            if( not node in visited_set ):
                # Se o vizinho não estava na lista de "a visitar", adiciona agora
                if( not node in tovisit_set ):
                    tovisit_set[node] = tovisit
                # Se ele estava na lista de "a visitar", apenas substitui se o custo vindo pelo atual é menor
                else:
                    if( cost < tovisit_set[node][1] ):
                        tovisit_set[node] = tovisit
            
        # Agora tira o nó atual da lista de "a visitar" e coloca na lista de "visitados"
        visited_set[current_node] = tovisit_set[current_node]
        tovisit_set.pop(current_node)
        
        # Não precisa fazer mais caminhos quando chegamos no ponto final
        if( current_node == end_node ):
            break
        
    # Dá pra ver a lista completa agora 
    # for v in visited_set:
    #     print(v, visited_set[v])
        
    # Mas só estamos interessados no último deles
    print(new_start_node, visited_set[end_node][1])

    if( visited_set[end_node][1] < shortest_path ):
        shortest_path = visited_set[end_node][1]

print(shortest_path)