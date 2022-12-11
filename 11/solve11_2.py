# Não vou fazer o parsing do arquivo de entrada porque são poucos macacos e fica mais fácil só declarar
# a lista no código mesmo 

# Nossa lista de entrada. Cada macaco é um dicionário.
monkey_list = [
    {
        'items': [83, 88, 96, 79, 86, 88, 70],
        'operation': lambda old : old * 5,
        'test': 11,
        'true': 2,
        'false': 3,
        'inspected': 0
    },
    {
        'items': [59, 63, 98, 85, 68, 72],
        'operation': lambda old : old * 11,
        'test': 5,
        'true': 4,
        'false': 0,
        'inspected': 0
    },
    {
        'items': [90, 79, 97, 52, 90, 94, 71, 70],
        'operation': lambda old : old + 2,
        'test': 19,
        'true': 5,
        'false': 6,
        'inspected': 0
    },
    {
        'items': [97, 55, 62],
        'operation': lambda old : old + 5,
        'test': 13,
        'true': 2,
        'false': 6,
        'inspected': 0
    },
    {
        'items': [74, 54, 94, 76],
        'operation': lambda old : old * old,
        'test': 7,
        'true': 0,
        'false': 3,
        'inspected': 0
    },
    {
        'items': [58],
        'operation': lambda old : old + 4,
        'test': 17,
        'true': 7,
        'false': 1,
        'inspected': 0
    },
    {
        'items': [66, 63],
        'operation': lambda old : old + 6,
        'test': 2,
        'true': 7,
        'false': 5,
        'inspected': 0
    },
    {
        'items': [56, 56, 90, 96, 68],
        'operation': lambda old : old + 7,
        'test': 3,
        'true': 4,
        'false': 1,
        'inspected': 0
    },
]

# print(monkey_list) # Apena

# Agora é um número bem maior de rodadas
for rounds in range(10000):
    # Varre a lista de macacos
    for monkey in monkey_list:
        # Antes de tudo, incrementa o contador de itens inspecionados
        monkey['inspected'] += len(monkey['items'])
        # Faz as inspeções dos itens
        for i in monkey['items']:
            # Aplica a operação que modifica o nível de preocupação.
            # Para não explodir, vamos ficar dentro da faixa de valores modulo 9699690 (2*3*5*7*11*13*17*19)
            new = monkey['operation'](i) % 9699690
            # Aplica o teste neste item e redireciona para a lista do macaco de destino
            if new % monkey['test'] == 0:
                monkey_list[monkey['true']]['items'].append(new)
            else:
                monkey_list[monkey['false']]['items'].append(new)
        # Esvazia a lista do macaco atual
        monkey['items'] = []

# Extraindo as informações de número de inspeções dos macacos
inspection_list = [ m['inspected'] for m in monkey_list ]
# Ordena e multiplica os 2 maiores
inspection_list.sort(reverse=True,)
print(inspection_list[0] * inspection_list[1])