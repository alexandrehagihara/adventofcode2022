import os
f = open(f"{os.path.dirname(__file__)}/input22.txt", "r")

# Estratégia: criar um dicionário cuja chave é um par ordenado de coordenadas (x,y) e o valor é um conjunto de 4 pares ordenados (x,y) com as coordenadas dos vizinhos
# de cima, baixo, esquerda e direita.
# Quando existe uma parede '#' em alguma direção, o vizinho é ele mesmo.
# Ao popular a lista, se uma posição não tiver vizinhos, ele pode não ser utilizada
# Pensar em como fazer o 'warping' deste mapa estilo pac-man
# Com isso, podemos ir movendo em qualquer direção simplesmente saltando para a próxima coordenada usando ela como chave
# Existem 13510 elementos tipo '.' no arquivo de entrada, esse é o nosso caso limite de entradas no dicionário