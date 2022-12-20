# import os
# f = open(f"{os.path.dirname(__file__)}/input19.txt", "r")

# blueprints = []

# for line in f.readlines():
#     tokens = line.strip().split()
#     print(tokens)
#     blueprints.append([int(i) for i in [tokens[1][:-1],tokens[6],tokens[12],tokens[18],tokens[21],tokens[27],tokens[30]]])

# print(blueprints)

blueprints = [
    [1,4,2,3,14,2,7],
    [2,2,3,3,8,3,12]
]


# blueprint: list contendo as informação do projeto atual, lido do arquivo
# state: list contendo os seguintes valores
#        - minuto atual (vai até 24)
#        - quantidade de ores totais
#        - quantidade de clays totais
#        - quantidade de obsidians totais
#        - quantidade de geodes totais
#        - quantidade de robôs tipo 'ore'
#        - quantidade de robôs tipo 'clay'
#        - quantidade de robôs tipo 'obsidian'
#        - quantidade de robôs tipo 'geode'
# Retorno: quantidade de geodes máximos que se conseguiu extrair em 24 minutos
# Esta função é recursiva e leva em conta aquilo que se pode fazer com o estado atual
def calculate_geodes(blueprint, state):
    # Acabou o tempo
    if( state[0] >= 24 ):
        return state[4]
    # Primeiro vamos gerar mais 1 recurso a depender da quantidade de robôs de cada tipo que temos
    copy_state = state[:]
    # Incrementa o minuto atual
    copy_state[0] += 1
    # Incrementa quantidade de ores
    copy_state[1] += copy_state[5]
    # Incrementa quantidade de clays
    copy_state[2] += copy_state[6]
    # Incrementa quantidade de obsidians
    copy_state[3] += copy_state[7]
    # Incrementa quantidade de geodes
    copy_state[4] += copy_state[8]

    result_geodes = []

    # Estratégia:
    # Ficar de olho na quantidade de clays. Se estamos longe de poder criar um obsidian robot, vai acumulando ores e gerando mais clay robots
    # Ficar de olho na quantidade de obsidians. Se estamos longe de poder criar um geode robot, vai acumulando ores e gerando mais clay robots
    # Então, a gente precisa gerar uma previsão baseada na quantidade atual de cada recurso e de cada robô.
    # Talvez seja vantajoso ao invés de gerar um clay robot, gerar mais um ore robot. Isso pode demandar abrir ramificações para ver o que vale mais a pena.
    # Acho que no blueprint 2 isso ocorre, já que o custo de um novo ore robot é menor do que um clay robot.
    
    # Quinta opção gera mais um robô tipo geode, se isso for possível
    if( copy_state[1] >= blueprint[5] and copy_state[3] >= blueprint[6] ):
        cstate = copy_state[:]
        cstate[1] -= blueprint[5]
        cstate[3] -= blueprint[6]
        cstate[8] += 1
        result_geodes.append(calculate_geodes(blueprint, cstate))
    # Quarta opção gera mais um robô tipo obsidian, se isso for possível
    if( copy_state[1] >= blueprint[3] and copy_state[2] >= blueprint[4] ):
        cstate = copy_state[:]
        cstate[1] -= blueprint[3]
        cstate[2] -= blueprint[4]
        cstate[7] += 1
        result_geodes.append(calculate_geodes(blueprint, cstate))
    # Terceira opção gera mais um robô tipo clay, se isso for possível
    if( copy_state[1] >= blueprint[2] ):
        cstate = copy_state[:]
        cstate[1] -= blueprint[2]
        cstate[6] += 1
        result_geodes.append(calculate_geodes(blueprint, cstate))
    # Segunda opção gera mais um robô tipo ore, se isso for possível
    if( copy_state[1] >= blueprint[1] ):
        cstate = copy_state[:]
        cstate[1] -= blueprint[1]
        cstate[5] += 1
        result_geodes.append(calculate_geodes(blueprint, cstate))
    # Primeira opção: não faz nada e deixa acumular mais recursos
    result_geodes.append(calculate_geodes(blueprint, copy_state))
    
    # Agora vamos retornar a opção mais rentável
    return max(result_geodes)

for blueprint in blueprints:
    start_state = [0,0,0,0,0,1,0,0,0]
    print(blueprint[0], calculate_geodes(blueprint, start_state))