import os
f = open(f"{os.path.dirname(__file__)}/input04.txt", "r")

count_full_contain = 0
# Lendo cada par
for line in f.readlines():
    line = line.replace("\n","")
    # Separando em cada elfo
    elf1, elf2 = line.split(",")
    
    # Separando as seções de cada elfo
    elf1_L, elf1_H = [int(t) for t in elf1.split("-")]
    elf2_L, elf2_H = [int(t) for t in elf2.split("-")]
    
    # print(elf1_L, elf1_H, elf2_L, elf2_H)
    # Para avaliar se houve uma inclusão inteira basta comparar os valores de mínimo e máximo 
    if( ( elf1_L >= elf2_L and elf1_H <= elf2_H ) or ( elf2_L >= elf1_L and elf2_H <= elf1_H ) ):
        count_full_contain += 1
    
print(f"{count_full_contain}")