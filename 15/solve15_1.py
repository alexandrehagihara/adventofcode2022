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



line_cant = set()
for sb in sensor_beacon:
    # Esta é a distância máxima que este sensor consegue detectar
    manhattan = abs(sb[0]-sb[2]) + abs(sb[1]-sb[3])
    # Verifica se tem algum ponto na linha y de interesse que faz parte desta distância
    if manhattan >= abs(sb[1]-y_interest):
        max_dx = manhattan - abs(sb[1]-y_interest)
        for x in range(sb[0], sb[0]+max_dx+1 ):
            line_cant.add(x)
        for x in range(sb[0], sb[0]-max_dx-1, -1):
            line_cant.add(x)

# Removendo do conjunto aqueles pontos que contém um beacon
for sb in sensor_beacon:
    if( sb[3] == y_interest and sb[2] in line_cant ):
        line_cant.remove(sb[2])

print([i for i in line_cant])
print(len(line_cant))