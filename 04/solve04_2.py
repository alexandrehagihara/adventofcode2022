import os
f = open(f"{os.path.dirname(__file__)}/input04.txt", "r")

count_overlap = 0
# Lendo cada par
for line in f.readlines():
    line = line.replace("\n","")
    # Separando em cada elfo
    elf1, elf2 = line.split(",")
    
    # Separando as seções de cada elfo
    elf1_L, elf1_H = [int(t) for t in elf1.split("-")]
    elf2_L, elf2_H = [int(t) for t in elf2.split("-")]
    
    # print(elf1_L, elf1_H, elf2_L, elf2_H)
    # Para avaliar se houve uma sobreposição, basta que uma dos seções de um dos elfos esteja dentro da
    # faixa de seções do outro elfo
    if( ( elf1_L >= elf2_L and elf1_L <= elf2_H ) or ( elf1_H >= elf2_L and elf1_H <= elf2_H ) or
        ( elf2_L >= elf1_L and elf2_L <= elf1_H ) or ( elf2_H >= elf1_L and elf2_H <= elf1_H ) ):
        count_overlap += 1
    
print(f"{count_overlap}")