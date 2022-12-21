import os
f = open(f"{os.path.dirname(__file__)}/input21.txt", "r")

monkeys = {}

for line in f.readlines():
    parse = line.strip().split()
    # Apenas valor
    if( len(parse) == 2 ):
        monkeys[parse[0][:-1]] = [int(parse[1])]
    # Expressão: monkey_left operação monkey_right
    else:
        monkeys[parse[0][:-1]] = [parse[1],parse[2],parse[3]]

def replace_expression(monkey_name):
    monkey = monkeys[monkey_name]
    if( monkey_name == 'root'):
        return f"({replace_expression(monkey[0])}) = ({replace_expression(monkey[2])})"
    elif( monkey_name == 'humn'):
        return 'x'
    else:
        if( len(monkey) == 1):
            return f"{monkey[0]}"
        else:
            return f"({replace_expression(monkey[0])}) {monkey[1]} ({replace_expression(monkey[2])})"

expression = replace_expression("root")

print(expression)

# Peguei o resultado da expressão e coloquei para resolver no site https://www.mathpapa.com/algebra-calculator.html
# Este site retornou x = 4795129184698945 / 1296, que pela calculadora dá 3.699.945.358.564,0007716049382716049
# Eu coloquei então o valor 3699945358564, assumindo que houve algum erro de arredondamento no site, e deu certo!
