import os
# f = open(f"{os.path.dirname(__file__)}/example15.txt", "r")
# y_interest = 10
f = open(f"{os.path.dirname(__file__)}/input15.txt", "r")
y_interest = 2000000


sensor_beacon = []
for line in f.readlines():
    info = line.split(" ")
    sensor_x = int(info[2].replace(",","").split("=")[1])
    sensor_y = int(info[3].replace(":","").split("=")[1])
    beacon_x = int(info[8].replace(",","").split("=")[1])
    beacon_y = int(info[9].replace("\n","").split("=")[1])
    
    sensor_beacon.append([sensor_x, sensor_y, beacon_x, beacon_y])

def union_interval(main_interval, new_interval):
    # Varre todos os intervalos e faz a fusão com o novo intervalo caso isso seja possível
    # Novo intervalo: [a,b]
    # Intervalo atual: [c,d]
    # Caso b >= c ou caso d >= a, temos um caso de intervalos que podem sofrer fusão
    merged = True
    while(merged):
        merged = False
        for interval in main_interval:
            a, b = new_interval
            c, d = interval
            if ( c-1 <= a <= d+1 ) or ( c-1 <= b <= d+1 ) or ( a-1 <= c <= b+1 ) or ( a-1 <= d <= b+1 ):
                new_interval = [min(a,c), max(b,d)]
                main_interval.remove(interval)
                merged = True
        
        
    main_interval.append(new_interval)

for y_interest in range(0,4000000):
    line_interval = []
    # line_cant = set()
    for sb in sensor_beacon:
        # Esta é a distância máxima que este sensor consegue detectar
        manhattan = abs(sb[0]-sb[2]) + abs(sb[1]-sb[3])
        # Verifica se tem algum ponto na linha y de interesse que faz parte desta distância
        if manhattan >= abs(sb[1]-y_interest):
            max_dx = manhattan - abs(sb[1]-y_interest)
            union_interval(line_interval, [sb[0]-max_dx, sb[0]+max_dx])
    if(len(line_interval) > 1):
        print(y_interest, line_interval)
        # Demorou mas imprimiu "3367718 [[2721115, 4602545], [-1541414, 2721113]]", ou seja, o valor x é 2721114 e o y é o 3367718


