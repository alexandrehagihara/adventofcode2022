import os
# f = open(f"{os.path.dirname(__file__)}/example13.txt", "r")
f = open(f"{os.path.dirname(__file__)}/input13.txt", "r")

def compare_pair(left, right):
    print("Compare ", left, " vs ", right)
    if( type(left) is int and type(right) is int ):
        return left - right
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


index = 0
sum = 0
while True:
    # Forma super fácil de interpretar as linhas como listas
    in_left = eval(f.readline().strip())
    in_right = eval(f.readline().strip())
    index += 1

    print("Pair #", index)
    # Somando os índices quando o pacote da esquerda é o correto
    if( compare_pair(in_left, in_right) < 0 ):
        print("Left was smaller")
        sum += index
    else:
        print("Right was smaller")
        

    blankline = f.readline()
    if( blankline != "\n" ):
        break



print(sum)