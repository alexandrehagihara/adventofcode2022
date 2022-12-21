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
    
def get_value(monkey_name):
    monkey = monkeys[monkey_name]
    # Só valor
    if( len(monkey) == 1 ):
        return monkey[0]

    # Expressão
    monkey_left = get_value(monkey[0])
    monkey_right = get_value(monkey[2])
    if( monkey[1] == '+' ):
        return monkey_left + monkey_right
    elif( monkey[1] == '-' ):
        return monkey_left - monkey_right
    elif( monkey[1] == '*' ):
        return monkey_left * monkey_right
    elif( monkey[1] == '/' ):
        return monkey_left / monkey_right
    print("?", monkey_name, monkey)
        
print(get_value("root"))