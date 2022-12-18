# Input data
import os
with open(f"{os.path.dirname(__file__)}/input17.txt", "r") as f:
    commands = f.readline().strip()

# Example
# commands = ">>><<><>><<<>><>>><<<>>><<<><<<>><>><<>>"

# Vamos definir os formatos das rochas como números em formato binário, já com a posição inicial deslocada em 2 pra direita
rocks = [
    [0b0011110], # -
    [0b0001000, 0b0011100, 0b0001000], # +
    [0b0011100, 0b0000100, 0b0000100], # _|
    [0b0010000, 0b0010000, 0b0010000, 0b0010000], # |
    [0b0011000, 0b0011000] # #
]

# Iniciamos o ponto mais alto da torre em altitude zero
highest = 0
last_highest = 0
# Primeiro comando será o de índice 0
index_command = 0
index_rock = 0

# Criando torre inicial
tower = [0b0000000, 0b0000000, 0b0000000]

max_total_fallen = 0
last_high_check = 0
last_r_check = 0
# Só vamos avaliar até a 2022ª rocha
for r in range(20220):
    # Capando a torre
    tower = tower[:highest+3]

    # Seleciona a rocha atual (faz uma cópia)
    current_rock = rocks[index_rock][:]
    index_rock = (index_rock + 1) % len(rocks)

    # Amplia a torre apenas até o limite da rocha atual
    for c in current_rock:
        tower.append(0b0000000)

    # Agora vamos fazer a física da queda da rocha
    total_fallen = 0
    while(True):
        # Lendo qual vai ser o tipo de movimentação
        current_command = commands[index_command]
        index_command = (index_command+1) % len(commands)

        # Usando este trecho para encontrar onde é o ciclo. Com isso, vi que podemos definir um ciclo a cada 1.720 rochas,
        # a partir da 1.729ª rocha e que esse ciclo gera envolve uma diferença de altitude de 2.738 a partir da altitude 2.773.
        # Isso significa que podemos encontrar a altitude quando vierem 1.000.000.000.000 rochas:
        # 1.000.000.000.000 - 1.729 = 999.999.998.271 rochas
        # 999.999.998.271 dividido por 1.720 = 581.395.347, resto 1431
        # Assim, temos que a altitude será de 2.773 + 2.738 * 581.395.347 + (altitude relativa a 1431 rochas = 2.251)
        # Resultado: 1.591.860.465.110
        if( index_command == 0 and index_rock == 0 ):
            print("Checkpoint: ", r, last_high_check, highest)
            print(tower[last_high_check:highest][:])
            last_high_check = highest
            last_r_check = r

        # Este trecho foi colocado depois para calcular a altura relativa às 1.431 rochas
        if( highest > 2773 and r - last_r_check == 1431):
            print("Height 1431:", highest, highest-last_high_check)

        

        # Movimenta se for possível (apenas levando em conta as paredes da torre)
        shift_rock = current_rock[:]
        if( current_command == '>'):
            shift_allowed = True
            for c in current_rock:
                if( c & 0b0000001 ):
                    shift_allowed = False
            if( shift_allowed ):
                shift_rock = [c >> 1 for c in current_rock]
        else:
            shift_allowed = True
            for c in current_rock:
                if( c & 0b1000000 ):
                    shift_allowed = False
            if( shift_allowed ):
                shift_rock = [c << 1 for c in current_rock]

        # Agora avalia se é possível fazer o deslocamento levando em conta as posições já ocupadas
        for l in range(len(current_rock)):
            # Opa, deu colisão de alguma parte, não pode deslocar
            if( tower[highest+3-total_fallen+l] & shift_rock[l] ):
                shift_rock = current_rock
                break
        
        current_rock = shift_rock

        # Vamos avaliar agora se vai acontecer alguma colisão ao descer
        fall_allowed = True
        for l in range(len(shift_rock)):
            # Opa, deu colisão com a linha de baixo, não pode descer
            if( (total_fallen >= highest+3) or (tower[highest+2-total_fallen+l] & shift_rock[l])):
                fall_allowed = False
                break
        # Se dá para descer...
        if( fall_allowed ):
            total_fallen += 1
        # Caso contrário, ocupa as posições atuais
        else:
            this_highest = highest + 3 - total_fallen + len(shift_rock)
            for l in range( len(shift_rock) ):
                tower[highest+3-total_fallen+l] |= shift_rock[l]
            if this_highest > highest:
                highest = this_highest
            break
        
print(highest)
# print(tower)

