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
        return -1
    elif( type(left) == int and type(right) == list ):
        return compare_pair([left], right)
    elif( type(left) == list and type(right) == int ):
        return compare_pair(left, [right])
    
    print("Erro ", left, right) # Não pode chegar aqui


pairs = 0
sum = 0
while True:
    # Forma super fácil de interpretar as linhas como listas
    in_left = eval(f.readline().strip())
    in_right = eval(f.readline().strip())
    pairs += 1

    print("Pair #", pairs)
    if( compare_pair(in_left, in_right) < 0 ):
        print("Left was smaller")
        sum += pairs
    else:
        print("Right was smaller")
        

    blankline = f.readline()
    if( blankline != "\n" ):
        break



print(sum)