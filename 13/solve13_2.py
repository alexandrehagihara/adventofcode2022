import os
# f = open(f"{os.path.dirname(__file__)}/example13.txt", "r")
f = open(f"{os.path.dirname(__file__)}/input13.txt", "r")

def compare_pair(left, right):
    #print("Compare ", left, " vs ", right)
    if( type(left) is int and type(right) is int ):
        return left-right
    elif( type(left) == list and type(right) == list ):
        for i in range(len(left)):
            if( i < len(right) ):
                ret = compare_pair(left[i], right[i])
                if( ret != 0 ):
                    return ret
            else:
                return +1
        # Se terminou lista, por ora está tudo igual então vamos seguir a comparação...
        if( len(left) == len(right) ):
            return 0
        else:
            return -1
    elif( type(left) == int and type(right) == list ):
        return compare_pair([left], right)
    elif( type(left) == list and type(right) == int ):
        return compare_pair(left, [right])
    
    print("Erro ", left, right) # Não pode chegar aqui


packets = []
while True:
    # Forma super fácil de interpretar as linhas como listas
    in_left = eval(f.readline().strip())
    in_right = eval(f.readline().strip())
    # Simplesmente adiciona na lista
    packets.append(in_left)
    packets.append(in_right)
        
    blankline = f.readline()
    if( blankline != "\n" ):
        break

# Adicionando os pacotes divisores
packets.append([[2]])
packets.append([[6]])

# Ordenando os pacotes
from functools import cmp_to_key
packets = sorted(packets,key=cmp_to_key(compare_pair))

# Procurando os índices dos 2 pacotes divisores
p2, p6 = 0, 0
for p in range(len(packets)):
    packet = packets[p]
    # print(packet)
    if( packet == [[2]] ):
        p2 = p+1
    elif (packet == [[6]]):
        p6 = p+1

print(p2*p6)
