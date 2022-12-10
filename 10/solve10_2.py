import os
#f = open(f"{os.path.dirname(__file__)}/example10.txt", "r")
f = open(f"{os.path.dirname(__file__)}/input10.txt", "r")

# Valores iniciais
cycles = 0
sprite = 0b111000 # Usando um artifício para lidar com shifts que fazem x negativo
# Limpando a linha
crt_line = ['.' for _ in range(40)]
for l in f.readlines():
    operation = l.split()
    if operation[0] == "noop":
        # Faz a verificação se o pixel atual está dentro da janela de sprites
        if(sprite & (1<<(cycles+3))):
            crt_line[cycles] = "#"
        cycles += 1
    elif operation[0] == "addx":
        # Faz a verificação se o pixel atual está dentro da janela de sprites
        if(sprite & (1<<(cycles+3))):
            crt_line[cycles] = "#"
        cycles += 1
        # Pode ter terminado a linha no meio do ciclo...
        if( cycles >= 40 ):
            print(''.join(crt_line))
            crt_line = ['.' for _ in range(40)]
            cycles = 0
        # Faz a verificação se o pixel atual está dentro da janela de sprites
        if(sprite & (1<<(cycles+3))):
            crt_line[cycles] = "#"
        cycles += 1
        # Atualiza posição do sprite
        shifts = int(operation[1])
        if( shifts >= 0 ):
            sprite = sprite << shifts
        else:
            sprite = sprite >> -shifts
    # Terminou linha no final deste ciclo?
    if( cycles >= 40 ):
        print(''.join(crt_line))
        crt_line = ['.' for _ in range(40)]
        cycles = 0

# print(bin(sprite)) # Conferindo valor final do sprite

    